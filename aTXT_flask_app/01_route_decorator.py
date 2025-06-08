# activate by run on current main directory
# venv\Scripts\activate

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, dog!'



if __name__ == "__main__":
    app.run(debug=True)