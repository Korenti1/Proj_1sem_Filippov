import sqlite3
from tables import booking, tours, tourists
from data import tourists_data, tours_data, booking_data
from select import selects
from update import updates
from delete import deletes


def get_cursor():
    with sqlite3.connect('pz15.db') as con:
        return con.cursor()


def execute_sql(sql):
    cursor = get_cursor()
    return cursor.executescript(sql).fetchall()


def create_tables(table):
    execute_sql(table)


def insert_data(data):
    execute_sql(data)


def main():
    for table in [booking, tours, tourists]:
        create_tables(table)

    for i in [tourists_data, tours_data, booking_data]:
        insert_data(i)

    for select in selects:
        cursor = get_cursor()
        print(cursor.executescript(select).fetchall())
    for update in updates:
        cursor = get_cursor()
        print(cursor.executescript(update).fetchall())
    for delete in deletes:
        cursor = get_cursor()
        cursor.executescript(delete)


if __name__ == "__main__":
    main()
