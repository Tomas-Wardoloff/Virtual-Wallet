import os
import check_input as ch
import database_actions as db


def clear_shell():
    return os.system("cls" if os.name == "nt" else "clear")


def log_in_user(connection):
    clear_shell()
    query = "SELECT * FROM Users"
    if db.get_data(connection, query) != []:
        login_name = input("Enter username: ").strip()
        password = input("Enter user password: ").strip()

        query = f"SELECT * FROM Users WHERE LoginName='{login_name}' AND Password='{password}';"
        if db.get_data(connection, query) == []:
            print(f"The user with the name and the password entered is incorrect")
        else:
            print("Success, the user is in the system")
    else:
        print("The table Users is empty")
    os.system("pause")


def sign_up_user(connection):
    clear_shell()
    login_name = ch.check_user_name("Enter your username: ")
    email = ch.check_email()
    password = ch.check_user_name("Enter your user password: ")

    # Check if user name already exists
    query = f"SELECT * FROM Users WHERE LoginName='{login_name}' OR Email='{email}';"
    while db.get_data(connection, query) != []:
        print(
            f"The user name: {login_name} or the email: {email} is in use. Use another one"
        )
        login_name = ch.check_user_name("Enter your username: ")
        email = ch.check_email()
        password = ch.check_user_name("Enter your user password: ")

    query = f'INSERT INTO Users (LoginName, Email, Password) VALUES ("{login_name}", "{email}", "{password}");'
    db.run_query(connection, query)
    os.system("pause")


def main():
    connection = db.connect_database("Virtual-Wallet.db")
    clear_shell()
    print("+----------------+\n| Virtual Wallet |\n+----------------+")
    print("[1] Log In\n[2] Sign Up\n[0] Exit")
    option = ch.check_int()
    while option != 0:
        if option == 1:
            log_in_user(connection)
        elif option == 2:
            sign_up_user(connection)
        else:
            print("Invalid option")
            os.system("pause")

        clear_shell()
        print("+----------------+\n| Virtual Wallet |\n+----------------+")
        print("[1] Log In\n[2] Sign Up\n[0] Exit")
        option = ch.check_int()
    connection.close()


if __name__ == "__main__":
    main()
