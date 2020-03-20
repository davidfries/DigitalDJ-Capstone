import websockets
import asyncio
import numpy as np 
import sys
import json

users=[]
async def notify_connection():
    if users:
        print("notify connection event")
        await asyncio.wait([user.send("New user connected") for user in users])
async def notify_users():
    if users:
        print("notify user event")
        await asyncio.wait([user.send(users_event()) for user in users])
def users_event():
    return json.dumps({"type:":"users","count":len(users)})

async def adduser(websocket):
    print("add user event")
    users.append(websocket)
    await notify_users()

async def receivestreamconnection(websocket,path):
    # loop=asyncio.get_event_loop()
    await adduser(websocket)
    try:
        await websocket.send("Connected!")
        async for message in websocket:
            data=json.loads(message)
            if data['action']=="user_connection":
                await notify_connection()
    # url="ws://localhost:8765"
    # async with websockets.connect(url) as websocket:
    # users.append(websocket)
    # print("user connected")
    # await websocket.send("ready")
    # data= websocket.recv()
    
    except Exception as e:
        print(e)
        print("bad shit happened")
    # print(data)
    # print("Connected users {}".format(len(users)))

server=websockets.serve(receivestreamconnection,"localhost",8765)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()

