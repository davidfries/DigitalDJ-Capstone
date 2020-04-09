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

    def authuser(self, username, password, token):
        pass

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
        # get last client key in db and increment
        client_key = int(self.db.query(
            "SELECT client_key FROM users ORDER BY client_key DESC LIMIT 1;"
            ).as_dict()[0].get("client_key")) + 1
        query="INSERT INTO users (client_key, email, password) VALUES (:client_key,:email,:password)"
        try:
            self.db.query(query,client_key=client_key,email=email,password=password)
        except Exception as e:
            print("create user error {}".format(e))