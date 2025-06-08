from flask import Flask, request, jsonify
from functools import wraps
import time

app = Flask(__name__)

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper

@app.route('/slow')
@timer
def slow_route():
    time.sleep(2)
    return "Done sleeping!"

if __name__ == "__main__":
    app.run(debug=True)