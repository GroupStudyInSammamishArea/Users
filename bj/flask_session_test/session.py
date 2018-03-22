from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return 'Session test'

@app.route('/flask_session/login/<username>')
def login(username):
    session['user'] = "hello " + username
    return 'Cookie Saved'

@app.route('/flask_session/restricted')
def restricted():
    if 'user' in session:
        return "Can call restricted"
    else:
        return None

@app.route('/flask_session/logout')
def logout():
    session.pop('user', None)
    return 'logged out'

@app.route('/flask_session/getsessionuser')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in'

if __name__ == '__main__':
    app.run(debug=True)