from fastapi import APIRouter, Body, Query
from gemini_llm import gemini_model
from claude_llm import claude_model

app_router=APIRouter()

@app_router.post('/gemini')
async def gemini_chat(request_body: dict = Body(...)):
    prompt = request_body.get("prompt")
    if not prompt:
        return {"error": "Missing prompt in request body"}

    response = await gemini_model(prompt)
    return {"data": response}

@app_router.post('/claude')
async def claude_chat(request_body: dict = Body(...)):
    prompt = request_body.get("prompt")
    if not prompt:
        return {"error": "Missing prompt in request body"}

    response = await claude_model(prompt)
    return {"data": response}