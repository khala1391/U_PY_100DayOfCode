from flask import Flask, render_template
app = Flask(__name__)

users = ['A','B',"C","D","E","F",]

@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
