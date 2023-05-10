import re

"""This function iterate until the user input can be converted to an int"""
def check_int() -> int:
    while True:
        try:
            option = int(input("Select and option from the menu: "))
            return option
        except ValueError:
            print("Invalid input. Try again")


"""
This function format the user name before store it in the database

Restriction:
The user name must be between 6 and 50 characters long 
"""
def check_user_name(message: str) -> str:
    user_input = input(
        f"\n• Must be between 6 and 50 characters long\n{message}"
    ).strip()
    while True:
        if 3 < len(user_input) < 50:
            return user_input.capitalize()
        print("Must be between six and 50 characters long")
        user_input = input(message).strip()


"""This function iterate until the user enter a valid email"""
def check_email() -> str:
    user_input = input("\n• your_name@example.com\nInsert your email: ").strip()
    while True:
        if bool(re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", user_input)):
            return user_input
        else:
            print("Invalid input. Try again")
            user_input = input("Insert your email: ").strip()


"""This function show all the currencies available and iterate until the user enter a valid option"""
def check_currency() -> str:
    currencies = {
        1: "United States Dollar",
        2: "Euro",
        3: "Japanese Yen",
        4: "British Pound",
        5: "Australian Dollar",
        6: "Canadian Dollar",
        7: "Swiss Franc",
        8: "Chinese Yuan",
        9: "Hong Kong Dollar",
        10: "Swedish Krona",
    }
    for index in range(1,11):
        print(index, currencies[index])
        
    while True:
        try:
            option = int(input("Enter the currency of your choice: "))
            if option in list(range(1,11)):
                return currencies[option]
            else:
                print("Option out of range")
        except ValueError:
            print("Invalid input. Try again")
