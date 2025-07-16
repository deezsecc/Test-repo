from flask import request, Flask
import os
import sqlite3

app = Flask(__name__)

# ❌ Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    return os.popen(f"ping -c 1 {host}").read()

# ❌ SQL Injection
@app.route('/login')
def login():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
    result = conn.execute(query).fetchall()
    return str(result)

# ❌ XSS
@app.route('/echo')
def echo():
    msg = request.args.get('msg')
    return f"<h1>{msg}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
