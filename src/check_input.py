import re
import datetime


def check_number(data_type: str, message: str):
    """
    Prompt the user to enter a number of a specified data type and validate the input.

    Continuously prompts the user to enter a number until a valid format is provided.
    Validates the input based on the specified data type: 'int' or 'float'.
    Returns the validated number.

    Args:
        data_type (str): The data type to which the user input should be converted ('int' or 'float').
        message (str): The message to display when prompting the user for input.

    Returns:
        int or float: The validated number.

    Raises:
        ValueError: If the input cannot be converted to the specified data type.

    Examples:
        >>> check_number('int', 'Enter an integer: ')
        Enter an integer: 42
        42

        >>> check_number('float', 'Enter a float: ')
        Enter a float: 3.14
        3.14
    """
    try:
        if data_type == "int":
            option = int(input(message))
        elif data_type == "float":
            option = float(input(message))
        else:
            raise ValueError
        return option
    except ValueError:
        print(f"Invalid input. Please enter a valid {data_type}.")


def check_len_user_input(message: str) -> str:
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
    user_input = input(
        f"{message}\n• Must be between 6 and 50 characters long\n"
    ).strip()
    while True:
        if 3 < len(user_input) < 50:
            return user_input
        print("Must be between six and 50 characters long")
        user_input = input(message).strip()


def check_email() -> str:
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
    while True:
        user_input = input("\n• your_name@example.com\nInsert your email: ").strip()
        if bool(
            re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_input)
        ):
            return user_input
        else:
            print("Invalid input. Try again")


def check_currency() -> str:
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
        10: ["Swedish Krona", "SEK"],
    }
    for option, text in currencies.items():
        print(f"[{option}] {text[0]}")

    try:
        option = int(input("Enter the currency of your choice: "))
        if option in list(range(1, 11)):
            return currencies[option][1]
        raise ValueError
    except ValueError:
        print("Invalid input. Try again")


def check_date() -> str:
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
    
    date_str = input("Date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Invalid date format. Try again.")


def check_transaction_type() -> str:
    """
    Prompt the user to enter a transaction type and validate it.

    This function prompts the user to enter a transaction type ('income' or 'expense')
    and continuously validates the input until a valid transaction type is provided.
    The input is case-insensitive and will be capitalized.

    Returns:
        str: The validated transaction type, either 'Income' or 'Expense'.

    Raises:
        None

    Examples:
        >>> check_transaction_type()
        Enter transaction type (income or expense): expense
        'Expense'
    """
    
    transaction_type = input(
        "Enter transaction type (income or expense): "
    ).capitalize()
    if transaction_type in ["Income", "Expense"]:
        return transaction_type
    else:
        print("Invalid transaction type. Plese enter 'expense' or 'income'.")
