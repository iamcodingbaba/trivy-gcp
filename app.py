from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"message": "Backend is running successfully!"})
@app.route('/health')
def health():
