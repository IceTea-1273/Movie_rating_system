import pwinput
import os
import re
import datetime

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
                    print("Invalid username. Username can only contain letters, numbers, -, _, ., and ().")
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
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False


class CreateUserProfile(Validation):

    def __init__(self):
        self.__email = self._get_valid_email()
        self.__password = self._get_valid_password()
        self.__username = self._get_valid_username()
        self.__date_of_birth = self._get_valid_date_of_birth()    
        
    def creating_user(self):
        user_dir = os.path.join(os.curdir, "userProfiles", self.__username)
        if os.path.exists(user_dir):
            print(f"The username '{self.__username}' already exists. Please choose a different username or try logging in.")
            return False
        os.makedirs(user_dir)
        print(f"Welcome, {self.__username}! Account created successfully.")
        profile_file_path = os.path.join(user_dir, f"{self.__username}.txt")
        with open(profile_file_path, 'w') as f:
            f.write(f'{self.__email}\n{self.__password}\n{self.__username}\n{self.__date_of_birth}\n')
        open(os.path.join(user_dir, "TOWATCH.txt"), 'w').close()
        open(os.path.join(user_dir, "WATCHED.txt"), 'w').close()
        return True

    def get_username(self):
        return self.__username


def sign_up():
    print('Signing up')
    create_profile = CreateUserProfile()
    succes = create_profile.creating_user()
    username = create_profile.get_username()
    return succes, username


def log_in():
    print('Logging in')
    username = input('Input your username: ')
    user_dir = os.path.join(os.curdir, "userProfiles", username)
    if not os.path.exists(user_dir):
        print(f"Username '{username}' doesn't exist, try signing up")
        return False, username
    else:
        while True:
            password = pwinput.pwinput('Input your password: ')
            user_file_path = os.path.join(user_dir, f"{username}.txt")
            with open(user_file_path, 'r') as f:
                file = f.readlines()
                if password == file[1].strip():
                    print(f'Succsesfully logged in')
                    break
                else:
                    print('Incorrect password! Try again')
                    continue
        return True, username