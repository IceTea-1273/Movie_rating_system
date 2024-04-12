import profileManaging


def start():
    running = True
    while running:
        print("\n1. Sign up")
        print("2. Log in")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            if profileManaging.sign_up():
                break
            else:
                continue
            
        elif choice == "2":
            if profileManaging.log_in():
                break
            else:
                continue
            
            
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start()
    print('Welcome!')