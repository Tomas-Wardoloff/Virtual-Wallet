import os
import check_input as ch
import database_actions as db

MENU_OPTIONS = {1: "Log In", 2: "Sign Up", 0: "Exit"}


def clear_shell():
    return os.system("cls" if os.name == "nt" else "clear")


def transaction_menu(connection, user_id: int):
    pass


def log_in_user(connection):
    clear_shell()
    # Check if there are any users in the database
    query = "SELECT COUNT(*) FROM Users;"
    if db.get_data(connection, query, ())[0][0] > 0:
        login_name = input("Enter username: ").strip().capitalize()
        password = input("Enter user password: ").strip()

        # Check if the username and password match a user in the database
        query = f"SELECT * FROM Users WHERE LoginName=? AND Password=? LIMIT 1;"
        params = (login_name, password)
        if db.get_data(connection, query, params) == []:
            print(f"Incorrect username or password")
        else:
            # Retrieve the user's ID
            query = f"SELECT UserId FROM Users WHERE LoginName=?;"
            user_id = db.get_data(connection, query, (login_name,))[0][0]

            # Check if the user has a wallet
            query = f"SELECT COUNT(*) FROM Wallets WHERE UserId=?;"
            if db.get_data(connection, query, (user_id,))[0][0] == 0:
                # If the user doesn't have a wallet, prompt for currency and create a wallet
                currency = ch.check_currency()
                query = f'INSERT INTO Wallets (Balance, Currency, UserId) VALUES (?, ?, ?);'
                params = (0.00, currency, user_id)
                db.run_query(connection, query, params)

            transaction_menu(connection, user_id)
    else:
        print("The table Users is empty")


def sign_up_user(connection):
    while True:
        clear_shell()
        login_name = ch.check_user_name("Enter your username: ")
        email = ch.check_email()
        password = ch.check_user_name("Enter your user password: ")

        # Check if user name or the email is already taken
        query = f"SELECT 1 FROM Users WHERE LoginName=? OR Email=? LIMIT 1;"
        result = db.get_data(connection, query, (login_name, email))

        if result:
            print(f"The username '{login_name}' or the email '{email}' is already in use. Please choose another one.")
        else:
            # Insert data of the new user in the database
            query = f"INSERT INTO Users (LoginName, Email, Password) VALUES (?, ?, ?);"
            db.run_query(connection, query, (login_name, email, password))
            break
    input("Registration successful. Press Enter to continue...")


def print_menu():
    print("+----------------+\n| Virtual Wallet |\n+----------------+")
    for option, text in MENU_OPTIONS.items():
        print(f"[{option}] {text}")


def main():
    connection = db.connect_database("Virtual-Wallet.db")
    while True:
        clear_shell()
        print_menu()
        option = ch.check_int()

        if option == 0:
            break
        elif option in MENU_OPTIONS:
            if option == 1:
                log_in_user(connection)
            elif option == 2:
                sign_up_user(connection)
        else:
            print("Invalid option")
        input("Press Enter to continue...")

    connection.close()


if __name__ == "__main__":
    main()
