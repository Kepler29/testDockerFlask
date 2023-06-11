from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return jsonify({"response": "Hello world"})

@app.route("/link1")
def test1():
  return jsonify({"response": "sihiuiente link"})

@app.route("/link2")
def test1():
  return jsonify({"response": "sihiuiente link 2"})

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=4000)