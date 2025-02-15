import requests
import json

# Ensure your API key is set
AIPROXY_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjEwMDAwNDlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.s-L9I8TWJNaiGEbyobc_b_z0U759xnzHu7nrDVfMZms" # Replace with a valid API key

if not AIPROXY_TOKEN or AIPROXY_TOKEN == "your_actual_api_key_here":
    print("❌ ERROR: API Key is missing or incorrect!")
    exit()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AIPROXY_TOKEN}",
}

response = requests.get("http://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers)
print(f"API Response: {response.status_code} {response.json()}")
