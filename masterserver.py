import socket
import threading
import pickle
class MasterServer():
    def __init__(self):
        self.host="localhost"
        self.port=8889
        self.streamdata=[]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #the SO_REUSEADDR flag tells the kernel to
        self.s.bind((self.host, self.port))
    def listen(self):
        print("listening for connections...")
        self.s.listen(5)
        while True:
            c, addr = self.s.accept()
            c.settimeout(60)
            threading.Thread(target = self.receivestream(c)).start()
    def receivestream(self,c):
        # while True:
        data=c.recv(4096)
        # print("receiving data")
        print(pickle.loads(data))

if __name__ == "__main__":
    MasterServer().listen()