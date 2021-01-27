import sqlite3

# Connect to this database
DATABASE = "./phones_db.db"
CONNECTION = None


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
    try:
        CONNECTION = sqlite3.connect(DATABASE)
        if CONNECTION:
            insert_phone = CONNECTION.cursor()
            insert_phone.execute("INSERT INTO phones (phone_model, serial_number, color) VALUES (?, ?, ?)", parms)
            CONNECTION.commit()
            print("Insert successful")
            CONNECTION.close()
    except "Error occurred while inserting a new phone" as ev:
        print(ev)
        CONNECTION.close()


# Updates a phone
def update_phone(phone_model, serial_number, color, id):
    update_parms = (phone_model, serial_number, color, id)
    try:
        CONNECTION = sqlite3.connect(DATABASE)
        if CONNECTION:
            update_phones = CONNECTION.cursor()
            update_phones.execute("""UPDATE phones SET phone_model=?, serial_number=?, color=?
            WHERE id=?""", update_parms)
            print(update_parms)
            CONNECTION.commit()

    except "Error occured while updating phone #" + id as error:
        print(error)
        CONNECTION.close()


# Delete a phone from database
def delete_phone(id):
    try:
        CONNECTION = sqlite3.connect(DATABASE)
        if CONNECTION:
            CONNECTION.cursor().execute("DELETE FROM phones WHERE id=?", (id,))
            CONNECTION.commit()
            print("phone deleted")
            CONNECTION.close()
    except "Error while deleting a phone" as eve:
        print(eve)
        CONNECTION.close()
