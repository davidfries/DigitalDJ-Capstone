import asyncio
import websockets
import json

async def hello():
    uri = "ws://localhost:5000/test"
    # while True:
    async with websockets.connect(uri) as websocket:
        
        name = "test data from client"
        data={"event":"connection","username":"djtest"}
        await websocket.send(json.dumps(data))
        # print(f"> {name}")
        
        # greeting = await websocket.recv()
        # print(greeting)

asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()