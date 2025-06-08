from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.args.get('api_key') == '123456':
            return func(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized"}), 401
    return wrapper

@app.route('/secure-data')
@require_api_key
def secure_data():
    return jsonify({"data": "correct api key"})


if __name__ == "__main__":
    app.run(debug=True)


# run pass if assign api
# http://127.0.0.1:5000/secure-data?api_key=123456