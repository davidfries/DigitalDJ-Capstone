import records
from secrets import Secrets as pw
import random
import string
class DigitalDJBackend():
    def __init__(self):
        self.db=records.Database(f'postgresql://digitaldj.cuxdpwvnnhxs.us-east-1.rds.amazonaws.com/digitaldj?user=digitaldj&password={pw.dbpw}',pool_size=50,max_overflow=200)
    def genid(self):
        
        return ''.join(random.choice(string.ascii_lowercase+'0123456789'+string.ascii_uppercase) for i in range(10))
    
    #AUTHENTICATION METHODS

    #def authuser(self, username, password, token):
    def authuser(self, email, password):
        query="SELECT client_key FROM users WHERE email=:email AND password=crypt(:password, password)"
        try:
            return self.db.query(query,email=email,password=password).as_dict(ordered=True)
        except Exception as e:
            print("User authentication error {}".format(e))

    def changepassword(self,password,token):
        pass
    def changeusername(self,currusr,newusr,token):
        pass

    def returnuser(self,username):
        return "Test User123"


    #ROOMS METHODS
    def getrooms(self):
        sql="select * from rooms where room_security=0"
        return self.db.query(sql).as_dict(ordered=True)

    def createroom(self,roomname, quantity, security, genre, owner=None):
        sql="insert into rooms(room_name,genre,max_quantity,room_security,room_key) values(:room_name,:genre,:quantity,:room_security,:key)"
        self.db.query(sql,room_security=security,quantity=quantity,room_name=roomname,genre=genre,key=self.genid())

    def deleteroom(self,roomid):
        pass

    def editroom(self,roomname, quantity, security):
        pass

    #VOTING METHODS
    def getsongs(self,room_key):
        sql="select * from songs where room_key=:room_key"
        return self.db.query(sql,room_key=room_key).as_dict(ordered=True)

    def addsong(self,room_key,song_title):
        song_key=self.genid()
        sql="insert into songs(song_key,room_key,song_title) values(:song_key,:room_key,:song_title)"
        try:
            self.db.query(sql,song_key=song_key,room_key=room_key,song_title=song_title)
        except Exception as e:
            print(e)
            print("error in song add")

        return song_key
    def songvote(self,song_key,room_key,vote_status):
        sql="insert into votes(room_key,song_key,vote_status) values(:room_key,:song_key,:vote_status)"
        self.db.query(sql,song_key=song_key,room_key=room_key,vote_status=vote_status)

    def getsongvotecount(self,song_key):
        sql="select sum(vote_status) as count from votes where song_key=:song_key"
        return self.db.query(sql,song_key=song_key).as_dict()

    #SHARING METHODS
        
        



    #USER METHODS
    def createuser(self,email,password):
        client_key = self.genid()
        query="INSERT INTO users (client_key, email, password) VALUES (:client_key,:email,crypt(:password, gen_salt('bf')))"
        try:
            self.db.query(query,client_key=client_key,email=email,password=password)
        except Exception as e:
            print("create user error {}".format(e))

    def addclienttoroom(self,clientid,room_key):
        # clientid=self.genid()
        query="insert into rooms_activeusers(clientid,room_key) values(:clientid,:room_key)"
        self.db.query(query,clientid=clientid,room_key=room_key)

    def getclientsinroom(self,room_key):
        query="select count(*) from rooms_activeusers where room_key=:room_key"
        return self.db.query(query,room_key=room_key).first().export('json')
    def leaveroom(self,client_key):
        query='delete from rooms_activeusers where clientid=:client_key'
        self.db.query(query,client_key=client_key)

    # CHAT METHODS
    def sendMessage(self,message,sender,room):
        query="INSERT INTO messages (sender, room, message) VALUES (:sender,:room,:message)"
        try:
            self.db.query(query,sender=sender,room=room,message=message)
        except Exception as e:
            print("send message error {}".format(e))

    def getMessages(self,room):
        query="SELECT * FROM messages WHERE room=:room"
        try:
            return self.db.query(query, room=room).as_dict(ordered=True)
        except Exception as e:
            print("get message error {}".format(e))