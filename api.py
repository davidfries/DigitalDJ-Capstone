from flask import Flask,jsonify,request,redirect
from flask_cors import CORS
from backend import DigitalDJBackend
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}).init_app(app)
db=DigitalDJBackend()
# app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/getsongs',methods=['GET'])
def getsongs():
    return jsonify(db.getsongs(request.args.get("room_key")))
@app.route('/addsong',methods=['POST'])
def addsong():
    if request.method=='POST':
        data=request.get_json()
        db.addsong(data['song_key'],data['room_key'],data['song_title'])
        return "success!"
@app.route('/rooms',methods=['GET'])
def getallrooms():
    if request.method=='GET':
        return jsonify(db.getrooms())

# USER API METHODS
@app.route('/',methods=['POST'])
def registeruser():
    db.createuser(request.request.form['email'],request.form['password'])

@app.route('/returnuser',methods=['GET','POST'])
def returnuser():
    if request.method=='POST':
        # if(jsonify(request.get_json())['username']):
        return request.get_json()['username']  
        # else:
        #     return "empty username field" 
          
# SONG VOTE API METHOD
@app.route('/songvote',methods=['POST'])
def songvote():
    if request.method=='POST':
        data=request.get_json()
        print(data)
        return "voted!"

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

   