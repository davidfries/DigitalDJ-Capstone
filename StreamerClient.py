import soundcard as sc 
import socket
import pickle
try:
    default_speaker = sc.default_speaker()
except:
    print('Error in speaker lookup')
mics = sc.all_microphones(include_loopback=True)
print(mics[0])
try:
    loopback = sc.get_microphone('Audio',include_loopback=True)
except:
    print('error in microphone binding')
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    print('created socket')
    
    # s.connect(('127.0.0.1',8001))
    with loopback.recorder(samplerate=48000) as mic:
        while True:
            data=mic.record(numframes=1024)
            print(data)
            # print(data)
            # comp = pickle.dumps(data)
            s.connect(("localhost",8889))
            print(len(pickle.dumps(data)))
            s.send(pickle.dumps(data))
            # sp.play(data)