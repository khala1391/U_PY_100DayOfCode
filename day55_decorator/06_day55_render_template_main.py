from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# way1 CLI: flask --app main run

# way2 run by __main__


@app.route("/bye")
def say_bye():
    return "<h1>bye</h1> \
        <h1>bye</h1>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def greet(name):
    return f"Hello {name} !"

@app.route('/<int:number1>')
def calculate(number1):
    results = number1 + 10
    return f"Hello {results} !"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath is {escape(subpath)}'


if __name__ == "__main__":
    app.run(debug=True)

