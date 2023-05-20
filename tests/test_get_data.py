import pytest
import sqlite3 as sql
from src.database_actions import get_data

def test_get_data_success():
    # Create a test connection to an in-memory database
    connection = sql.connect(":memory:")
    cursor = connection.cursor()
    
    # Create a test table and add some data
    cursor.execute("CREATE TABLE TestTable (Id INTEGER PRIMARY KEY, Name TEXT)")
    cursor.execute("INSERT INTO TestTable (Id, Name) VALUES (1, 'John')")
    cursor.execute("INSERT INTO TestTable (Id, Name) VALUES (2, 'Mike')")
    
    # Query the data from the test table
    query = "SELECT * FROM TestTable"
    result = get_data(connection, query, ())
    
    # Ensure the returned data is as expected        
    assert result == [(1, "John"), (2, "Mike")]
    
    connection.close()
    
def test_get_data_error():
    # Create a test connection to an in-memory database
    connection = sql.connect(":memory:")
    
    # Query the data from a table does not exists
    query = "SELECT * FROM NonExistentTable"
    
    # Ensure it raise an error
    assert get_data(connection, query, ()) == None
    
    connection.close()
