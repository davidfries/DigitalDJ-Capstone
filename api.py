from flask import Flask,jsonify,request,redirect
from flask_cors import CORS
from backend import DigitalDJBackend
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
db=DigitalDJBackend()
# app.config['CORS_HEADERS'] = 'Content-Type'



if __name__ == '__main__':
    app.run()