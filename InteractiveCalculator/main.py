from greet import greet_user
from exit import exit_application
from menu import display_menu

def main():
    user_name = input('Please enter your name: ')
    greet_user(user_name)

    while True:
        display_menu()
        choice = input('Select an option (1 or 2): ')

        if choice == '1':
            greet_user(user_name)
        elif choice == '2':
            exit_application()
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()