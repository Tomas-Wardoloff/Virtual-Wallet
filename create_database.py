import src.database_actions as db

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
        Password VARCHAR(50)
        );
    """

    categories_table = """
    CREATE TABLE Categories(
        CategoryId INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(50)
        );
    """

    transactions_table = """
    CREATE TABLE Transactions(
        TransactionId INTEGER PRIMARY KEY AUTOINCREMENT,
        Date DATE,
        Amount DECIMAL(9,2),
        Description VARCHAR(250),
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

    queries = [users_table, categories_table, transactions_table, wallets_table]
    for query in queries:
        db.run_query(connection, query)
    connection.close()
