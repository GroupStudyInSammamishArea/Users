from datetime import timedelta
from flask import Flask
from flask_login import (LoginManager, login_required, login_user, current_user, logout_user, UserMixin)
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

#Flask-Login Login Manager
login_manager = LoginManager()

@app.route('/')
def index():
    return 'flask login test'

@app.route('/flask_login/login')
def login():
    user = User.get('user1')
    login_user(user, remember=True)
    return 'login_user is called'

@app.route("/flask_login/restricted")
@login_required
def restricted_page():
    return "Can call restricted"

@app.route("/flask_login/logout")
@login_required
def logout_page():
    logout_user()
    return 'logged out'

# Login stuff
@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

#####################################################################################
class User(UserMixin):
    """
    User Class for flask-Login
    """
    def __init__(self, userid, password):
        self.id = userid
        self.password = password

    def get_auth_token(self):
        """
        Encode a secure token for cookie
        """
        data = [str(self.id), self.password]
        return login_serializer.dumps(data)

    @staticmethod
    def get(userid):
        for user in USERS:
            if user[0] == userid:
                return User(user[0], user[1]) # User name and password
        return None
#####################################################################################

if __name__ == '__main__':
    #Create a quick list of users (username, password).
    USERS = (("user1", "pass1"),("user2", "pass2"))

    #Change the duration of how long the Remember Cookie is valid on the users
    #computer.  This can not really be trusted as a user can edit it.
    app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=14)

    #Tell the login manager where to redirect users to display the login page
    login_manager.login_view = "/flask_login/login/"
    #Setup the login manager.
    login_manager.setup_app(app)

    app.run(debug=True)