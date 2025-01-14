import asyncio
import websockets

async def hello():
    async with websockets.connect(
            "ws://localhost:45826") as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
