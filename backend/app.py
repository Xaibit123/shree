from flask import Flask, request, jsonify
from openpyxl import Workbook
import os

app = Flask(__name__)

# Create a workbook and sheet (if it doesn't already exist)
excel_file = 'user_data.xlsx'

if not os.path.exists(excel_file):
    wb = Workbook()
    ws = wb.active
    ws.append(["Name", "Age"])  # Adding column headers
    wb.save(excel_file)

# Endpoint to save data to Excel
@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    if not name or not age:
        return jsonify({"error": "Name and age are required!"}), 400

    # Save the data to Excel
    wb = Workbook()
    ws = wb.active
    ws.append([name, age])
    wb.save(excel_file)

    return jsonify({"message": "Data saved successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Flask app runs on port 5000
