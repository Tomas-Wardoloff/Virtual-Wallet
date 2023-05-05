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
    user_input = input(f"\n• Must be between 6 and 50 characters long\n{message}").strip()
    while True:
        if 3 < len(user_input) < 50:
            return user_input
        print("Must be between six and 50 characters long")
        user_input = input(message)


"""This function iterate until the user input a valid email"""
def check_email() -> str:
    user_input = input("\n• your_name@example.com\nInsert your email: ").strip()
    while True:
        if bool(re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", user_input)):
            return user_input
        else:
            print("Invalid input. Try again")
            user_input = input("Insert your email: ").strip()
