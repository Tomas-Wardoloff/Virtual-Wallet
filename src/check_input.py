import datetime
import hashlib
import re


def check_number(data_type: str, message: str = "") -> int | float:
    """
    Prompt the user to enter a number of a specified data type and validate the input.

    Continuously prompts the user to enter a number until a valid format is provided.
    Validates the input based on the specified data type: 'int' or 'float'.
    Returns the validated number.

    Args:
        data_type (str): The data type to which the input should be converted ('int' or 'float').
        message (str): The message to display when prompting the user for input.

    Returns:
        int or float: The validated number.
        None: In case the input cannot be converted.

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
    while True:
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


def check_len_user_input(min_length: int, max_length: int, message: str = "") -> str:
    """
    Prompt the user to enter a username within a specific length range.

    This function prompts the user to enter a string and validates the input
    Validates the input based on the specified minimum and maximum lengths.
    Returns the validated username.

    Args:
        min_length (int): The minimum allowed length of the input string.
        max_length (int): The maximum allowed length of the input string.
        message (str, optional): The message to display when prompting the user for input.

    Returns:
        str: The validated string, if the length is withing the specific range.
        None: If the input length is not within the specified range.

    Raises: None

    Examples:
        >>> check_user_name("Enter your desired username: ")
        • Must be between 6 and 50 characters long
        Enter your desired username: myusername
        'myusername'
    """
    print(f"{message}\n• Must be between {min_length} and {max_length} characters long")
    while True:
        user_input = input().strip()
        if len(user_input) not in list(range(min_length, max_length + 1)):
            print("Input is too short or too long.", end="")
        return user_input


def check_email() -> str:
    """
    Prompt the user to enter an email address and validate its format.

    This function prompts the user to enter an email address until a valid format is provided.
    Uses a regular expression pattern to validate the email format.
    Returns the validated email address.

    Returns:
        str: The validated email address, if it match the pattern.
        None: If the input format is not correct.

    Raises: None

    Examples:
        >>> check_email()
        • your_name@example.com
        Insert your email: example@example.com
        'example@example.com'
    """
    print("\n• your_name@example.com\nInsert your email: ", end="")
    while True:
        user_input = input().strip()
        if bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_input)):
            return user_input
        print("Invalid input. Try again")


def check_currency() -> str:
    """
    Prompt the user to select a currency from a predefined list.

    Displays a menu of currencies and prompts the user to enter their choice.
    Validates the input to ensure it corresponds to a valid currency option.
    Returns the currency code associated with the selected option.

    Returns:
        str: The currency code selected by the user.
        None: If the input not corresponds to a valid currency option.
        
    Raises: 
        ValueError: If the input not corresponds to a valid currency option.

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

    while True:
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

    This function prompts the user to enter a date a valid date in the format 'YYYY-MM-DD'.
    Uses the datetime module to validates the date format.
    Returns the formated date.

    Returns:
        str: The valid date string in 'YYYY-MM-DD' format.
        None: If the entered date is not in the correct format.

    Raises:
        ValueError: If the entered date is not in the correct format.

    Examples:
        >>> check_date()
        Date (YYYY-MM-DD): 2023-05-13
        '2023-05-13'
    """
    date_str = input("Date (YYYY-MM-DD): ")
    while True:
        try:
            if datetime.datetime.strptime(date_str, "%Y-%m-%d"):
                return date_str
            raise ValueError
        except ValueError:
            print("Invalid date format. Try again.")


def check_transaction_type() -> str:
    """
    Prompt the user to enter a transaction type and validate it.

    This function prompts the user to enter a transaction type ('income' or 'expense')
    Validates the input is a valid transaction type.
    The input is case-insensitive and then capitalize.
    Returns a valid transaction type.

    Returns:
        str: The validated transaction type, either 'Income' or 'Expense'.
        None: If the transactions type is not "Income" or "Expense".

    Raises: None

    Examples:
        >>> check_transaction_type()
        Enter transaction type (income or expense): expense
        'Expense'
    """
    while True:
        transaction_type = input("Enter transaction type (income or expense): ").capitalize()
        if transaction_type in ["Income", "Expense"]:
            return transaction_type
        print("Invalid transaction type. Plese enter 'expense' or 'income'.")


def hash_password(user_password: str) -> str:
    """
    Hash the user password using the SHA256 algorithm.

    This function takes a user password and computes its SHA256 hash. The password
    is first encoded into UTF-8 format before being hashed. The resulting hash is returned
    as a hexadecimal string.

    Args:
    user_password (str): The password to be hashed.

    Returns:
    str: The SHA256 hash of the user password.

    Raises:
    None

    Examples:
    >>> hash_user_password('myPassword123')
    '3a4e19f12de49f3dbd68cbfd6f0b15da3d789797d24018b3a44a36e7f8a38c18'
    >>> hash_user_password('password')
    '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'
    """
    password_bytes = user_password.encode("utf-8")
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password_bytes)
    return sha256_hash.hexdigest()
