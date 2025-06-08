import requests
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

current_year = datetime.now().year

@app.route('/')
def index():
    return render_template('index.html',current_year = current_year)

@app.route('/blog')
def get_blog():
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    all_posts = requests.get(url).json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
