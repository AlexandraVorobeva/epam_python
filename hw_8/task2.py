import sqlite3
from typing import Callable


def connect_database(func: Callable) -> Callable:
    """This decorator connects to an existing database
    and opens a cursor to perform database operations.
    """

    def wrapper(self, *args, **kwargs):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            return func(self, cursor, *args, **kwargs)

    return wrapper


class TableData:
    """Class initializes with database name and table,
    then gives current amount of rows in database,
    then return single data row for single name,
    then return if row with same name exists in table,
    than implements iteration protocol.
    """

    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    @connect_database
    def __len__(self, cursor) -> int:
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return cursor.fetchone()[0]

    @connect_database
    def __getitem__(self, cursor, item: str) -> tuple:
        cursor.execute(f"SELECT * from  {self.table_name} WHERE name ='{item}'")
        return cursor.fetchone()

    @connect_database
    def __contains__(self, cursor, item: str) -> bool:
        cursor.execute(f"SELECT * from {self.table_name} WHERE name ='{item}'")
        return cursor.fetchone()

    @connect_database
    def __iter__(self, cursor) -> tuple:
        cursor.execute(f"SELECT * from {self.table_name}")
        return cursor
