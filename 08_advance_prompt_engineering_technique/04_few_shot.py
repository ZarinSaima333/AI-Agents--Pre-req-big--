# 1️⃣ Load environment variables FIRST
from dotenv import load_dotenv
import os
#from ..env import GOOGLE_API_KEY wrong cz not a python file.
load_dotenv() #eki directory te na rakhleo eka khuje ber kore env

API_KEY = os.getenv("GOOGLE_API_KEY")

# Optional safety check
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Did you create a .env file?")
from openai import OpenAI

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
#Zero shot prompting directly giving the ins to the model

SYSTEM_PROMT='''You should only and only answer the coding related questions. DO not answer anything else./' \
'your name is RozaAI. If user asks soemthing other than coding just say sorrryy:(
Q:Can you explain the a+b whole square?
A: Sorry, I can only help you with coding related questions.

Q:Hey, write a code in python for adding two numbers

def add(a,b):
    return a+b

'''

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   "role": "system", #special instruction
            "content": SYSTEM_PROMT
        },
        {
            "role": "user",
            "content": "td3net, have you heard about this ML architecture?"
        }
    ]
)

print(response.choices[0].message.content) #cleaner
#print(response.choices[0].message) returns ChatCompletionMessage(content='..",refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)

