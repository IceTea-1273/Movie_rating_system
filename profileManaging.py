import getpass  # for hiding password on input
import os


class CreateUserProfile:
    def __init__(self):
        self._email = input('Enter your email: ')
        self._password = getpass.getpass("Enter your password: ")
        self._username = input('Create a username: ')
        self._date_of_birth = input('What is your date of birth?(YYYY MM DD): ')
        
    def creating_user(self):
        if not os.path.exists(f'X:/Python/kursinis/try/userProfiles/{self._username}'):
            os.makedirs(f'X:/Python/kursinis/try/userProfiles/{self._username}')
            print(f"Welcome, {self._username}. Account created successfully.")
            with open(f'X:/Python/kursinis/try/userProfiles/{self._username}/{self._username}.txt', 'w') as f:
                f.write(f'{self._email}\n{self._password}\n{self._username}\n{self._date_of_birth}\n')
            return True
        else:
            print(f"The username '{self._username}' already exists, try logging in or using a different username.")
            return False

    def display_profile(self):
        print("User Profile:")
        print("Email:", self._email)
        print("Username:", self._username)
        print("Date of Birth:", self._date_of_birth)

def user_login():
    username = input('Input your username: ')
    if not os.path.exists(f'X:/Python/kursinis/try/userProfiles/{username}'):
        print(f"Username {username} doesn't exist, try signing up")
    else:
        password = getpass.getpass('Input your password: ')
        with open(f'X:/Python/kursinis/try/userProfiles/{username}/{username}.txt', 'r') as f:
            file = f.readlines()
            while password != file[1]:
                print('Incorrect password! Try again')
                continue
            print(f'Succsesfully logged in, welcome back, {username}!')

def delete_profile(username):
    os.remove(f'X:/Python/kursinis/try/userProfiles/{username}.txt')

