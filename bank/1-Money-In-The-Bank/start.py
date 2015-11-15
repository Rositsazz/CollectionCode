import sql_manager
from Client_interface import Client_Interface


def main_menu():
    Client_Interface.start()

    while True:
        command = input("$$$>")

        if command == 'register':
            Client_Interface.registration()

        elif command == 'login':
            Client_Interface.login()

        elif command == 'help':
            Client_Interface.help()

        elif command == 'exit':
            Client_Interface.exit()

        elif command == 'list':
            Client_Interface.list()

        else:
            print("Not a valid command")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
