from fastapi import APIRouter, Body, Query
from gemini_llm import gemini_model
from claude_llm import claude_model
from pydantic import BaseModel

app_router=APIRouter()
class PromptInput(BaseModel):
    system_input: str
    prompt: str

@app_router.post('/gemini')
async def gemini_chat(request_body: dict = Body(...)):
    prompt = request_body.get("prompt")
    if not prompt:
        return {"error": "Missing prompt in request body"}

    response = await gemini_model(prompt)
    return {"data": response}

@app_router.post('/claude')
async def claude_chat(input: PromptInput):
    system_input = input.system_input
    prompt = input.prompt
    if not prompt:
        return {"error": "Missing prompt in request body"}

    response = await claude_model(system_input, prompt)
    return {"data": response}