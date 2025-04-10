from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'university_dispancery_management_system'
}

# Function to get database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

@app.route('/api/patients', methods=['GET'])
def get_patients():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patient")
        patients = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(patients)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM doctor")
        doctors = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(doctors)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT a.*, p.Patient_name, d.doctor_name 
            FROM appointment a 
            JOIN patient p ON a.Patient_id = p.Patient_id 
            JOIN doctor d ON a.doctor_id = d.doctor_id
        """)
        appointments = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(appointments)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/medicines', methods=['GET'])
def get_medicines():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medicine")
        medicines = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(medicines)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/prescriptions', methods=['GET'])
def get_prescriptions():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.*, pt.Patient_name, d.doctor_name, m.medicine_name 
            FROM precption p 
            JOIN patient pt ON p.Patient_id = pt.Patient_id 
            JOIN doctor d ON p.doctor_id = d.doctor_id 
            JOIN medicine m ON p.medicine_id = m.medicine_id
        """)
        prescriptions = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(prescriptions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
