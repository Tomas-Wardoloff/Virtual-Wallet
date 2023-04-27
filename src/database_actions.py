import sqlite3 as sql
from sqlite3 import Error

"""
Run a sql query into the database

Keyword arguments:
connection -- object that connect to the database (sqlite3.Connection)
query -- the query that it is going to be executed (str)
"""
def run_query(connection: sql.Connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Query: '{query}' executed correctly")
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
