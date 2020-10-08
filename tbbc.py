# tbbc.py
import time
import requests

# Get key from apikey.txt
key = ""
with open("apikey.txt","r") as f:
    key = f.readline().strip()

# Test if it works
url = "https://osu.ppy.sh/p/api/get_user_best"
params = {"k": key, "u": 2188855, "m": 0, "limit": 10, "type": "id"}

resp = requests.get(url, params)
data = resp.json()

print(data)

# Main loop
while True:

    time.sleep(2) # Avoid spamming requests
