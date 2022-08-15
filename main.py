from time import time
from flask import Flask, jsonify, request
import sqlite3, socket
from datetime import datetime
app = Flask(__name__)

@app.get("/")
def home():
    return("<h1>hello<h1/>")

@app.post("/newWord")
def NewWord():
    response = 'Working'  
    message = {"answer": response}
    print(message)
    return jsonify(message)

@app.post("/<int:device_id>")
def allow(device_id):
    data = request.get_json()
    log_data(device_id, data)
    return f'You have been allowed to enter because the data is {str(device_id)}'

def log_data(Id, Data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Device id is:",Id," and the data received is:", Data, "at time:", timestamp)
    Temp = Data['text']
    Status = Data['answer']
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS DataLogging(
                    Device_Id int,
                    Status text,
                    Temp int,
                    Time text)
                """)
    # c.execute("SELECT rowid,* FROM tasks ORDER BY due DESC")
    c.execute("INSERT INTO DataLogging VALUES (?,?,?,?)", (Id, Status, Temp, timestamp))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.debug=True
    IPAddr = socket.gethostbyname(socket.gethostname())  
    app.run(host=IPAddr, port=5000)