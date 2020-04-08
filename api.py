from flask import Flask,jsonify,request,redirect,session,render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send,join_room, leave_room
import json
from backend import DigitalDJBackend
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}).init_app(app)
socketio = SocketIO(app,cors_allowed_origins='*')
db=DigitalDJBackend()
# app.config['CORS_HEADERS'] = 'Content-Type'

# SOCKET METHODS GO HERE
class Client():
    def __init__(self,room_key):
        self.room_key=room_key
@app.route('/socket.io',methods=['GET'])
def default():
    render_template("index.html")
@socketio.on('connect')
def on_connect():
    send("Hi!")
clients=[]
@socketio.on('room_connection')
def room_connection(data):
    # print(str(data))
    print(str(json.loads(data)))
    # clients.append(Client(json.loads(data)['room_key']))
    room_key=str(json.loads(data)['room_key'])
    client_key=str(json.loads(data)['client_key'])
    join_room(room_key)
    send("joined room!")
    send("all should see",room=room_key,broadcast=True)
    db.addclienttoroom(client_key,room_key)
@socketio.on('leave_music_room')
def leave_music_room(data):
    # print(str(data))
    # print(str(json.loads(data)['room_key']))
    # clients.append(Client(json.loads(data)['room_key']))
    room_key=str(json.loads(data)['room_key'])
    client_key=str(json.loads(data)['client_key'])
    leave_room(room_key)





@app.route('/getsongs',methods=['GET'])
def getsongs():
    return jsonify(db.getsongs(request.args.get("room_key")))
@app.route('/addsong',methods=['POST'])
def addsong():
    if request.method=='POST':
        data=request.get_json()
        song_key=db.addsong(data['room_key'],data['song_title'])
        return jsonify({"song_key":song_key})
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

@app.route('/register',methods=['POST'])
def registeruser():
    db.createuser(request.form['userid'],request.form['password'],request.form['email'])
        
# SONG VOTE API METHOD
@app.route('/getsongvotecount',methods=['GET'])
def getsongvotecount():
    if request.method =='GET':
        count=db.getsongvotecount(request.args.get("song_key"))
        return jsonify(count)

@app.route('/songvote',methods=['POST'])
def songvote():
    if request.method=='POST':
        data=request.get_json()
        print(data)
        try:
            db.songvote(data['song_key'],data['room_key'],data['vote_status'])
            return "success"
        except Exception as e:
            print(e)
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
    socketio.run(app,host='localhost',port=5000,debug=True)

   