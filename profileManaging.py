import getpass  # for hiding password on input
import os


class CreateUserProfile:
    def __init__(self):
        self.__email = input('Enter your email: ')
        self.__password = getpass.getpass("Enter your password: ")
        self.__username = input('Create a username: ')
        self.__date_of_birth = input('What is your date of birth?(YYYY MM DD): ')
        
    def creating_user(self):
        if not os.path.exists(f'X:/Python/kursinis/try/userProfiles/{self.__username}'):
            os.makedirs(f'X:/Python/kursinis/try/userProfiles/{self.__username}')
            print(f"Welcome, {self.__username}. Account created successfully.")
            with open(f'X:/Python/kursinis/try/userProfiles/{self.__username}/{self.__username}.txt', 'w') as f:
                f.write(f'{self.__email}\n{self.__password}\n{self.__username}\n{self.__date_of_birth}\n')
            with open(f'X:/Python/kursinis/try/userProfiles/{self.__username}/TOWATCH.txt', 'w'):
                pass
            with open(f'X:/Python/kursinis/try/userProfiles/{self.__username}/WATCHED.txt', 'w'):
                pass
            return True
        else:
            print(f"The username '{self.__username}' already exists, try logging in or using a different username.")
            return False
        
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
    if not os.path.exists(f'X:/Python/kursinis/try/userProfiles/{username}'):
        print(f"Username '{username}' doesn't exist, try signing up")
        return False, username
    else:
        while True:
            password = input('Input your password: ')
            with open(f'X:/Python/kursinis/try/userProfiles/{username}/{username}.txt', 'r') as f:
                file = f.readlines()
                if password == file[1].strip():
                    print(f'Succsesfully logged in')
                    break
                else:
                    print('Incorrect password! Try again')
                    continue
        return True, username


def delete_profile(username):
    os.remove(f'X:/Python/kursinis/try/userProfiles/{username}.txt')

