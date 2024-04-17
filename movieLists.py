from abc import ABC, abstractmethod

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

    def _get_file_path(self, username, list_type):
        return f'X:/Python/kursinis/try/userProfiles/{username}/{list_type}.txt'



# Concrete strategies
class ToWatchList(ListStrategy):

    def add_to_list(self, username):
        title = input("What movie would you like to add? ")
        file_path = self._get_file_path(username, 'TOWATCH')
        with open(file_path, 'a') as f:
                f.write(f"{title}\n")
        print(f"Added '{title}' to To-Watch List")

    def remove_from_list(self, username):
        title = int(input("Which movie would you like to remove? (nr)"))
        file_path = self._get_file_path(username, 'TOWATCH')
        with open(file_path, 'r') as f:
            lines = f.readlines()
            removed = lines.pop(title-1)
        with open(file_path, 'w') as f: 
            for line in lines:
                f.write(str(line))   
        print(f"Removed '{title}' from To-Watch List")

    def move_to_watched(self, username):
        self.display_list(username)
        file_path = self._get_file_path(username, 'TOWATCH')
        title = int(input("Which movie did you watch from your To-Watch list? (nr)"))
        with open(f'X:/Python/kursinis/try/userProfiles/{username}/TOWATCH.txt', 'r') as f:
            lines = f.readlines()
            removed = lines.pop(title-1)
        file_path = self._get_file_path(username, 'WATCHED')
        with open(file_path, 'r') as f:
            f.write(f"{removed}\n")


    def display_list(self, username):
        print('To watch list: ')
        file_path = self._get_file_path(username, 'TOWATCH')
        with open(file_path, 'r') as f: 
            count = 1
            for line in f:
                print(f'{count}. {line}')
                count += 1   


class WatchedList(ListStrategy):
    def add_to_list(self, username):
        title = input("What movie would you like to add? ")
        rating = input("What do you rate this movie 1-10? ")
        file_path = self._get_file_path(username, 'WATCHED')
        with open(file_path, 'a') as f:
                f.write(f"'{title}\n' Rating: {rating}")
        print(f"Added '{title}' to Watched List")

    def remove_from_list(self, username):
        title = int(input("Which movie would you like to remove? (nr)"))
        file_path = self._get_file_path(username, 'WATCHED')
        with open(file_path, 'r') as f:
            lines = f.readlines()
            removed = lines.pop(title-1)
        with open(file_path, 'w') as f: 
            for line in lines:
                f.write(str(line))   
        print(f"Removed '{title}' from Watched List")

    def display_list(self, username):
        print('Watched list: ')
        file_path = self._get_file_path(username, 'WATCHED')
        with open(file_path, 'r') as f: 
            lines = f.readlines()
            count = 1
            for line in lines:
                print(f'{count}. {line}')
                count += 1



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

    def move_to_watched(self, username):
        if isinstance(self._strategy, WatchedList):
            self._strategy.move_to_watched(username)
        else:
            print("Error: This method is not supported by the current strategy.")

# Client code
def main():
    # Initialize with To-Watch List strategy
    manager = ListManager(ToWatchList())
    manager.add_to_list('iceTea')
    manager.display_list('iceTea')
    manager.remove_from_list('iceTea')
    manager.display_list('iceTea')
    manager.add_to_list('iceTea')
    manager.display_list('iceTea')


 #   # Switch to Watched List strategy
  #  manager.set_strategy(WatchedList())
  #  manager.add_to_list("Movie X")
  #  manager.display_list()

if __name__ == "__main__":
    main()