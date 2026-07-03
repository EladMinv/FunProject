from flask import Flask, jsonify, json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return { 'message': 'Hello World!' }, 200

@app.route('/about')
def health():
    return jsonify({'status: ok'}), 200
    # return 'OK'

if __name__ == '__main__':
    port = os.environ.get('PORT', 8080)
    app.run(host='0.0.0.0', port=8080, debug=True)