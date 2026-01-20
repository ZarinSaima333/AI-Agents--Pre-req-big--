#deepseek etc use this cause they think before writing.

from dotenv import load_dotenv
import os
import json
load_dotenv() 
API_KEY = os.getenv("GOOGLE_API_KEY")

# Optional safety check
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Did you create a .env file?")
from openai import OpenAI

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMT='''
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN has been done,finally you can give an OUTPUT.

    Rules:
    -Strictly follow the given JSON output format
    -Only run one step at a time.
    _The sequence of steps in START (where user gives an input), PLAN(That can
    be multiple times) and ,finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    {'step':'START'|"PLAN"|"OUTPUT",'content':'string'}

    Example:
    Q: Start: hey, can you solve 2+3*5/10
    PLAN:{'step':"PLAN":"content":"Seems like user is interested in math problem"}
    PLAN:{'step':"PLAN":"content":"Looking at the problem we can use BODMAS method"}
    PLAN:{'step':"PLAN":"content":"Yes, BODMAS is the correct thing to be done here"}
    PLAN:{'step':"PLAN":"content":"First, we multiple 3*5 which is 15 "}
    PLAN:{'step':"PLAN":"content":"Now the equationis 2+15/10"}
    PLAN:{'step':"PLAN":"content":"We must perform devide that is 15/10=1.5"}
    PLAN:{'step':"PLAN":"content":"Now new equation is 2+1.5"}
    PLAN:{'step':"PLAN":"content":"Now finally lets perform the addition which is 3.5"}
    PLAN:{'step':"PLAN":"content":"Great now we have solved and finalize 3.5 as ans"}
    PLAN:{'step':"OUTPUT":"content":"3.5"}
'''

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {   "role": "system", #special instruction
            "content": SYSTEM_PROMT
        },
        {
            "role": "user",
            "content": "write me a code to add n numbers in python"
        },
        {
            "role": "assistant",
            "content": json.dumps({"step":"START","content":"You want a python code to add 'n' numbers."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "The user is asking for a Python code to sum 'n' numbers."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "I will define a Python function that takes a list of numbers as input."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "Inside the function, I'll initialize a sum variable to 0 and iterate through the input list, adding each number to the sum."})
        },
         {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "Finally, the function will return the calculated sum."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "I will also provide an example of how to use this function."})
        }
        
    ]
)

print(response.choices[0].message.content) #cleaner
#print(response.choices[0].message) returns ChatCompletionMessage(content='..",refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)

# {{
# "code":"SELECT * FROM table_name;",
# "iscodingquestion":true}}

#{"step": "OUTPUT", "content": "```python\ndef add_n_numbers(numbers):\n    \"\"\"\n    Adds a list of 'n' numbers.\n\n    Args:\n        numbers (list or tuple): A list or tuple of numbers (integers or floats).\n\n    Returns:\n        int or float: The sum of the numbers.\n    \"\"\"\n    total = 0\n    for number in numbers:\n        total += number\n    return total\n\n# Example usage:\nif __name__ == \"__main__\":\n    # Example 1: Adding a list of integers\n    my_list_of_ints = [1, 2, 3, 4, 5]\n    sum_of_ints = add_n_numbers(my_list_of_ints)\n    print(f\"The sum of {my_list_of_ints} is: {sum_of_ints}\") # Expected output: 15\n\n    # Example 2: Adding a list of floats\n    my_list_of_floats = [10.5, 20.0, 3.5, 6.0]\n    sum_of_floats = add_n_numbers(my_list_of_floats)\n    print(f\"The sum of {my_list_of_floats} is: {sum_of_floats}\") # Expected output: 40.0\n\n    # Example 3: Adding an empty list\n    empty_list = []\n    sum_of_empty = add_n_numbers(empty_list)\n    print(f\"The sum of {empty_list} is: {sum_of_empty}\") # Expected output: 0\n\n    # Example 4: Using a tuple\n    my_tuple = (7, 8, 9)\n    sum_of_tuple = add_n_numbers(my_tuple)\n    print(f\"The sum of {my_tuple} is: {sum_of_tuple}\") # Expected output: 24\n\n    # Python's built-in sum() function is often more concise for this purpose:\n    print(f\"\\nUsing built-in sum(): sum({my_list_of_ints}) = {sum(my_list_of_ints)}\")\n    print(f\"Using built-in sum(): sum({my_list_of_floats}) = {sum(my_list_of_floats)}\")\n```"}