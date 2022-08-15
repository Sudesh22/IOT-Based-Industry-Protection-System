from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)

@app.get("/")
def home():
    return("<h1>hello<h1/>")

@app.post("/newWord")
def NewWord():
    response = 'abcde'  
    message = {"answer": response}
    print(message)
    return jsonify(message)

@app.post("/<int:device_id>")
def allow(device_id):
    data = request.get_json()
    # if device_id < 25:
    func(device_id, data)
    return f'You have been allowed to enter because the data is {str(device_id)}'
    # else:
    #     return f'You are not allowed'

def func(Id, Data):
    print("Device id is:",Id," and the data received is:",  Data)
    # conn = sqlite3.connect('test.db')
    # c = conn.cursor()
    # c.execute("SELECT rowid,* FROM tasks ORDER BY due DESC")
    # # c.execute("INSERT INTO tasks VALUES (?,?,?,?)", (task, desc, date, 1))
    # conn.commit()
    # conn.close()

if __name__ == "__main__":
    app.run(debug=True)