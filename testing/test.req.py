import requests
import json

data = requests.put("http://127.0.0.1:5000/user/signup/", { "usern": json.dumps({ "email": "linus.bolls@code.berlinn", "name": 5 }) })
print(data.json())