import records
from secrets import Secrets as pw
class DigitalDJBackend():
    def __init__(self):
        self.db=records.Database(f'postgresql://digitaldj.cuxdpwvnnhxs.us-east-1.rds.amazonaws.com/digitaldj?user=digitaldj&password={pw.dbpw}')
    def genid(self):
        import random
        digits=[i for i in range(0,10)]
        rand=""
        for i in range(1,6):
            rand+=str(digits[random.randint(0,10)])
        return rand
    
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
        sql="select * from rooms"
        return self.db.query(sql).as_dict(ordered=True)

    def createroom(self,roomname, quantity, security, genre, owner=None):
        sql="insert into rooms(room_name,genre,max_quantity,room_security) values(:room_name,:genre,:quantity,:room_security)"
        self.db.query(sql,room_security=security,quantity=quantity,room_name=roomname,genre=genre)

    def deleteroom(self,roomid):
        pass

    def editroom(self,roomname, quantity, security):
        pass

    #VOTING METHODS







    #SHARING METHODS
        
        