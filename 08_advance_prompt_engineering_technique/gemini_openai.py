from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyD6SyviFAWU9NbY3iXtlYeWnf0UD2PP1uE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message.content) #cleaner
#print(response.choices[0].message) returns ChatCompletionMessage(content='..",refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)