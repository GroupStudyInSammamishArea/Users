from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    session['user'] = 'person in sammamish'
    return 'Cookie Saved'

@app.route('/login/<username>')
def login(username):
    session['user'] = "hello " + username
    return 'Cookie Saved'

@app.route('/getsessionuser')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped'

if __name__ == '__main__':
    app.run(debug=True)