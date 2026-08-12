import requests
import os

# Fireworks AI API Demo
# Powered by AMD GPU via Fireworks

API_KEY = os.getenv("FIREWORKS_API_KEY")
url = "https://api.fireworks.ai/inference/v1/chat/completions"

payload = {
  "model": "accounts/fireworks/models/llama-v3-8b-instruct",
  "messages": [{"role": "user", "content": "Hello!"}],
  "max_tokens": 256
}
headers = {
  "Authorization": f"Bearer {API_KEY}",
  "Content-Type": "application/json"
}

if __name__ == "__main__":
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
