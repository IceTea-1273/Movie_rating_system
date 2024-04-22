from abc import ABC, abstractmethod
import movieChoosing

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
        title = movieChoosing.movie_searcher()
        if title is None:
            print("No movies found")
            return
        file_path = self._get_file_path(username, 'TOWATCH')
        with open(file_path, 'r') as f:
            existing_movies = [line.strip() for line in f]
        if title in existing_movies:
            print(f"'{title}' is already in the To-Watch List.")
        else:
            with open(file_path, 'a') as f:
                    f.write(f"{title}\n")
            print(f"Added '{title}' to To-Watch List")

    def remove_from_list(self, username):
        file_path = self._get_file_path(username, 'TOWATCH')
        with open(file_path, 'r') as f: 
            lines = f.readlines()
        self.display_list(username)
        while True:
            title = input("Which movie would you like to remove? (nr) ")
            if not title.isdigit():
                print(f"Invalid choice. Please enter a number between 1 and {len(lines)}.")
                continue
            title = int(title) - 1
            if not (0 <= title <= len(lines)):
                print(f"Invalid choice. Please enter a number between 1 and {len(lines)}.")
                continue
            break
        removed = lines.pop(title)
        with open(file_path, 'w') as f: 
            for line in lines:
                f.write(line) 
        print(f"Removed '{removed.strip()}' from To-Watch List")

    def move_to_watched(self, username):
        file_path = self._get_file_path(username, 'TOWATCH')
        with open(file_path, 'r') as f: 
            lines = f.readlines()
        self.display_list(username)
        while True:
            title = input("Which movie did you watch from your To-Watch list? (nr) ")
            if not title.isdigit():
                print(f"Invalid choice. Please enter a number between 1 and {len(lines)}.")
                continue
            title = int(title)
            if not (1 <= title <= len(lines)):
                print(f"Invalid choice. Please enter a number between 1 and {len(lines)}.")
                continue
            while True:
                rating = input("What do you rate this movie 1-10? ")
                if not rating.isdigit():
                    print("Invalid choice. Please enter a number between 1 and 10.")
                    continue
                rating = int(rating)
                if not (1 <= rating <= 10):
                    print("Invalid choice. Please enter a number between 1 and 10.")
                    continue
                break
            break
        removed = lines.pop(title-1)
        with open(file_path, 'w') as f:
            for line in lines:
                f.write(line)
        file_path = self._get_file_path(username, 'WATCHED')

        with open(file_path, 'a') as f:
            f.write(f"'{removed.strip()}' Rating: {rating}\n")
        print(f"Moved {removed.strip()} to Watched list")


    def display_list(self, username):
        print("To watch list: ")
        file_path = self._get_file_path(username, 'TOWATCH')
        with open(file_path, 'r') as f: 
            count = 1
            for line in f:
                print(f'{count}. {line.strip()}')
                count += 1   


class WatchedList(ListStrategy):
    def add_to_list(self, username):
        title = movieChoosing.movie_searcher()
        if title is None:
            print("No movies found")
            return
        file_path = self._get_file_path(username, 'WATCHED')
        with open(file_path, 'r') as f:
            existing_movies = [line.strip().split(" ")[0] for line in f]
        if title in existing_movies:
            print(f"'{title}' is already in the Watched List.")
        else:
            while True:
                rating = input("What do you rate this movie 1-10? ")
                if not rating.isdigit():
                    print("Invalid choice. Please enter a number between 1 and 10.")
                    continue
                rating = int(rating)
                if not (1 <= rating <= 10):
                    print("Invalid choice. Please enter a number between 1 and 10.")
                    continue
                break
            with open(file_path, 'a') as f:
                f.write(f"'{title}' Rating: {rating}\n")
        print(f"Added '{title}' to Watched List")

    def remove_from_list(self, username):
        file_path = self._get_file_path(username, 'WATCHED')
        with open(file_path, 'r') as f:
            lines = f.readlines()
        self.display_list(username)
        while True:
            title = input("Which movie would you like to remove? (nr) ")
            if not title.isdigit():
                print(f"Invalid choice. Please enter a number between 1 and {len(lines)}.")
                continue
            title = int(title) -1
            if not (0 <= title <= len(lines)):
                print(f"Invalid choice. Please enter a number between 1 and {len(lines)}.")
                continue
            break
        removed = lines.pop(title)
        with open(file_path, 'w') as f: 
            for line in lines:
                f.write(line) 
        print(f"Removed '{removed.strip()}' from Watched List")

    def display_list(self, username):
        print("Watched list: ")
        file_path = self._get_file_path(username, 'WATCHED')
        with open(file_path, 'r') as f: 
            count = 1
            for line in f:
                print(f'{count}. {line.strip()}')
                count += 1
    
    def move_to_watched(self, username):
        pass


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
        if isinstance(self._strategy, ToWatchList):
            self._strategy.move_to_watched(username)
        else:
            print("Error: This method is not supported by the current strategy.")

