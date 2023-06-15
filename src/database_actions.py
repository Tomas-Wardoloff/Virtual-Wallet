import sqlite3 as sql
from sqlite3 import Error


def get_data(connection: sql.Connection, query: str, params: tuple) -> list | None:
    """
    Retrieve data from a database using the provided query and parameters.

    This function executes the specified SQL query with the given parameters.
    It retrieves all the resulting rows from the executed query and returns them as a list.

    Args:
        connection (sql.Connection): The database connection object.
        query (str): The SQL query to execute.
        params (tuple): The parameters to pass to the query.

    Returns:
        list: A list of rows retrieved from the database.
        None: If an error occurs while executing the query.

    Raises:
        Error: If an error occurs while executing the query.

    Examples:
        >>> connection = sql.connect('database.db')
        >>> query = "SELECT * FROM Users WHERE Age > ?"
        >>> params = (25,)
        >>> get_data(connection, query, params)
        [(1, 'John', 28), (2, 'Jane', 30), ...]
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}")
        return None


def run_query(connection: sql.Connection, query: str, params: tuple):
    """
    Execute a SQL query on the provided database connection.

    This function executes the specified SQL query with the given parameters
    It commits the changes to the database if the query execution is successful.

    Args:
        connection (sql.Connection): The database connection object.
        query (str): The SQL query to execute.
        params (tuple): The parameters to pass to the query.

    Returns:
        None

    Raises:
        Error: If an error occurs while executing the query.

    Examples:
        >>> connection = sql.connect('database.db')
        >>> query = "INSERT INTO Users (Name, Age) VALUES (?, ?)"
        >>> params = ('John', 28)
        >>> run_query(connection, query, params)
        'INSERT INTO Users (Name, Age) VALUES (?, ?)' executed correctly with params: ('John', 28)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print(f"Query: '{query}' executed correctly with params: {params}")
    except Error as err:
        print(f"Error: '{err}'")


def connect_database(database_name: str) -> sql.Connection | None:
    """
    Connect to a SQLite database and return the database connection object.

    This function create a connection to the specified SQLite database. 
    It use the provided database name, in case the database does not exist it is created.
    It returns the connection object if the connection is successful.

    Args:
        database_name (str): The name of the SQLite database file.

    Returns:
        sql.Connection: The connection object representing the database connection.
        None: If an error occurs while connecting to the database.

    Raises:
        Error: If an error occurs while connecting to the database.

    Examples:
        >>> connection = connect_database('database.db')
        Connection to database.db successful
        <sqlite3.Connection object at 0x...>
    """
    connection = None
    try:
        connection = sql.connect(
            database_name,
        )
        print(f"Connection to {database_name} successsful")
        return connection
    except Error as err:
        print(f"Error: '{err}'")
        return None
