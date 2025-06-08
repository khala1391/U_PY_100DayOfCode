from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

# @app.route("/<name>")
# def variable():
#     return f"hello <name>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    # return 'User %s' % escape(username)  # old style
    return f'User {escape(username)}'

@app.route('/user2/<name>')
def username(name):
    return f'username is {name}'

if __name__ == "__main__":
    app.run(debug=True)