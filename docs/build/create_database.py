import sys

sys.path.append("src")
import database_actions as db

"""
This file is use to create the database of the project
and show the structure and how the tables were made
"""
if __name__ == "__main__":
    connection = db.connect_database("Virtual-Wallet.db")

    users_table = """
    CREATE TABLE Users(
        UserId INTEGER PRIMARY KEY AUTOINCREMENT,
        LoginName VARCHAR(50),
        Email VARCHAR(50),
        Password VARCHAR(256)
        );
    """

    categories_table = """
    CREATE TABLE Categories(
        CategoryId INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(50),
        UserId int,
        FOREIGN KEY(UserId) REFERENCES Users(UserId)
        );
    """

    transactions_table = """
    CREATE TABLE Transactions(
        TransactionId INTEGER PRIMARY KEY AUTOINCREMENT,
        Date DATE,
        Amount DECIMAL(9,2),
        Description VARCHAR(250),
        Type VARCHAR(7),
        UserId INT,
        CategoryId INT,
        FOREIGN KEY(UserId) REFERENCES Users(UserId),
        FOREIGN KEY(CategoryId) REFERENCES Categories(CategoryId)
        );
    """

    wallets_table = """
    CREATE TABLE Wallets(
        WalletId INTEGER PRIMARY KEY AUTOINCREMENT,
        Balance DECIMAL(9, 2),
        Currency VARCHAR(16),
        UserId INT,
        FOREIGN KEY(UserId) REFERENCES Users(UserId)
        );"""

    create_main_categories = """
    INSERT INTO Categories (Name, UserId)
    VALUES
        ('Groceries', 0),
        ('Utilities', 0),
        ('Transportation', 0),
        ('Housing', 0),
        ('Eating Out', 0),
        ('Entertainment', 0),
        ('Clothing', 0),
        ('Healthcare', 0),
        ('Education', 0),
        ('Miscellaneous', 0)
    ;
    """

    queries = [
        users_table,
        categories_table,
        transactions_table,
        wallets_table,
        create_main_categories,
    ]
    for query in queries:
        db.run_query(connection, query, ())
    connection.close()
