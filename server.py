# server.py

import io
import json
import sys
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from interpreter import interpreter
from interpreter import OpenInterpreter


custom_instructions = """
Personality & Capabilities:
- You're name is Rose, you are a personal assistant that lives on my home desktop computer.
- You can help with anything, you can access the internet.
- You can install new packages and tools
- You can run any code to achieve the goal.
- And if at first you don't succeed, try again and again!
- You are capable of any task.

Output:
- You should ALWAYS respond in machine readabile, valid json, with not line-breaks or pretty-printing.
- You should always respond with a "response" key, and optionally a "data" key, unless the response is an error, in which case you should respond with an "error" key.
"""

app = FastAPI()
interpreter = OpenInterpreter(
    os=True,
    auto_run=True,
    custom_instructions=custom_instructions,
)

# Streaming chat response
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

# Non-streaming version of the chat endpoint
@app.route("/ask", methods=["GET", "POST"])
async def ask_post_endpoint(request: Request):
    try:
        if request.method == "POST":
            data = await request.json()
            message = data.get("message")
            if not message:
                return JSONResponse({"error": "No message provided"}, status_code=400)
        elif request.method == "GET":
            message = request.query_params.get("message", "")
            if not message:
                return JSONResponse({"error": "No message provided"}, status_code=400)
        else:
            return JSONResponse({"error": "Invalid request method"}, status_code=405)
        return JSONResponse(interpreter.chat(message))
    except Exception as e:
        return JSONResponse({"error": f"Failed to process request: {e}"}, status_code=500)

# Get the history of messages
@app.get("/history")
def history_endpoint():
    return interpreter.messages
