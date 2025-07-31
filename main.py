from dotenv import load_dotenv
from src import SearchTool
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse


load_dotenv()


app = FastAPI()


@app.get("/search")
def search(query: str):
    return SearchTool(query=query).run()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.get("/sse")
async def sse():
    async def event_generator():
        for i in range(10):
            yield {"data": f"Message {i}"}

    return EventSourceResponse(event_generator())
