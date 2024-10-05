# server.py

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from interpreter import interpreter
from interpreter import OpenInterpreter

app = FastAPI()
interpreter = OpenInterpreter(
    os=True,
    auto_run=True,
)

@app.route("/chat", methods=["GET", "POST"])
async def chat_endpoint(request: Request):
    if request.method == "POST":
        data = await request.json()
        message = data.get("message", "")
    else:
        message = request.query_params.get("message", "")
    def event_stream():
        for result in interpreter.chat(message, stream=True):
            yield f"data: {result}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.post("/ask")
async def ask_post_endpoint(request: Request):
    return {"error": "BLAH BLAH"}
    data = await request.json()
    message = data.get("message")
    if not message:
        return {"error": "No message provided"}
    return interpreter.chat(message)

@app.get("/history")
def history_endpoint():
    return interpreter.messages
