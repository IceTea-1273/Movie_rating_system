import profileManaging
import movieLists as m


def start():
    global username
    running = True
    while running:
        print("\n1. Sign up")
        print("2. Log in")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            success, username = profileManaging.sign_up()
            if success:
                break
            else:
                continue
            
        elif choice == "2":
            success, username = profileManaging.log_in()
            if success:
                print(f"Welcome back, {username}!")
                break
            else:
                continue
               
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
    return username

def functions():
    running = True
    manager = m.ListManager(m.ToWatchList())
    while running:
        print("\nWhat would you like to do? ")
        print("1. Display to-watch list")
        print("2. Manage to-watch list")
        print("3. Display watched list")
        print("4. Manage watched list")
        print("5. Choose a movie to watch")
        print("6. Exit program")
        choice = input("Choose an option: ")

        if choice == '1':
            manager.set_strategy(m.ToWatchList())
            manager.display_list(username)
        elif choice == '2':
            managing = True
            while managing:
                print("\nAdd/remove, move to 'Watched', back.")
                manage = input().lower()
                if manage == 'add':
                    manager.set_strategy(m.ToWatchList())
                    manager.add_to_list(username)
                elif manage == 'remove':
                    manager.set_strategy(m.ToWatchList())
                    manager.remove_from_list(username)
                elif manage == 'move':
                    manager.set_strategy(m.ToWatchList())
                    manager.move_to_watched(username)
                elif manage =='back':
                    break 
                else:
                    print("Such a function doesn't exist")
                    continue
        elif choice == '3':
            manager.set_strategy(m.WatchedList())
            manager.display_list(username)
        elif choice == '4':
            managing = True
            while managing:
                print("\nAdd/remove from list, back.")
                manage = input().lower()
                if manage == 'add':
                    manager.set_strategy(m.WatchedList())
                    manager.add_to_list(username)
                elif manage == 'remove':
                    manager.set_strategy(m.WatchedList())
                    manager.remove_from_list(username)
                elif manage =='back':
                    break 
                else:
                    print("Such a function doesn't exist.")
                    continue
        elif choice == '5':
            print("watch next")
        elif choice == '6':
            print("exiting program")
            break
        else:
            print("Such a function doesn't exist.")



if __name__ == "__main__":
    start()
    print(f'Using program as {username}')
    functions()