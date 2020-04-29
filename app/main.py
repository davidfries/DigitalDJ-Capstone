from flask import Flask,jsonify,request,redirect,session,render_template, Response
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
    def __init__(self,room_key,client_key):
        self.room_key=room_key
        self.client_key=client_key
@app.route('/socket.io',methods=['GET'])
def default():
    return render_template("index.html")
@socketio.on('connect')
def on_connect():
    send("Hi!")
@socketio.on('disconnect')
def on_disconnect():
    print("Disconnected a client")
clients=[]
@socketio.on('room_connection')
def room_connection(data):
    print(data)
    # print(str(json.loads(data)))
    # clients.append(Client(json.loads(data)['room_key']))
    room_key=data['room_key']
    client_key=data['client_key']
    # clientdata={"room_key":room_key,"client_key":client_key}
    # clients.append(clientdata)
    join_room(room_key)
    send("joined room!",room=room_key)
    # send("all should see",room=room_key,broadcast=True)
    db.addclienttoroom(client_key,room_key)
    counter=db.getclientsinroom(room_key)
    print(counter)
    emit("active_clients_counter",counter,broadcast=True,room=room_key)
@socketio.on('leave_music_room')
def leave_music_room(data):
    # print(str(data))
    # print(str(json.loads(data)['room_key']))
    # clients.append(Client(json.loads(data)['room_key']))
    db.leaveroom(data['client_key'])
    leave_room(data['room_key'])
    print("leaving room!")
    counter=db.getclientsinroom(data['room_key'])
    emit("active_clients_counter",counter,broadcast=True,room=data['room_key'])
    # room_key=str(json.loads(data)['room_key'])
    # client_key=str(json.loads(data)['client_key'])
    # leave_room(room_key)

@socketio.on('update_songs')
def update_songs(data):
    songs=db.getsongs(data['room_key'])
    emit("client_songs_update",songs,broadcast=True,room=data['room_key'])

@socketio.on('update_chat')
def update_chat(data):
    resp=db.getMessages(data['room_key'])
    emit("client_chat_update",resp,broadcast=True,room=data['room_key'])

#checks when new stream is published to server whether stream_key exists in DB
#and checks if that key corresponds to that room
@app.route('/on_publish',methods=['GET','POST'])
def authstream():
    from urllib.parse import urlparse,parse_qs
    if request.method=='POST':
        print("Posted from server")
        try:
            url=urlparse(request.form['tcurl'])
            room_key=request.form['name']
            stream_key=parse_qs(url.query)['streamkey'][0]
            print(room_key)
            print(stream_key)
            print(db.authstream(room_key,stream_key))
            if len(db.authstream(room_key,stream_key))>0:
                return Response("{'msg':'Successful stream join'",status=201,mimetype='application/json')

            # print(stream_key)
        except Exception as e:
            print(e)
            print("error in stream key parse")
            return Response("{'msg':'UnSuccessful stream join'",status=404,mimetype='application/json')


        return Response("{'msg':'UnSuccessful stream join'",status=404,mimetype='application/json')
    elif request.method =='GET':
        print("Get from server")
        return Response("{'msg':'UnSuccessful stream join'",status=404,mimetype='application/json')

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
def userauth():
    if request.method=='POST':
        data=request.get_json()
        try:
            db.createuser(data['email'],data['password'])
            return jsonify({"msg":"successful user registration"})
        except Exception as e:
            print(e)
            print("error in user registration")
            return jsonify({"msg":"error in user registration {}".format(e)})

@app.route('/login',methods=['POST'])
def loginauth():
    if request.method=='POST':
        data=request.get_json()
        try:
            db.authuser(data['email'],data['password'])
            return "success"
            #print("Successful user authentication")
            #return jsonify({"msg":"successful user authentication {}"})
        except Exception as e:
            print(e)
            print("Error in user authentication")
            return jsonify({"msg":"error in user authentication {}".format(e)})
        
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
            db.createroom(data['room_name'],data['max_listeners'],data['security'],data['genre'],data['stream_key'])
            return jsonify({"msg":"successful room creation"})
        except Exception as e:
            print(e)
            print("error in room creation")
            return jsonify({"msg":"error in room creation {}".format(e)})

# CHAT API METHOD
@app.route('/chat',methods=['GET', 'POST'])
def message():
    if request.method=='GET':
        try:
            return jsonify(db.getMessages(request.args.get("room_key")))
        except Exception as e:
            print(e)
            print("Error when getting messages")
            return jsonify({"msg":"error when getting messages {}".format(e)})

    if request.method=='POST':
        data=request.get_json()
        try:
            db.sendMessage(data['message'],data['sender'],data['room_key'])
            print("Message sent")
            return "success"
        except Exception as e:
            print(e)
            print("Error when sending message")
            return jsonify({"msg":"error when sending message {}".format(e)})

@app.route('/newid',methods=['GET'])
def getid():
    if request.method=='GET':
        data={"id":db.genid()}
        return jsonify(data)
if __name__ == '__main__':
    socketio.run(app,host='localhost',port=5000,debug=True)