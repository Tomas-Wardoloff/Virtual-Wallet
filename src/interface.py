import os

import check_input as ch
import database_actions as db

MENU_OPTIONS = {1: "Log In", 2: "Sign Up", 0: "Exit"}
MENU_TRANSACTIONS = {
    1: "Enter Transaction",
    2: "Create Category",
    3: "Edit Transaction",
    4: "Show Transactions by category",
    5: "Show Transactions by date",
    6: "Show Categories",
    7: "Show Transactions",
    0: "Exit",
}


def clear_shell():
    return os.system("cls" if os.name == "nt" else "clear")


def edit_transaction(connection, user_id):
    transaction_query = """
                        SELECT t.TransactionId, t.Date, t.Amount, t.Description, t.Type, c.Name
                        FROM Transactions t
                        JOIN Categories c ON t.CategoryId = c.CategoryId
                        WHERE t.UserId = ? 
                        ORDER BY Date DESC;
                    """
    all_transactions = db.get_data(connection, transaction_query, (user_id,))
    print_transactions(all_transactions)
    transaction_id = ch.check_number("int", "Enter the transaction ID that you want to edit: ")
    if any(transaction[0] == transaction_id for transaction in all_transactions):
        # Remove the transaction from the balance
        transaction_to_edit_query = """
            SELECT Type, Amount
            FROM Transactions WHERE UserId = ? and TransactionId = ?
        """
        transaction_to_edit = db.get_data(connection, transaction_to_edit_query, (user_id, transaction_id))
        print(transaction_to_edit)
        if transaction_to_edit[0][0] == "Income":
            update_balance(connection, ["Expense", transaction_to_edit[0][1]], user_id)
        else:
            update_balance(connection, ["Income", transaction_to_edit[0][1]], user_id)
        
        # Update transaction
        params = enter_transaction(connection, user_id) + (transaction_id,)
        update_transaction_query = """
                UPDATE Transactions
                SET Date=?, Amount=?, Description=?, Type=?, CategoryId=?
                WHERE TransactionId=? AND UserId=?;
            """
        db.run_query(connection, update_transaction_query, params)
        # Update balance
        update_balance(connection, [params[3], params[1]], user_id)
    else:
        print("Invalid transaction id")
    

def print_transactions(transactions: list):
    print("| {:^10} | {:^10} | {:^10} | {:^20} | {:^10} | {:^20} |".format(
        "Transaction Id", "Date", "Amount", "Description", "Type", "Category"
    ))
    print("*" + "-" * 101 + "*")
    
    for transaction in transactions:
        transaction_id, date, amount, description, transaction_type, category_name = transaction
        print("| {:^14} | {:^10} | ${:^9} | {:^20} | {:^10} | {:^20} |".format(
            transaction_id, date, amount, description, transaction_type, category_name
        ))
        print("*" + "-" * 101 + "*")


def get_transactions_by_date(connection, user_id):
    clear_shell()
    selected_date = ch.check_date()
    query = """
        SELECT t.TransactionID, t.Date, t.Amount, t.Description, t.Type, c.Name
        FROM Transactions t
        JOIN Categories c ON t.CategoryId = c.CategoryId
        WHERE t.UserId = ? AND t.Date = ?
        ORDER BY Date DESC;
    """
    transactions_by_date = db.get_data(connection, query, (user_id, selected_date))
    
    if not transactions_by_date:
        print("The user has no transactions on that date")
    else:
        print_transactions(transactions_by_date)
    

def get_transactions_by_category(connection, user_id):
    category_id = select_category(connection, user_id)
    clear_shell()
    query = """
        SELECT t.TransactionId, t.Date, t.Amount, t.Description, t.Type, c.Name
        FROM Transactions t
        JOIN Categories c ON t.CategoryId = c.CategoryId
        WHERE t.UserId = ? AND t.CategoryId = ?
        ORDER BY Date DESC;
    """
    
    transactions_by_category = db.get_data(connection, query, (user_id, category_id))
    
    if not transactions_by_category:
        print("The user has no transactions of that category")
    else:
        print_transactions(transactions_by_category)
    

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
    categories = get_categories(connection, user_id)
    print("These are the available categories:")
    for category in categories:
        print(f"[{category[0]}]  {category[1]}")

    category_id = ch.check_number("int", "Enter the category ID: ")
    # Check if the category ID is valid
    if any(category[0] == category_id for category in categories):
        return category_id
    else:
        print("Category ID is not valid.")


def get_categories(connection, user_id):
    query = "SELECT CategoryId, Name FROM Categories WHERE UserId = ? OR UserId = 0;"
    return db.get_data(connection, query, (user_id, ))


def enter_transaction(connection, user_id: int) -> list:    
    date = ch.check_date()
    transaction_type = ch.check_transaction_type()    
    amount = ch.check_number("float", "Amount: ")
    description = ch.check_len_user_input(3, 50, "Enter Description: ")
    category_id = select_category(connection, user_id)

    return (date, amount, description, transaction_type, category_id, user_id)


def transaction_menu(connection, user_id: int):
    get_balance_query = "SELECT Balance FROM Wallets WHERE UserId=?;"
    while True:
        clear_shell()
        last_balance = db.get_data(connection, get_balance_query, (user_id,))[0][0]
        print(f"Actual balance: {last_balance}")

        print("+------------------+\n| Transaction Menu |\n+------------------+")
        print_menu(MENU_TRANSACTIONS)
        
        option = ch.check_number("int", "Select and option from the menu: ")

        if option in MENU_TRANSACTIONS:
            if option == 0:
                break
            if option == 1:
                query = "INSERT INTO Transactions (Date, Amount, Description, Type, CategoryId, UserId) VALUES (?, ?, ?, ?, ?, ?)"
                params = enter_transaction(connection, user_id)
                db.run_query(connection, query, params)
                update_balance(connection, [params[3], params[1]], user_id)
            elif option == 2:
                create_category(connection, user_id)
            elif option == 3:
                edit_transaction(connection, user_id)
            elif option == 4:
                get_transactions_by_category(connection, user_id)
            elif option == 5:
                get_transactions_by_date(connection, user_id)
            elif option == 6:
                clear_shell()
                categories = get_categories(connection, user_id)
                for category in categories:
                    print(f"[{category[0]}]  {category[1]}")
            elif option == 7:
                transaction_query = """
                    SELECT t.TransactionId, t.Date, t.Amount, t.Description, t.Type, c.Name
                    FROM Transactions t
                    JOIN Categories c ON t.CategoryId = c.CategoryId
                    WHERE t.UserId = ? 
                    ORDER BY Date DESC;
                """
                user_transactions = db.get_data(connection, transaction_query, (user_id,))
                print_transactions(user_transactions)
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
        hashed_password = ch.hash_password(password)
        
        # Check if the username and password match a user in the database
        query = f"SELECT * FROM Users WHERE LoginName=? AND Password=? LIMIT 1;"
        params = (login_name, hashed_password)
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
        login_name = ch.check_len_user_input(3, 50, "Enter your username: ")
        password = ch.check_len_user_input(3, 50, "Enter your user password: ")
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
            hashed_password = ch.hash_password(password)
            db.run_query(connection, query, (login_name, email, hashed_password))
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

        if option in MENU_OPTIONS:
            if option == 0:
                break
            elif option == 1:
                log_in_user(connection)
            elif option == 2:
                sign_up_user(connection)
        else:
            print("Invalid option")
        input("Press Enter to continue...")

    connection.close()


if __name__ == "__main__":
    main()
