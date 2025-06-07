import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def get_blog():
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(url).json()
    return render_template('blog.html', posts=posts)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
