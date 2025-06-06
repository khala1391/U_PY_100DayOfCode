import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/<name>')
def predict(name):
    gender_url = "https://api.genderize.io"
    age_url = "https://api.agify.io"
    param = {"name":name}
    gender_response = requests.get(gender_url, params=param)
    age_response = requests.get(age_url, params=param)
    gender_guess = gender_response.json().get('gender')
    age_guess = age_response.json().get('age')
    
    return render_template('predict.html',
                           name = name,
                           gender = gender_guess,
                           age = age_guess)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
