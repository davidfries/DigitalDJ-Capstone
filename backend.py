import records
from secrets import Secrets as pw
class DigitalDJBackend():
    def __init__(self):
        self.db=records.Database(f'postgresql://digitaldj.cuxdpwvnnhxs.us-east-1.rds.amazonaws.com/digitaldj?user=digitaldj&password={pw.dbpw}')
        
    
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

    def createroom(self,roomname, quantity, security, owner):
        pass

    def deleteroom(self,roomid):
        pass

    def editroom(self,roomname, quantity, security):
        pass

    #VOTING METHODS





    #SHARING METHODS
        
        



    #USER METHODS
    def createuser(self,userid,password,email):
        query="INSERT INTO users (userid, email, password) VALUES (:userid,crypt(:password, gen_salt('bf')),:email)"
        try:
            self.db.query(query,userid=userid,email=email,password=password)
        except Exception as e:
            print("create user error {}".format(e))