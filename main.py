from flask import Flask, jsonify, json
import os

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}, 200

@app.get("/health")
async def health():
    return {"status": "ok"}

# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return { 'message': 'Hello World!' }, 200
#
# @app.route('/about')
# def health():
#     return jsonify({'status: ok'}), 200
#     # return 'OK'

if __name__ == '__main__':
    # port = os.environ.get('PORT', 8080)
    # gunicorn app:app --bind 0.0.0.0:8080
    # app.run(host='0.0.0.0', port=8080, debug=True)
    # uvicorn main:app --host 127.0.0.1 --port 8080 --reload --workers 1
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=1)
