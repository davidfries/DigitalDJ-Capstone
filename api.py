from flask import Flask,jsonify,request,redirect
from flask_cors import CORS
from backend import DigitalDJBackend
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
db=DigitalDJBackend()
# app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def hello():
    # DigitalDJBackend().createtesttable()
    db.inserttestdata("testuser","test_todo","test_category","1")
    data=db.selecttestdata() 
    print(data)
    return jsonify(data)
@app.route('/createtodo',methods=['POST','OPTIONS'])
def createtodo():
    # if request.method=='POST':
        # data=jsonify(request.data())
        # print(data)
    print(request.form['todo'])
    db.inserttestdata('default',request.form['todo'],request.form['category'],request.form['completed'])
    return '200'
@app.route('/todos',methods=['GET'])
def gettodos():
    if request.method=='GET':
        return jsonify(db.selecttestdata())
if __name__ == '__main__':
    app.run()