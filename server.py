# server.py

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from interpreter import interpreter
from interpreter import OpenInterpreter

app = FastAPI()
interpreter = OpenInterpreter(
    os=True,
    auto_run=True,
)

@app.get("/chat")
def chat_endpoint(message: str):
    def event_stream():
        for result in interpreter.chat(message, stream=True):
            yield f"data: {result}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/history")
def history_endpoint():
    return interpreter.messages
