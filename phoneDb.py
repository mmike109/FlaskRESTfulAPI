import sqlite3

# Connect to this database
DATABASE = "./phones_db.db"


# if connection is successful create phones table
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except "Error occurred while creating dbFile" as e:
        print(e)
        conn.close()
    finally:
        if conn:
            create_phones_table = conn.cursor()
            create_phones_table.execute("""CREATE TABLE IF NOT EXISTS phones (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                            phone_model TEXT NOT NULL,
                                            serial_number TEXT NOT NULL, color TEXT NOT NULL)""")

            conn.close()


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
    con = None
    try:
        con = sqlite3.connect(DATABASE)
        if con:
            delete_phones = con.cursor()
            delete_phones.execute("DELETE FROM phones WHERE id=" + id)
            con.commit()
            print("phone deleted")
            con.close()
    except "Error while deleting a phone" as eve:
        print(eve)
        con.close()
