from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)
def validate_json(*required_fields):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            if not data:
                return jsonify({"error": "Missing JSON"}), 400
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing field: {field}"}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/')
def hello_world():
    return 'Hello, dog!'

@app.route('/create-user', methods=['POST'])
@validate_json('username', 'email')
def create_user():
    data = request.get_json()
    return jsonify({"message": f"User {data['username']} created!"})


if __name__ == '__main__':
    app.run(debug=True)