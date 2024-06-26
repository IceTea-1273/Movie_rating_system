import profileManaging
import movieLists as m
import movieRecomendations as r
import os

def start():
    global username
    user_profiles_dir = os.path.join(os.curdir, "userProfiles")
    if not os.path.exists(user_profiles_dir):
        os.makedirs(user_profiles_dir)
        print("User profiles directory created.")
        
    running = True
    while running:
        print("\n1. Sign up")
        print("2. Log in")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            success, username = profileManaging.sign_up()
            if success:
                return True
            else:
                continue
            
        elif choice == "2":
            success, username = profileManaging.log_in()
            if success:
                print(f"Welcome back, {username}!")
                return True
            else:
                continue
               
        elif choice == "3":
            print("Exiting program.")
            return False
        else:
            print("Invalid choice. Please try again.")
    return username

def functions():
    running = True
    manager = m.ListManager(m.ToWatchList())
    movie_rec = r.RecomendMovies()
    while running:
        print("\nWhat would you like to do? ")
        print("1. Display to-watch list")
        print("2. Manage to-watch list")
        print("3. Display watched list")
        print("4. Manage watched list")
        print("5. Get a recomendation")
        print("6. Exit program")
        choice = input("Choose an option: \n")

        if choice == '1':
            manager.set_strategy(m.ToWatchList())
            manager.display_list(username)
        elif choice == '2':
            while True:
                print("\n'Add', 'remove', 'move' to Watched List, 'back'.")
                manage = input().strip().lower()
                if manage == 'add':
                    manager.set_strategy(m.ToWatchList())
                    print('\n')
                    manager.add_to_list(username)
                elif manage == 'remove':
                    print('\n')
                    manager.set_strategy(m.ToWatchList())
                    manager.remove_from_list(username)
                elif manage == 'move':
                    print('\n')
                    manager.set_strategy(m.ToWatchList())
                    manager.move_to_watched(username)
                elif manage =='back':
                    print('\n')
                    break 
                else:
                    print('\n')
                    print("Such a function doesn't exist")
                    continue
        elif choice == '3':
            manager.set_strategy(m.WatchedList())
            manager.display_list(username)
        elif choice == '4':
            while True:
                print("\n'Add', 'remove' from list, 'back'.")
                manage = input().lower()
                if manage == 'add':
                    print('\n')
                    manager.set_strategy(m.WatchedList())
                    manager.add_to_list(username)
                elif manage == 'remove':
                    print('\n')
                    manager.set_strategy(m.WatchedList())
                    manager.remove_from_list(username)
                elif manage =='back':
                    print('\n')
                    break 
                else:
                    print("Such a function doesn't exist.")
                    continue
        elif choice == '5':
            while True:
                print("\nWhat recomendation would you like to get? ")
                print("1. Discover surprise movies.")
                print("2. Find similar to one you've enjoyed.")
                print("3. Explore by genre.")
                print("4. Discover based on you watched movies.")
                print("5. Go back")
                choice = input("Choose an option: \n")
                if choice == '1':
                    print('\n')
                    movie_rec.random_movies()
                elif choice == '2':
                    print('\n')
                    movie_rec.similar_movie()
                elif choice == '3':
                    print('\n')
                    movie_rec.movie_genre()
                elif choice == '4':
                    movie_rec.from_watched(username)
                elif choice == '5':
                    break
                else:
                    print('\n')
                    print("Such a choice doesn't exist")
                    continue                    

        elif choice == '6':
            print("Exiting program")
            break
        else:
            print("Such a function doesn't exist.")

if __name__ == "__main__":

    if start():
        functions()
    else:
        exit()