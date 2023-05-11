import sqlite3 as sql
from sqlite3 import Error

"""
Get a list of all the records that match a query
"""
def get_data(connection: sql.Connection, query: str, params: tuple) -> list:
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}")

"""
Run a sql query into the database

Keyword arguments:
connection -- object that connect to the database (sqlite3.Connection)
query -- the query that it is going to be executed (str)
"""
def run_query(connection: sql.Connection, query: str, params: tuple):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print(f"Query: '{query}' executed correctly with params: {params}")
    except Error as err:
        print(f"Error: '{err}'")


"""
Connect to an existing database, if it does not exist it is created 
on the foler 'dataBase' of the project

Keyword arguments:
database_name -- the name of database you want to connect (str)
"""
def connect_database(database_name: str) -> sql.Connection:
    connection = None
    try:
        connection = sql.connect(database_name,)
        print(f"Connection to {database_name} successsful")
        return connection
    except Error as err:
        print(f"Error: '{err}'")
