import getpass  # for hiding password on input
import os


class CreateUserProfile:
    def __init__(self):
        self._email = input('Enter your email: ')
        self._password = getpass.getpass("Enter your password: ")
        self._username = input('Create a username: ')
        self._date_of_birth = input('What is your date of birth?(YYYY MM DD): ')
        
        if not os.path.exists(f'X:/Python/kursinis/try/userProfiles/{self._username}'):
            os.makedirs(f'X:/Python/kursinis/try/userProfiles/{self._username}')
            print(f"Folder {self._username} created successfully.")
        else:
            print(f"Folder '{self._username} already exists.")
        
        with open(f'X:/Python/kursinis/try/userProfiles/{self._username}/{self._username}.txt', 'w') as f:
            f.write(f'{self._email}\n{self._password}\n{self._username}\n{self._date_of_birth}\n')

    def display_profile(self):
        print("User Profile:")
        print("Email:", self._email)
        print("Username:", self._username)
        print("Date of Birth:", self._date_of_birth)


def delete_profile(username):
    os.remove(f'X:/Python/kursinis/try/userProfiles/{username}.txt')



first_profile = CreateUserProfile()
first_profile.display_profile()
