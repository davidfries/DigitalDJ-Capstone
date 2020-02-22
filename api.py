from flask import Flask,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello():
    json=[{"data":{
    "1":"Wash car",
    "2":"Clean room",
    "3":"Do homework"}}]
    
    return jsonify(json)

if __name__ == '__main__':
    app.run()