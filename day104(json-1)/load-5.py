## using of load ..



import json


data = {"name": "John"}

# Save data
with open("data.json", "w") as f:
    json.dump(data, f)

# Read data
with open("data.json", "r") as f:
    x = json.load(f)

print(x)