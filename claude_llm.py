import anthropic
import dotenv
import os


dotenv.load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv('CLAUDE_API')
)

def claude_model(prompt:str):
    message = client.messages.create(
        model='claude-3-5-sonnet-20240620',
        max_tokens=1000,
        temperature=0.1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )  
    return message.content[0].text