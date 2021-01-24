import phoneDb
from flask import Flask, request, jsonify

app = Flask(__name__)

phones_list = [
    {
        "id": 0,
        "phone_model": "Iphone 11",
        "serial_number": "1X3g5V66",
        "color": "White"
    },
    {
        "id": 1,
        "phone_model": "Samsung Galaxy S21",
        "serial_number": "1w3f5g6h",
        "color": "Black"
    }
]


@app.route("/phones", methods=['GET', 'POST'])
def phones():
    if request.method == 'GET':
        if len(phones_list) > 0:
            return jsonify(phones_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        id = phones_list[-1]['id'] + 1
        phone_model = request.form['phone_model']
        serial_number = request.form['serial_number']
        color = request.form['color']

        new_phone = {
            'id': id,
            'phone_model': phone_model,
            'serial_number': serial_number,
            'color': color
        }
        
        phoneDb.insert_new_phone(phone_model, serial_number, color)
        phones_list.append(new_phone)
        return jsonify(phones_list), 201


if __name__ == '__main__':
    phoneDb.create_connection("phones_db.db")
    app.run(port=3000, debug=True)
