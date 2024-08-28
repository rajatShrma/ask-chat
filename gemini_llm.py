import google.generativeai as genai
import os


genai.configure(api_key=os.environ['GEMINI_API'])
model = genai.GenerativeModel('gemini-1.5-flash')

async def gemini_model(prompt:str):
    response = model.generate_content(prompt)
    return response.text