import sql_manager
import sys
import getpass


class Client_Interface:
    @classmethod
    def start(cls):
        print("""Welcome to our bank service. You are not logged in.
        All available commands:
        register, login, list, help, exit

        Please, register or login""")

    @classmethod
    def registration(cls):
        username = input("Username: ")
        print("""Enter password with more than 8 symbols, capital and
lower letters,digits and special symbols""")
        password = getpass.getpass(stream=None)
        # password = input("Enter your password(above 8 symbols): ")
        sql_manager.register(username, password)
        print("Successful registration!")

    @classmethod
    def logged_menu(cls, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        print("""Available commands: info / change_pass / change_message
                    show_message / help""")
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'change_pass':
                new_pass = input("Enter your new password: ")
                sql_manager.change_pass(new_pass, logged_user)

            elif command == 'change_message':
                new_message = input("Enter your new message: ")
                sql_manager.change_message(new_message, logged_user)

            elif command == 'show_message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")

    @classmethod
    def login(cls):
        username = input("Username: ")
        password = getpass.getpass(stream=None)

        logged_user = sql_manager.login(username, password)

        if logged_user:
            cls.logged_menu(logged_user)
        else:
            print("Login failed")

        return username

    @classmethod
    def help(cls):
        print("""        login - for logging in!
        register - for creating new account!
        list - for all commands!
        exit - for closing program!""")

    @classmethod
    def list(cls):
        print("""        All available commands:
        register, login, list, help, exit""")

    @classmethod
    def exit():
        sys.exit("You are out from your bank account")
