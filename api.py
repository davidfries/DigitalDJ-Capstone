from flask import Flask,jsonify,request,redirect
from flask_cors import CORS
from backend import DigitalDJBackend
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
db=DigitalDJBackend()
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/returnuser',methods=['GET','POST'])
def returnuser():
    if request.method=='POST':
        # if(jsonify(request.get_json())['username']):
        return request.get_json()['username']  
        # else:
        #     return "empty username field" 
@app.route('/rooms',methods=['GET'])
def getallrooms():
    if request.method=='GET':
        return jsonify(db.getrooms())


@app.route('/addroom',methods=['POST'])
def addroom():
    if request.method=='POST':
        data=request.get_json()
        try:
            db.createroom(data['room_name'],data['quantity'],data['roomsecurity'],data['genre'])
            return jsonify({"msg":"successful room creation"})
        except Exception as e:
            print(e)
            print("error in room creation")
            return jsonify({"msg":"error in room creation {}".format(e)})
@app.route('/newid',methods=['GET'])
def getid():
    if request.method=='GET':
        data={"id":db.genid()}
        return jsonify(data)
if __name__ == '__main__':
    app.run()

   