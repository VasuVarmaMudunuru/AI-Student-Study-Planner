import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2:3b",
    "prompt": "Explain artificial intelligence in 3 simple sentences.",
    "stream": False
}

response = requests.post(
    url,
    json=data
)

if response.status_code == 200:

    result = response.json()

    print("\n==============================")
    print("       AI RESPONSE")
    print("==============================\n")

    print(result["response"])

else:

    print("ERROR:", response.status_code)
    print(response.text)