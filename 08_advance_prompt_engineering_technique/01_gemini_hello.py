from google import genai

client = genai.Client(api_key='AIzaSyD6SyviFAWU9NbY3iXtlYeWnf0UD2PP1uE')

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)