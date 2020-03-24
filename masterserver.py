import socket
import threading
import pickle
import sys
class MasterServer():
    def __init__(self):
        self.host="localhost"
        self.port=8889
        self.streamdata=[]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #the SO_REUSEADDR flag tells the kernel to
        self.s.bind((self.host, self.port))
    def conn(self):
        print("starting listen thread")
        self.s.listen(5)
    def listen(self):
        print("listening for connections...")
        # threading.Thread(target=self.conn()).start()
        self.s.listen(5)
        while True:
            print("accepting connection")
            c, addr = self.s.accept()
            c.settimeout(60)
            threading.Thread(target = self.receivestream(c)).start()
    def receivestream(self,c):
        print("receiving data")
        while True:
            
            packet=c.recv(4096)
            if not packet:break 
            self.streamdata.append(packet)
        # print("receiving data")
        print(pickle.loads(b"".join(self.streamdata)))

if __name__ == "__main__":
    # threading.Thread(target=MasterServer().listen()).start()
    MasterServer().listen()
    while True:
        cmd=input("Enter command: ")
        if(cmd=="exit"):
            sys.exit()
