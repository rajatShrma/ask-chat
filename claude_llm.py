import json
import anthropic
import dotenv
import os
from typing import Any

dotenv.load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv('CLAUDE_API')
)

async def claude_model(system_input:str, prompt:Any):
    system_input = f"""
        You are a class teacher. Write a comprehensive student profile record paragraphs of around 350 words based on the student information provided.
        Task: 
        The profile should include details about their academic performance, behavior, and extracurricular activities.

        Strengths: [Highlight the student's strengths in specific subjects, do not display marks in number unless there is a significant change.]
        
        Areas for Improvement: [Identify areas where the student could benefit from additional support]
        
        Classroom Participation: [Describe the student's involvement in class discussions and activities]
        
        Homework Completion: [Comment on the student's consistency and quality of homework]
        
        Social Interactions: [Assess the student's interactions with peers and teachers]
        
        Extracurricular Activities: [List any extracurricular activities the student is involved in]
        
        Overall Assessment: Provide a summary of the student's overall performance and development, highlighting both their strengths and areas for growth.
    """
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