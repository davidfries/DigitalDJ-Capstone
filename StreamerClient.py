import soundcard as sc 
import socket
import pickle
import threading
from os import _exit
try:
    default_speaker = sc.default_speaker()
except:
    print('Error in speaker lookup')
mics = sc.all_microphones(include_loopback=True)
print(mics[0])
# try:
#     loopback = sc.get_microphone('Audio',include_loopback=True)
# except:
#     print('error in microphone binding')
def playstream(self,data):
    try:
        default_speaker = sc.default_speaker()
    except:
        print('Error in speaker lookup')
    with default_speaker.player(48000) as sp:
        sp.play(data)
def sendaudio(threadnum):
    msg=b"msg:stream"
    try:
        loopback = sc.get_microphone('Audio',include_loopback=True)
    except:
        print('error in microphone binding')
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        
        s.connect(("localhost",8889))
        print('created socket')
        s.send(msg)
        # s.connect(('127.0.0.1',8001))
        with loopback.recorder(samplerate=48000) as mic:
            while True:
                data=mic.record(numframes=1024)
                # print(data)
                # print(data)
                # comp = pickle.dumps(data)
                
                # print(len(pickle.dumps(data)))
                print("data sending thread #{}".format(threadnum))
                s.send(pickle.dumps(data))
                # sp.play(data)
if __name__ == "__main__":
    for i in range(1,2):
        print("Starting thread #{}".format(i))
        threading.Thread(target=sendaudio,args=(i,)).start()
    while True:
        cmd=input("Enter command: ")
        # print(cmd)
        if(cmd=="exit"):
            _exit(0)
        else:
            print(cmd)