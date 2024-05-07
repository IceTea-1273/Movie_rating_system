# Coursework repot

## Introduction

The objective of the coursework was to learn about object-oriented programming and implement it in an application of your own choice. I chose the topic Movie rating system and created an application that lets users create profiles and manage movie lists. Running this program requires several steps: 
* Ensuring that [Python](https://www.python.org/) is installed in the system 
* Ensuring that the required packages or libraries are installed using pip. This program needs modules “[pwinput](https://pypi.org/project/pwinput/)”, “[openai](https://pypi.org/project/openai/)”, “[imdbpy](https://pypi.org/project/IMDbPY/)”.
* Since the program integrates OpenAI functionality, there is a need to set up an OpenAI API key as a local variable in each new environment. This can be done by following a tutorial (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
* Locating the directory of the project and the “main.py” file 
* Launching the file using a command prompt, or using an IDE (integrated development environment), such as PyCharm or Visual Studio Code to run the “main.py” file.  

Once the program is launched, users need to follow the prompts shown in the terminal. The program guides users through various actions such as creating user profiles and managing movie lists. 

## Analysis of the program 

The program had some functionality requirements.  All 4 OOP pillars and 2 design patterns. Now, I will go over them and explain what they are and how they were used in my program.  

### 4 pillars of OOP

**Polymorphism** 

In object-oriented programming, polymorphism allows objects of different classes to be treated as objects of a common superclass. This means that one interface can represent multiple forms of data. Objects can perform actions with the same method name, but with different implementations based on their specific class. It enhances code flexibility and reusability by allowing a single interface to represent various data types or objects. Polymorphism can occur through method overloading, where multiple methods have the same name but different parameters, or through method overriding, where a subclass provides a specific implementation of a method defined in its superclass. 

In my code, I use method overriding to implement polymorphism. In these two code snippets, I have different classes with the same superclass, containing a method with the same signatures. This displays polymorphism, as the superclass method is being overridden, and each of the methods can be called, even if they have the same name. 

```Python
class ToWatchList(ListStrategy): 

    def display_list(self, username): 
        print("To watch list: ") 
        file_path = self._get_file_path(username, 'TOWATCH') 
        with open(file_path, 'r') as f:  
            count = 1 
            for line in f: 
                print(f'{count}. {line.strip()}') 
                count += 1 

class WatchedList(ListStrategy): 

    def display_list(self, username): 
        print("Watched list: ") 
        file_path = self._get_file_path(username, 'WATCHED') 
        with open(file_path, 'r') as f:  
            count = 1 
            for line in f: 
                print(f'{count}. {line.strip()}') 
                count += 1 
```

**Abstraction** 

Abstraction in object-oriented programming is the concept of simplifying complex systems by hiding unnecessary implementation details while emphasizing essential features. It allows developers to focus on what an object does rather than how it achieves its functionality. Abstraction is achieved through abstract classes and interfaces, which define a blueprint for other classes to follow without specifying their exact implementation. This promotes code reusability, modularity, and easier maintenance by creating a clear separation between the interface and the implementation. 

In my code I use abstraction through abstract methods. The “ListStrategy” class is declared as an abstract class, which means it cannot be instantiated directly. It has abstract methods, which are defined, but not implemented. This class acts as a template or blueprint for other classes to inherit from. Subclasses that inherit this class, are required to implement these abstract methods, providing their specific implementation details. 
 
 ```Python
 class ListStrategy(ABC): 

    @abstractmethod 
    def add_to_list(self, username): 
        pass 

    @abstractmethod 
    def remove_from_list(self, username): 
        pass 

    @abstractmethod 
    def display_list(self, username): 
        pass 

    @abstractmethod 
    def move_to_watched(self,username): 
        pass 
```

**Inheritance** 

Inheritance in OOP is a mechanism that allows the creation of a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties (methods) from another class. This allows the child class to reuse the code of the parent class, reducing redundancy and promoting code reusability. 

In my program, I’ve created a class “Validation”, and a class “CreateUserProfile”, that inherits from the previous class. Inheritance is used in my code to reuse and extend functionality from the “Validation” class in the “CreateUserProfile” class. That means it gains access to all of the methods from the “Validation” class and can use them without having to redefine them. By inheriting from “Validation”, “CreateUserProfile” can focus on adding additional behaviour specific to user profile creation, such as initializing user attributes like email, password, username, and date of birth.Inheritance promotes code reuse, simplifies maintenance, and helps in creating a more organized code. 

```Python
class Validation: 

    def _get_valid_email(self): 
        email = input('Enter your email: ') 
        while not self._is_valid_email(email): 
            print("Invalid email format. Please enter a valid email address.") 
            email = input('Enter your email: ') 
        return email 
        
    def _is_valid_email(self, email): 
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
        return bool(re.match(pattern, email)) 
     
    def _get_valid_password(self): 
        while True: 
            password = pwinput.pwinput("Enter your password: ") 
            if len(password.strip()) < 8 or len(password.strip()) > 20: 
                print("Password must be 8-20 characters long.") 
            else: 
                return password    

    def _get_valid_username(self): 
            while True: 
                username = input('Create a username: ') 
                if not username: 
                    print("Username can't be empty.") 
                    continue 
                if not self._is_valid_username(username): 
                    print("Invalid username. Too short too long, or contaisn invalid characters.
                          Username can only contain letters, numbers, -, _, ., and ().") 
                    continue 
                return username 
             
    def _is_valid_username(self, username): 
        pattern = r'^[\w\-.()]{3,20}$' 
        return bool(re.match(pattern, username))  
        
    def _get_valid_date_of_birth(self): 
        while True: 
            date_of_birth = input('What is your date of birth?(YYYY MM DD): ') 
            if self._is_valid_date_of_birth(date_of_birth): 
                return date_of_birth 
            else: 
                print("Invalid date format. Please enter your date of birth in YYYY MM DD format.") 

    def _is_valid_date_of_birth(self, date_of_birth): 
        try: 
            year, month, day = map(int, date_of_birth.split()) 
            input_date = datetime.datetime(year, month, day) 
            current_date = datetime.datetime.now() 
            if input_date >current_date: 
                return False 
            return True 
        except ValueError: 
            return False 


class CreateUserProfile(Validation): 

    def __init__(self): 
        self.__email = self._get_valid_email() 
        self.__password = self._get_valid_password() 
        self.__username = self._get_valid_username() 
        self.__date_of_birth = self._get_valid_date_of_birth()
```

**Encapsulation** 

Encapsulation in OOP describes the idea of wrapping data and the methods that work on data within one unit, a class. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed or accessed by an object’s methods, called getters and setters. 

There are few levels of Encapsulation that can be used. Public variables and methods can be accessed outside of classes, without setter or getter methods, which can cause security issues or accidental change of data. Protected elements are accessible within the class where they are declared and within subclasses (classes that inherit from the parent class). They cannot be accessed directly from outside the class, but can be accessed by subclasses. However, in Python, it is just a convention, which means you technically can access protected members from outside the class, but it's generally considered best practice to treat them as if they were private and refrain from accessing them directly. Finally, private variables and methods are accessible only within the class where they are declared. They cannot be accessed or modified directly from outside the class. Access to private members is restricted to methods defined within the same class (getters and setters). 

In my code, I used both private and protected elements, to ensure that no data can be accidentally changed. The “CreateUserProfile” class, that inherits protected methods from the “Validation” class, can use them to set private attributes, such as email and password. These attributes can’t be accessed outside of the class, so I set up a getter method “get_username”, that returns the private username attribute. 

```Python
class CreateUserProfile(Validation): 

    def __init__(self): 
        self.__email = self._get_valid_email() 
        self.__password = self._get_valid_password() 
        self.__username = self._get_valid_username() 
        self.__date_of_birth = self._get_valid_date_of_birth() 

    def get_username(self): 
        return self.__username 
```

### Design patterns

Design patterns in object-oriented programming are reusable solutions to common software design problems. They provide a structured approach for solving specific design challenges and promote code reusability, modularity, and scalability. There are three main types of design patterns: creational, structural, and behavioural, each addressing different aspects of software design and development. The pattern is not a specific piece of code, but a general concept for solving a particular problem. The design patterns that I used in my code are Singleton and Strategy design patterns. 

**Singleton design pattern** 

The Singleton design pattern solves the problem of ensuring that a class has only one instance and provides a global point of access to that instance. This is useful in scenarios where you need exactly one instance of a class to coordinate actions across the system, such as managing a shared resource or controlling access to a resource 

In my case, I used the Singleton pattern to make sure that only one instance of the class  “IMDbWrapper” exists. The IMDbWrapper class interacts with an external resource (the IMDb movie database). Creating multiple instances of this class would mean establishing multiple connections to the database, which is unnecessary and inefficient. By using a Singleton, I ensure that only one connection to the IMDb database is established and reused by all parts of the program. 

```Python
class IMDbWrapper: 
    _instance = None 

    def __new__(cls): 
        if not cls._instance: 
            cls._instance = super().__new__(cls) 
        return cls._instance 
```

**Strategy design pattern**

The Strategy Design Pattern, a behavioural pattern, enables dynamic behaviour modification by encapsulating objects within interchangeable strategies, helping objects change their behaviour by swapping them with different strategies. Each strategy represents a specific algorithm or behaviour, enabling easy swapping at runtime without altering client code. The Strategy pattern lets you switch between different ways of doing something, depending on the situation This promotes flexibility, modularity, and maintainability. Overall, it offers a structured approach to dynamically adapt object behaviour, ensuring system adaptability and scalability in complex software environments.

![](https://i0.wp.com/www.e4developer.com/wp-content/uploads/2018/10/strategy-pattern.png?w=669&ssl=1)

In my code, I used the Strategy design pattern to organize different ways of managing movie lists. This pattern allows me to encapsulate each list management strategy (such as adding or removing from different lists) into separate classes, making it easy to switch between strategies without changing the core code.  

The Strategy interface contains a set of abstract methods that define the behaviours and actions associated with managing lists, such as adding to a list and displaying a list.  

```Python
# Strategy interface 
class ListStrategy(ABC): 

    @abstractmethod 
    def add_to_list(self, username): 
        pass 

    @abstractmethod 
    def remove_from_list(self, username): 
        pass 

    @abstractmethod 
    def display_list(self, username): 
        pass 

    @abstractmethod 
    def move_to_watched(self,username): 
        pass 
```

Then follow the concrete classes “ToWatchList(ListStrategy)” and “WatchedList(ListStrategy)”, that inherit from the ListStrategy class. These classes implement the methods defined in th ListStrategy interface. Each concrete strategy provides a distinct way of performing a task or achieving a goal, letting the context decide which strategy to use when performing a task. 

Lastly, the context is represented by the ListManager class. It acts as an interface between the other code and the concrete strategies. It holds a reference to a strategy object and delegates tasks to it based on the current strategy set. 

```Python
# Context 
class ListManager: 
    def __init__(self, strategy: ListStrategy): 
        self._strategy = strategy 

    def set_strategy(self, strategy: ListStrategy): 
        self._strategy = strategy 

    def add_to_list(self, username): 
        self._strategy.add_to_list(username) 

    def remove_from_list(self, username): 
        self._strategy.remove_from_list(username) 

    def display_list(self, username): 
        self._strategy.display_list(username) 
 ```
 
 ## Results 

I successfully created a program that lets users create profiles and manage movie lists. However, I faced some challenges during the process.
* Since this is my first project with Python and object-oriented programming, learning all the syntax and making decisions about which design patterns to use, was quite difficult 
* Learning how to use Git and GitHub proved to be extremely helpful, as it allows me to review the progress made from the start of the project and share my program with the community 
* Unit testing was completely new and challenging for me. I made the mistake of leaving the unit testing as the last task in my project, which was not a good idea. Testing should take place during the writing of the program, to ensure that the code is working as intended. 
* Finally, managing the creation of the project alongside other studies was pretty though. Time management is crucial while working on a project, but since many things were new, it sometimes took more time to complete tasks that didn’t seem as difficult at the start.  

## Summary 

The outcome of the coursework is the successful creation of a Python program for managing movie lists. This work enabled me to learn and understand Python, object-oriented programming, and the four pillars of OOP, including design patterns and program testing. The result of my work is a functional program that allows users to create and manage movie lists. Although the program functions correctly, there are several areas for improvement. Firstly, instead of working with .txt files, integrating databases would provide more security, offering features such as user authentication and data encryption. Additionally, implementing a user interface, using libraries such as tkinter or NiceGUI would enhance usability and user experience. If these enhancements are successfully implemented, it would be possible to create a working application and deploy it for practical use. In conclusion, this work made me understand object-oriented programming and practices used in software development, but there is plenty of space to improve. 
 







