import requests
import os 
from datetime import datetime
import json 

url="https://api.thedogapi.com/v1/breeds"
Api_key="live_G55XQ1EeiV80ppVIOrrThgvw6GKemZiwkd7A65e5TJn5BiF41zkAGPJZGwXuB9jZ"

hearders={
   "x-api-key": Api_key
}

response = requests.get(url,headers=hearders)
data = response.json() 

# Create folder
os.makedirs("data", exist_ok=True)

# Save file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filepath = f"data/dogs_{timestamp}.json"

with open(filepath, "w") as f:
    json.dump(data, f)

print("Saved:", filepath)