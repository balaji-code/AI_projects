import os
from dotenv import load_dotenv
import requests

# Load your API key
load_dotenv()
api_key = os.getenv('X_AI_API_KEY')

# Set up the request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# What you want to ask the AI
data = {
    'model': "grok-beta",
    "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "write a poem about todays weather"
    }
  ],
}

# Send the request
response = requests.post(
    'https://api.x.ai/v1/chat/completions',
    headers=headers,
    json=data
)

# Get the response
if response.status_code == 200:
    # Print the AI's response
    print(response.json()['choices'][0]['message']['content'])
else:
    print('Error:', response.text)

