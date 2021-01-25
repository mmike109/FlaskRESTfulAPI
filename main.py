import phoneDb
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/phones", methods=['GET', 'POST'])
def phones():
    if request.method == 'GET':
        phones_list = [
            dict(id=row[0], phone_model=row[1],
                 serial_number=row[2], color=row[3])
            for row in phoneDb.db_connection_cursor().execute("SELECT * FROM phones")
        ]
        if phones_list is not None:
            return jsonify(phones_list)

    if request.method == 'POST':
        phone_model = request.form['phone_model']
        serial_number = request.form['serial_number']
        color = request.form['color']

        # Insert a new phone into the database and add it to the API
        phoneDb.insert_new_phone(phone_model, serial_number, color)
        return "Phone Entered Successfully"


@app.route("/phones/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def find_phone(id):
    phone = None
    if request.method == 'GET':
        phoneDb.db_connection_cursor().execute("SELECT FROM phones WHERE id=?", (id,))
        rows = phoneDb.db_connection_cursor().execute("SELECT * FROM phones")
        for p in phoneDb.db_connection_cursor().execute("SELECT * FROM phones"):
            phone = p
        if phone is not None:
            return jsonify(phone), 200
        else:
            return "Error occurred"


if __name__ == '__main__':
    phoneDb.create_connection()
    app.run(port=3000, debug=True)
