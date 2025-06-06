from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    sum_value = 1+1
    current_year = datetime.now().year
    # return render_template('index.html')
    return render_template('index.html',
                           sum = sum_value,
                           current_year = current_year)

if __name__ == '__main__':
    app.run(debug=True)
