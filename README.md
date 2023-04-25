# Virtual Wallet
This is a personal project where I design a virtual wallet to track personal expenses and incomes. The main idea is to spend my time on something more important rather than playing League of Legends and learn during the process. 
I am going to use Python 3.11 to build the application, Git and GitHub to keep track of the code, [sqlite3](https://docs.python.org/3/library/sqlite3.html) to create and manage the database, [pytest](https://docs.pytest.org/en/7.3.x/contents.html) to test the functions of the code, [coverage.py](https://coverage.readthedocs.io/en/7.2.3/#) to see how much of the code is being tested, [virtualenv](https://docs.python.org/3/library/venv.html) just to be more pythonic and keep a track of the packages that I am going to use and also Chatgpt to ask different business rules, functionalities and issues that came out during the process (which I am not sure to add or not).

## Table of contents
- [Description of the project]()
- [Tech Stack]()
- [Authors]()

## Description of the project
I am using Python to create this virtual wallet that allows users to enter their incomes and expenses and keep a track of their finances using the features described below.

1. **Account registration**:  

   The application allows the user to create a wallet account and register their personal details such as name, email address, and password .

2. **Transaction logging**:

   The application keeps a record of all transactions made, whether it is an income or expense. It tracks every financial operation that involves the movement of money. All the transactions include sensitive information such as the date, the amount of money involved, the category, and a short description that is going to be provided by the user.

- **Categories**

  The application provided you with a list of different categories to use for the transactions but the user also can create their categories.

3. **Transaction analysis**:

   The application shows the user an analysis of their transactions to have a better understanding of their spending and saving habits. The application offer charts and statistics to help the user see how their money is being spent.

## Database
I am going to use the sqlite3 library to create and manage a database locally that stores all the data from the user. To start, The database has a table called user that stores the following information for each user:
```SQL
CREATE TABLE IF NOT EXISTS vwallet.users(
        UserId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        LoginName VARCHAR(50) NOT NULL,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        Email VARCHAR(50) NOT NULL,
        Password VARCHAR(50) NOT NULL
    );
```
The general idea, so far, is to create a database with the personal information of each ussser and have different wallets related to each user, with their own transactions, expenses, and incomes.

## Authors
- [@Tomas-Wardoloff](https://www.github.com/Tomas-Wardoloff)
