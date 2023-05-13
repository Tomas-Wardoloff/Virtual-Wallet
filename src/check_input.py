import re
import datetime

"""
    Prompt the user to enter an integer and validate its format.

    Continuously prompts the user to enter an integer until a valid format is provided.
    Uses a try-except block to catch the ValueError raised if the input cannot be converted to an integer.
    Returns the validated integer.

    Returns:
        int: The validated integer.

    Examples:
        >>> check_int()
        Select an option from the menu: 3
        3
"""
def check_int() -> int:
    while True:
        try:
            option = int(input("Select and option from the menu: "))
            return option
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


"""
    Prompt the user to enter a username within a specific length range.

    Displays a custom message to guide the user regarding the username requirements.
    Continuously prompts the user to enter a username until a valid length is provided.
    Returns the validated username.

    Args:
        message (str): The custom message to display before prompting for the username.

    Returns:
        str: The validated username.

    Examples:
        >>> check_user_name("Enter your desired username: ")
        • Must be between 6 and 50 characters long
        Enter your desired username: myusername
        'myusername'
"""
def check_user_name(message: str) -> str:
    user_input = input(
        f"\n• Must be between 6 and 50 characters long\n{message}"
    ).strip()
    while True:
        if 3 < len(user_input) < 50:
            return user_input
        print("Must be between six and 50 characters long")
        user_input = input(message).strip()


"""
    Prompt the user to enter an email address and validate its format.

    Continuously prompts the user to enter an email address until a valid format is provided.
    Uses a regular expression pattern to validate the email format.
    Returns the validated email address.

    Returns:
        str: The validated email address.

    Examples:
        >>> check_email()
        • your_name@example.com
        Insert your email: example@example.com
        'example@example.com'
"""
def check_email() -> str:
    while True:
        user_input = input("\n• your_name@example.com\nInsert your email: ").strip()
        if bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_input)):
            return user_input
        else:
            print("Invalid input. Try again")


"""
    Prompt the user to select a currency from a predefined list.

    Displays a menu of currencies and prompts the user to enter their choice.
    Validates the input to ensure it corresponds to a valid currency option.
    Returns the currency code associated with the selected option.

    Returns:
        str: The currency code selected by the user.

    Examples:
        >>> check_currency()
        [1] US Dollar
        [2] Euro
        ...
        Enter the currency of your choice: 2
        'EUR'
"""
def check_currency() -> str:
    currencies = {
        1: ["US Dollar", "USD"],
        2: ["Euro", "EUR"],
        3: ["Japanase Yen", "JPY"],
        4: ["British Pound", "GBP"],
        5: ["Australian Dollar", "AUD"],
        6: ["Canadian Dollar", "CAD"],
        7: ["Swiss Franc", "CHF"],
        8: ["Chinese Yuan", "CNY"],
        9: ["Hong Kong Dollar", "HKD"],
        10: ["Swedish Krona", "SEK"]
    }
    for option, text in currencies.items():
        print(f"[{option}] {text[0]}")
        
    while True:
        try:
            option = int(input("Enter the currency of your choice: "))
            if option in list(range(1,11)):
                return currencies[option][1]
            else:
                print("Option out of range")
        except ValueError:
            print("Invalid input. Try again")
            
"""
    Prompt the user for a date and validate that it is in the format 'YYYY-MM-DD'.

    This function continuously prompts the user to enter a date until a valid date in the format 'YYYY-MM-DD' is provided.
    The entered date is then converted to a datetime object to ensure its validity.

    Returns:
        str: The valid date string in 'YYYY-MM-DD' format.

    Raises:
        ValueError: If the entered date is not in the correct format.

    Examples:
        >>> check_date()
        Date (YYYY-MM-DD): 2023-05-13
        '2023-05-13'
"""
def check_date() -> str:
    while True:
        date_str = input("Date (YYYY-MM-DD): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Try again.")
