from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from hashlib import sha256
import config
import certifi
import uuid

app = Flask(__name__)
app.config.from_object(config)

client = MongoClient(config.MONGO_URI,tlsCAFile=certifi.where())
db = client["Userdatabase"]
col = db["users"]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = col.find_one({'username': username})
        if user and sha256(password.encode("utf-8")).hexdigest()==user['password']:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            hashed_password = sha256(password.encode("utf-8")).hexdigest()
            col.insert_one({'_id':uuid.uuid4().hex,'username': username, 'password': hashed_password})
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error='Passwords do not match')
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)