import requests
import os 
from datetime import datetime
import json 

url="https://api.thecatapi.com/v1/breeds"
Api_key="you have to register so the send api key by email "

hearders={
   "x-api-key": Api_key
}

response = requests.get(url,headers=hearders)
data = response.json() 

# Create folder
os.makedirs("data", exist_ok=True)

# Save file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filepath = f"data/cat_{timestamp}.json"

with open(filepath, "w") as f:
    json.dump(data, f)

print("Saved:", filepath)