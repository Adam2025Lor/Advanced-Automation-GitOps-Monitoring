# app/main.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(message="Hello from QuakeWatch via Flask!")

@app.route("/health")
def health():
    return jsonify(status="ok")
