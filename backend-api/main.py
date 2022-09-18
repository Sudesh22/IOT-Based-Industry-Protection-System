from time import time
from flask import Flask, jsonify, request
import sqlite3, socket
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return ("<h1>Hello</h1>")

@app.post("/<int:device_id>/data")
def allow(device_id):
    data = request.get_json()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Temp = data["Temperature"]
    Status = data["Status"]
    Humi = data["Humidity"]
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS DataLogging(
                    Device_Id int,
                    Status text,
                    Temp int,
                    Humi int,
                    Time text)
                """)
    c.execute("INSERT INTO DataLogging VALUES (?,?,?,?,?)", (device_id, Status, Temp, Humi, timestamp))
    conn.commit()
    conn.close()
    return f'Data sent by {str(device_id)} was received successfully '

@app.post("/<int:device_id>/dashboard")
def dashboard(device_id):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    Data = c.execute("SELECT * FROM DataLogging WHERE Device_Id = ? ORDER BY Time DESC'", (device_id,)).fetchone()
    conn.close()
    return 

@app.post("/signin")
def signIn():
    email = request.get_json().get("email")
    password = request.get_json().get("password")
    if isValid(email, password):
        return jsonify(isValid(email,password)) 
    else:
         return jsonify({"status": "Error logging in"})

def isValid(email, password): 
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    Data = c.execute("SELECT * FROM loginDetails WHERE email = ? AND password = ?", (email, password)).fetchall()
    if (Data==[]):
        return {"status": "Error logging in"}
    else:
        if (email==Data[0][2] and password==Data[0][3]):
            conn.close()
            print(Data)
            return Data
        else:
            conn.close()
            return False

@app.post("/signup")
def signUp():
    email = request.get_json().get("email")
    password = request.get_json().get("password")
    name = request.get_json().get("name")
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("INSERT INTO loginDetails (name,email,password) VALUES (?,?,?)", (name,email,password))
    data = c.execute("SELECT * FROM loginDetails WHERE email = ? AND password = ?", (email, password)).fetchall()
    conn.commit()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.debug=True
    IPAddr = socket.gethostbyname(socket.gethostname())  
    app.run(host=IPAddr, port=5000)