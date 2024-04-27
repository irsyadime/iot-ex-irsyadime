import serial
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="iot_algoritma"
)
cursor = db.cursor()

ser = serial.Serial('COM3',9600)

try:
    while True:
        data = ser.readline().decode().strip()

        query = "INSERT INTO mct_data (data) VALUES (%s)"
        cursor.execute(query, (data,))
        db.commit()
        print("Data inserted:", data)

except KeyboardInterrupt:
    ser.close()
    db.close()