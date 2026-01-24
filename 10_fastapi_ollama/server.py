from fastapi import FastAPI,Body
from ollama import Client

app = FastAPI()
client= Client(
    host='http://localhost:11434/'
)

@app.get("/")
async def read_root():
    return {'hello':'world'}

@app.get('/contact-us')
async def read_root():
    return {'zarin':'zarin.saima@gmail.com '}
@app.post('/chat')
async def chat(message: str = Body(..., description="The Message")):
    response = client.chat(
        model='gemma2:2b',
        messages=[{'role': 'user', 'content': message}]
    )
    return {'response': response.message.content}