import profileManaging


def sign_up():
    print('Signing up')
    create_profile = profileManaging.CreateUserProfile()
    succes = create_profile.creating_user()
    return succes

def log_in():
    print('Logging in')
    profileManaging.user_login()


def start():
    running = True
    while running:
        print("\n1. Sign up")
        print("2. Log in")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            if sign_up():
                break
            else:
                continue
            
        elif choice == "2":
            log_in()
            break
        
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start()
    print('Welcome!')