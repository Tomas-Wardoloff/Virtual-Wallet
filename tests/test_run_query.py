import pytest
import sqlite3 as sql
from src.database_actions import run_query

def test_run_query_success():
    # Create a test connection to an in-memory database
    connection = sql.connect(":memory:")
    cursor = connection.cursor()
    
    # Create a test table
    create_table_query = "CREATE TABLE Test (id INTEGER PRIMARY KEY, name TEXT)"
    run_query(connection, create_table_query, ()) 
    
    # Query the table name from the database
    assert "Test" in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()[0]
    
    # Add some data to the table
    insert_data_query = "INSERT INTO Test (id, name) VALUES (?, ?)"
    run_query(connection, insert_data_query, (1, "Mike"))
    
    # Ensure the returned data is as expected 
    result = cursor.execute("SELECT * FROM Test").fetchall()
    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "Mike"
        
    connection.close()
    
def test_run_query_error():
    # Create a test connection to an in-memory database
    connection = sql.connect(":memory:")
    cursor = connection.cursor()
    
    # Insert data to a table does not exists
    query = "INSERT INTO Test (id, name) VALUES (?, ?)"
    
    # Ensure it raise an error
    assert run_query(connection, query, ())  is None
    
    connection.close()