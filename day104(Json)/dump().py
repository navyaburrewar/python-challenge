## important differencess

# | Function | Use                  |
# | -------- | -------------------- |
# | dumps()  | Python → JSON string |
# | dump()   | Python → JSON file   |
# | loads()  | JSON string → Python |
# | load()   | JSON file → Python   |





# ##data types mapping

# | Python     | JSON       |
# | ---------- | ---------- |
# | dict       | object     |
# | list       | array      |
# | str        | string     |
# | int/float  | number     |
# | True/False | true/false |
# | None       | null       |


# # 1. What is json.dump()?
# 👉 Meaning:
# Python object → JSON file
# It writes data into a file

# 🧠 Think like:
# “I have Python data, I want to store it in a file in JSON format”

import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)


## atomatically a file is created here 
## the file anme is that data.json
## dont not show any thing in the output screen 



# ## advantages of this thing here are:
# ##json = save
# #  shares 
# # reuse data



################### 🔥 Applications of json.dump()$#############################

# 1. 💾 Saving user data
# Store user info like:
# name, age, email

# Example use:

# Registration system saves user details
# 2. 🎮 Saving game progress
# Store:
# score
# level
# coins

# 👉 So when user opens game again → progress is not lost




# 3. ⚙️ Storing settings / configuration

# Apps save settings like:

# {
#   "theme": "dark",
#   "volume": 80
# }

# 👉 Next time app opens → same settings applied



# 4. 📊 Storing program results
# Save output of a program

# Example:

# Student marks
# Report data
# Analysis results


# 5. 🔄 Data exchange (APIs / Web)
# Send data from Python → web server

# 👉 JSON is standard format for communication



# 6. 🗂️ Simple database replacement
# Instead of using database:
# use JSON file to store data

# Good for:

# small projects
# beginners


# 7. 📝 Logging information
# Save logs like:
# errors
# events
# activity history



# 🧠 Real-life flow
# User gives data
# ↓
# Program processes
# ↓
# json.dump() saves it in file
# ↓
# Later → json.load() reads it