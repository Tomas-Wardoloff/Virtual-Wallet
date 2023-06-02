import os
import check_input as ch
import database_actions as db

MENU_OPTIONS = {1: "Log In", 2: "Sign Up", 0: "Exit"}
MENU_TRANSACTIONS = {
    1: "Enter Transaction",
    2: "Create Category",
    3: "Show Transactions by category",
    4: "Show Transactions by date",
    5: "Show Categories",
    6: "Show Transactions",
    0: "Exit",
}


def clear_shell():
    return os.system("cls" if os.name == "nt" else "clear")


def get_transactions_by_category(connection, user_id):
    category_id = select_category(connection, user_id)
    clear_shell()
    query = """
        SELECT t.Date, t.Amount, t.Description, t.Type, c.Name
        FROM Transactions t
        JOIN Categories c ON t.CategoryId = c.CategoryId
        WHERE t.UserId = ? AND t.CategoryId = ?
        ORDER BY Date DESC;
    """
    transactions_by_date = db.get_data(connection, query, (user_id, category_id))
    if transactions_by_date == []:
        print("There user has no transactions of that category")
    else:
        for transaction in transactions_by_date:
            date, amount, description, transaction_type, category_name = transaction
            print(
                "| {:^} | ${:^} | {:^} | {:^} | {:^}".format(
                    date, amount, description, transaction_type, category_name
                )
            )
    input("\nPress Enter to continue...")
    

def create_category(connection, user_id: int):
    clear_shell()
    all_categories = get_categories(connection, user_id)
    all_categories_names = [category[1] for category in all_categories]
    
    while True:
        category_name = input("Enter the category name: ").strip()
        
        if category_name in all_categories_names:
            print("The category already exists. Try with other name.")
        else:
            query = "INSERT INTO Categories (Name, UserId) VALUES (?, ?)"       
            db.run_query(connection, query, (category_name, user_id, ))
            break


def update_balance(connection, last_transaction, user_id):
    get_balance_query = "SELECT Balance FROM Wallets WHERE UserId=?;"
    last_balance = db.get_data(connection, get_balance_query, (user_id,))[0][0]
    if last_transaction[0] == "Income":
        last_balance += last_transaction[1]
    else:
        last_balance -= last_transaction[1]
    update_balance_query = "UPDATE Wallets SET Balance = ? WHERE UserId = ?"
    db.run_query(connection, update_balance_query, (last_balance, user_id))


def select_category(connection, user_id) -> int:
    clear_shell()
    categories = get_categories(connection, user_id)
    print("These are the available categories:")
    for category in categories:
        print(f"[{category[0]}]  {category[1]}")

    while True:
        category_id = ch.check_number("int", "Enter the category ID: ")
        while not category_id:
            category_id = ch.check_number("int", "Enter the category ID: ")
        # Check if the category ID is valid
        if any(category[0] == category_id for category in categories):
            return category_id
        else:
            print("Category ID is not valid. Try Again")


def print_transactions(connection, user_id: int):
    clear_shell()
    transaction_query = """
        SELECT t.Date, t.Amount, t.Description, t.Type, c.Name
        FROM Transactions t
        JOIN Categories c ON t.CategoryId = c.CategoryId
        WHERE t.UserId = ? 
        ORDER BY Date DESC;
    """
    user_transactions = db.get_data(connection, transaction_query, (user_id,))
    for transaction in user_transactions:
        date, amount, description, transaction_type, category_name = transaction
        print(
            "| {:^} | ${:^} | {:^} | {:^} | {:^}".format(
                date, amount, description, transaction_type, category_name
            )
        )


def get_categories(connection, user_id):
    query = "SELECT CategoryId, Name FROM Categories WHERE UserId = ? OR UserId = 0;"
    return db.get_data(connection, query, (user_id, ))


def enter_transaction(connection, user_id: int) -> list:
    clear_shell()
    
    date = ch.check_date()
    while not date:
        date = ch.check_date()

    transaction_type = ch.check_transaction_type()    
    while not transaction_type:    
        transaction_type = ch.check_transaction_type()
    
    amount = ch.check_number("float", "Amount: ")
    while not amount:
        amount = ch.check_number("float", "Amount: ")
    
    description = ch.check_len_user_input("Enter Description: ")
    while not description:
        description = ch.check_len_user_input("Enter Description: ")
    
    category_id = select_category(connection, user_id)

    query = "INSERT INTO Transactions (Date, Amount, Description, UserId, CategoryId, Type) VALUES (?, ?, ?, ?, ?, ?)"
    params = (date, amount, description, user_id, category_id, transaction_type)
    db.run_query(connection, query, params)
    return [transaction_type, amount]


def transaction_menu(connection, user_id: int):
    get_balance_query = "SELECT Balance FROM Wallets WHERE UserId=?;"
    while True:
        clear_shell()
        last_balance = db.get_data(connection, get_balance_query, (user_id,))[0][0]
        print(f"Actual balance: {last_balance}")

        print("+------------------+\n| Transaction Menu |\n+------------------+")
        print_menu(MENU_TRANSACTIONS)
        
        option = ch.check_number("int", "Select and option from the menu: ")
        while not option:
            option = ch.check_number("int", "Select and option from the menu: ")

        if option == 0:
            break
        elif option in MENU_TRANSACTIONS:
            if option == 1:
                last_transaction = enter_transaction(connection, user_id)
                update_balance(connection, last_transaction, user_id)
            elif option == 2:
                create_category(connection, user_id)
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                clear_shell()
                categories = get_categories(connection, user_id)
                for category in categories:
                    print(f"[{category[0]}]  {category[1]}")
            elif option == 6:
                print_transactions(connection, user_id)
        else:
            print("Invalid option")
        input("\nPress Enter to continue...")


def log_in_user(connection):
    clear_shell()
    # Check if there are any users in the database
    query = "SELECT COUNT(*) FROM Users;"
    if db.get_data(connection, query, ())[0][0] > 0:
        login_name = input("Enter username: ").strip()
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
                clear_shell()

                currency = ch.check_currency()
                while not currency:
                    currency = ch.check_currency()                    

                query = (
                    f"INSERT INTO Wallets (Balance, Currency, UserId) VALUES (?, ?, ?);"
                )
                params = (float(0), currency, user_id)
                db.run_query(connection, query, params)

            transaction_menu(connection, user_id)
    else:
        print("The table Users is empty")


def sign_up_user(connection):
    while True:
        clear_shell()
        
        login_name = ch.check_len_user_input("Enter your username: ")
        password = ch.check_len_user_input("Enter your user password: ")
        while not login_name and password:
            login_name = ch.check_len_user_input("Enter your username: ")
            password = ch.check_len_user_input("Enter your user password: ")

        email = ch.check_email()        
        while not email:
            email = ch.check_email()

        # Check if user name or the email is already taken
        query = f"SELECT 1 FROM Users WHERE LoginName=? OR Email=? LIMIT 1;"
        result = db.get_data(connection, query, (login_name, email))

        if result:
            print(
                f"The username '{login_name}' or the email '{email}' is already in use. Please choose another one."
            )
        else:
            # Insert data of the new user in the database
            query = f"INSERT INTO Users (LoginName, Email, Password) VALUES (?, ?, ?);"
            db.run_query(connection, query, (login_name, email, password))
            break


def print_menu(menu: dict):
    for option, text in menu.items():
        print(f"[{option}] {text}")


def main():
    connection = db.connect_database("Virtual-Wallet.db")
    while True:
        clear_shell()
        print("+----------------+\n| Virtual Wallet |\n+----------------+")
        print_menu(MENU_OPTIONS)
        
        option = ch.check_number("int", "Select and option from the menu: ")
        while not option:
            option = ch.check_number("int", "Select and option from the menu: ")
            
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
