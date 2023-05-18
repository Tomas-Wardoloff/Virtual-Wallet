# Virtual Wallet
![GitHub last commit](https://img.shields.io/github/last-commit/Tomas-Wardoloff/Virtual-Wallet?style=plastic)
![GitHub](https://img.shields.io/github/license/Tomas-Wardoloff/Virtual-Wallet?color=informational&style=plastic)

This is a personal project where I design a virtual wallet to track personal expenses and incomes. The main idea is to spend my time on something more important rather than playing League of Legends and learn during the process. 
I am going to use Python 3.11 to build the application, Git and GitHub to keep track of the code, [sqlite3](https://docs.python.org/3/library/sqlite3.html) to create and manage the database, [pytest](https://docs.pytest.org/en/7.3.x/contents.html) to test the functions of the code, [coverage.py](https://coverage.readthedocs.io/en/7.2.3/#) to see how much of the code is being tested, [virtualenv](https://docs.python.org/3/library/venv.html) just to be more pythonic and keep a track of the packages that I am going to use and also Chatgpt to ask different business rules, functionalities and issues that came out during the process (which I am not sure to add or not).

## Table of contents
- [Description of the project](#description-of-the-project)
- [Database](#database)
- [Authors](#authors)

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

From the beginning, I knew I was going to work with a database and what data I wanted to store, but I did not know how to struct the database. So I asked Chat-GTP.
After chatting and seeing different databases that Chat-GTP provided me, I modified one of those ideas and came out with this:
The database has four main tables: Users, Transactions, Categories and Wallets.

- **Users**
  The Users table will store information about each user, such as their login name, email and password. Each user will have a unique identifier, which will serve as the primary key for this table

- **Categories**
  This table only stores the information of the different categories that the users can use to identify their transactions, and like the user's table, it has a unique identifier. The users can create their own categories, which is why this table has a foreign key that references the Users table. The categories with UserId = 0 are accessible to all the users.
  
- **Transactions**
  This table store information about each transaction made by the users. This table will have two foreign keys, one references the User table so each transaction will be associated with a particular user, and the other one references the Categories table.

- **Wallets**
  This table store a "summit" of the user's wallet. This one has a foreign key that references the User table and also stores information such as currency, balance and an identifier.

<p align="center">
   <img src="https://raw.githubusercontent.com/Tomas-Wardoloff/Virtual-Wallet/main/Database%20Diagram.png" alt="Database Diagram" width="600" height="400"/>
</p>

## Authors
- [@Tomas-Wardoloff](https://www.github.com/Tomas-Wardoloff)
