import socket
import threading
import pickle
from os import _exit

class ClientSocket():
    def __init__(self,key,s):
        self.key=key 
        self.s=s 


class MasterServer():
    def __init__(self):
        self.host="localhost"
        self.port=8889
        self.streamdata=[]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #the SO_REUSEADDR flag tells the kernel to
        self.s.bind((self.host, self.port))
        self.clientsockets=[]
    def conn(self):
        print("starting listen thread")
        self.s.listen(5)
    def sendstream(self):
        print("would be sending the stream right now")
    def listen(self):
        print("listening for connections...")
        # threading.Thread(target=self.conn()).start()
        self.s.listen(100)
        while True:
            
            c, addr = self.s.accept()
            print("accepting connection")
            # c.settimeout(60)
            msg=c.recv(15)
            if msg[:3]==b"key":
                self.clientsockets.append(ClientSocket(msg[:3],c))
            if(msg[4:]==b"stream"):
                threading.Thread(target = self.receivestream,args=(c,)).start()
            elif(msg[4:]==b"mirror"):
                threading.Thread(target = self.sendstream).start()
    def receivestream(self,c):
        print("receiving data")
        while True:
            
            packet=c.recv(4096)
            print("packet length{}".format(len(packet)))
            if not packet:
                c.close()
                break 
            self.streamdata.append(packet)
            print(len(self.streamdata))
        # print("receiving data")
        print(pickle.loads(b"".join(self.streamdata)))

if __name__ == "__main__":
    threading.Thread(target=MasterServer().listen).start()
    # MasterServer().listen()
    while True:
        cmd=input("Enter command: ")
        # print(cmd)
        if(cmd=="exit"):
            _exit(0)
        else:
            print(cmd)
