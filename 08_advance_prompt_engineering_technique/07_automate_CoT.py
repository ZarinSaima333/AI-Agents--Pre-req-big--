# #deepseek etc use this cause they think before writing.

# from dotenv import load_dotenv
# import os
# import json

# load_dotenv() 
# API_KEY = os.getenv("GOOGLE_API_KEY")

# # Optional safety check
# if not API_KEY:
#     raise ValueError("GOOGLE_API_KEY not found. Did you create a .env file?")
# from openai import OpenAI

# client = OpenAI(
#     api_key=API_KEY,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )


# SYSTEM_PROMT='''
#     You're an expert AI assistant in resolving user queries using chain of thought.
#     You work on START, PLAN and OUTPUT steps.
#     You need to first PLAN has been done,finally you can give an OUTPUT.

#     Rules:
#     -Strictly follow the given JSON output format
#     -Only run one step at a time.
#     _The sequence of steps in START (where user gives an input), PLAN(That can
#     be multiple times) and ,finally OUTPUT (which is going to the displayed to the user).

#     Output JSON Format:
#     {'step':'START'|"PLAN"|"OUTPUT",'content':'string'}

#     Example:
#     Q: Start: hey, can you solve 2+3*5/10
#     PLAN:{'step':"PLAN":"content":"Seems like user is interested in math problem"}
#     PLAN:{'step':"PLAN":"content":"Looking at the problem we can use BODMAS method"}
#     PLAN:{'step':"PLAN":"content":"Yes, BODMAS is the correct thing to be done here"}
#     PLAN:{'step':"PLAN":"content":"First, we multiple 3*5 which is 15 "}
#     PLAN:{'step':"PLAN":"content":"Now the equationis 2+15/10"}
#     PLAN:{'step':"PLAN":"content":"We must perform devide that is 15/10=1.5"}
#     PLAN:{'step':"PLAN":"content":"Now new equation is 2+1.5"}
#     PLAN:{'step':"PLAN":"content":"Now finally lets perform the addition which is 3.5"}
#     PLAN:{'step':"PLAN":"content":"Great now we have solved and finalize 3.5 as ans"}
#     PLAN:{'step':"OUTPUT":"content":"3.5"}
# '''

# print('/n/n/n')

# message_history=[
#     {'role':'system',
#      'content':SYSTEM_PROMT}
# ]

# user_query = input("👉🏻")

# message_history.append({'role':'system',
#      'content':user_query})

# while True:
#     response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type":"json_object"},
#     messages=message_history
#     )

#     raw_result =(response.choices[0].message.content)
#     message_history.append({'role':'user',
#      'content':raw_result})
#     parsed_result=json.loads(raw_result)

#     if parsed_result.get('step')=='START':
#         print("🔥",parsed_result.get('content'))
#         continue

#     if parsed_result.get('step')=='PLAN':
#         print("🧠",parsed_result.get('content'))
#         continue

#     if parsed_result.get('step')=='OUTPUT':
#         print("✅",parsed_result.get('content'))
#         break

# print('/n/n/n')  
# 07_automate_CoT_fixed.py
from dotenv import load_dotenv
import os
import json
from openai import OpenAI

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please create a .env file with your key.")

# Initialize Gemini client
client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# System prompt with CoT instructions
SYSTEM_PROMPT = '''
You're an expert AI assistant in solving user queries using Chain of Thought (CoT).
Follow these steps: START → PLAN → OUTPUT.
- Only run one step at a time.
- Output must strictly follow this JSON format:
  {"step": "START"|"PLAN"|"OUTPUT", "content": "string"}

Example:
Q: hey, can you solve 2+3*5/10
Response:
{"step":"START","content":"Solving 2+3*5/10"}
{"step":"PLAN","content":"Use BODMAS: first multiply 3*5 = 15"}
{"step":"PLAN","content":"Then divide 15/10 = 1.5"}
{"step":"PLAN","content":"Now add 2 + 1.5 = 3.5"}
{"step":"OUTPUT","content":"3.5"}
'''

# Ask user for a math expression
math_expr = input("👉🏻 Enter a math expression to solve: ")

# Create the chat completion request
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},  # Ensures JSON output
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": math_expr}
    ]
)

# # Print the model's JSON response
print("\nModel Output:\n")
print(response.choices[0].message.content)

# 👉🏻 Enter a math expression to solve: hey can you solve 2+3/10*6*4/1-50

# Model Output:

# {"step":"START","content":"Solving 2+3/10*6*4/1-50"}
# {"step":"PLAN","content":"First perform division/multiplication from left to right: 3/10 = 0.3"}
# {"step":"PLAN","content":"Next, multiply 0.3 * 6 = 1.8"}
# {"step":"PLAN","content":"Then, multiply 1.8 * 4 = 7.2"}
# {"step":"PLAN","content":"After that, divide 7.2 / 1 = 7.2"}
# {"step":"PLAN","content":"Now, perform addition/subtraction from left to right: 2 + 7.2 = 9.2"}
# {"step":"PLAN","content":"Finally, subtract 9.2 - 50 = -40.8"}
# {"step":"OUTPUT","content":"-40.8"}