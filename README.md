# Virtual Wallet

This is a personal project where I am going to design a virtual wallet to track personal expenses and incomes

## table of contents

- [Description of the project]()
- [Tech Stack]()
- [Authors]()

## Description of the project

I am using Python to create this virtual wallet that allows users to enter their incomes and expenses and keep a track of their personal finances using the features described bellow.

1. **Account registration**:  
   The aplication allow the user to create a wallet account and register their personal details such as name, email addres and password 

2. **Transaction logging**:
   The application keeps a record of all transactions made, whether it is an income or an expense. It tracks every financial operation that involves a movement of money. All the transactions include sensitive information such as the date, the amount of money involved, the category and short description that it going to be provided by the user.

- **Categories**
  The application provided you with a list with different categories to use for the transactions but the user also have the possibility to create their own category

3. **Transcation analysis**:
   The apliaction show the user an analysis of their transactions to have a better understanding of their spending and saving habits. The application offer charts ands statistics to help the user see how thir money is being spent

## Database
I am going to the sqlite3 library to create and managment a database localy that store all the data from the user. The database have table called user that store the following information for each user:
```sql
CREATE TABLE IF NOT EXISTS vwallet.users(
        UserId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        LoginName VARCHAR(50) NOT NULL,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        Email VARCHAR(50) NOT NULL,
        Password VARCHAR(50) NOT NULL
    );
```

## Tech Stack

Describe all the tools that are use to create the project

## Authors

- [@Tomas-Wardoloff](https://www.github.com/Tomas-Wardoloff)
