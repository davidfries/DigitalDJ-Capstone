import records

class DigitalDJBackend():
    def __init__(self):
        self.db=records.Database('sqlite:///test.db',connect_args={'check_same_thread': False})
        
    
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

    def createroom(self,roomname, quantity, security, owner):
        pass

    def deleteroom(self,roomid):
        pass

    def editroom(self,roomname, quantity, security):
        pass

    #VOTING METHODS







    #SHARING METHODS
        
        