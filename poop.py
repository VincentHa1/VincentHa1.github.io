import json

number = 123
data = {"number": number}

with open("data.json", "w") as f:
    json.dump(data, f)
