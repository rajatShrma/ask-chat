import json
import anthropic
import dotenv
import os
from typing import Any
from constant import report_prompt

dotenv.load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv('CLAUDE_API')
)

async def claude_model(system_input:str, prompt:Any):
    system_input = report_prompt
    message = client.messages.create(
        model='claude-3-5-sonnet-20240620',
        max_tokens=1000,
        temperature=0.3,
        system=system_input,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": str(prompt)
                    }
                ]
            }
        ]
    )  

    translation_prompt = f"""
        You are a Nepali translator who translates English language to Nepali. 
        Translate the user input English text into Nepali. 
        Keep the name in both English and Nepali language.
        Class name should be an actual name.
        Ensure the translation is accurate and clearly in Nepali, avoiding any mix with Hindi. 
        The content should be translated in a way that retains the original meaning and tone.
    """
    response = client.messages.create(
        model='claude-3-5-sonnet-20240620',
        max_tokens=3000,
        temperature=0.3,
        system=translation_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message.content[0].text
                    }
                ]
            }
        ]
    )  
    return response.content[0].text