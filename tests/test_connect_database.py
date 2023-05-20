import pytest
import sqlite3 as sql
from src.database_actions import connect_database


def test_connect_database_success():
    # Connect to a database in-memory
    database_name = ":memory:"
    connection = connect_database(database_name)

    # Test if the connection was successful
    assert isinstance(connection, sql.Connection)
    connection.close()
