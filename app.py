from flask import Flask, jsonify, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        response = {"work": "Działa!"}
        return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
