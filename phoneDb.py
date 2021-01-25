import sqlite3

# Connect to this database
DATABASE = "./phones_db.db"


def db_connection_cursor():
    db_conn = None
    try:
        db_conn = sqlite3.connect(DATABASE)
    except "ERROR while connecting to database" as err:
        print(err)
        db_conn.close()
    finally:
        if db_conn:
            db_connect = db_conn.cursor()
            return db_connect


def db_connection():
    connection = None
    try:
        connection = sqlite3.connect(DATABASE)
    except "Error connecting to db" as e:
        print(e)
        connection.close()
    finally:
        if connection:
            return connection


# if connection is successful create phones table
def create_connection():
    try:
        db_connection_cursor()
    except "Error occurred while creating dbFile" as e:
        print(e)
        db_connection_cursor().close()
    finally:
        if db_connection_cursor():
            db_connection_cursor().execute("""CREATE TABLE IF NOT EXISTS phones (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                            phone_model TEXT NOT NULL,
                                            serial_number TEXT NOT NULL, color TEXT NOT NULL)""")

            db_connection_cursor().close()


# Inserts new phone into phone store database when new POST request is initiated
def insert_new_phone(phone_model, serial_number, color):
    parms = (phone_model, serial_number, color)
    connection = None
    try:
        connection = sqlite3.connect(DATABASE)
        if connection:
            insert_phone = connection.cursor()
            insert_phone.execute("INSERT INTO phones (phone_model, serial_number, color) VALUES (?, ?, ?)", parms)
            connection.commit()
            print("Insert successful")
            connection.close()
    except "Error occurred while inserting a new phone" as ev:
        print(ev)
        connection.close()


# Delete a phone from database
def delete_phone(id):
    try:
        db_connection_cursor()
        if db_connection_cursor():
            db_connection_cursor().execute("DELETE FROM phones WHERE id=" + id)
            db_connection_cursor().commit()
            print("phone deleted")
            db_connection_cursor().close()
    except "Error while deleting a phone" as eve:
        print(eve)
        db_connection_cursor().close()
