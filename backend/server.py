"""Chat app with websockets

Start with uvicorn main:app --reload
"""

from fastapi import FastAPI, WebSocket

app = FastAPI()

connections: list[WebSocket] = []
history: list[str] = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)

    while True:
        data = await websocket.receive_text()

        history.append(data)
        print(history)
        for connection in connections:
            await connection.send_text("<br>".join(history))
