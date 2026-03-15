# 2️⃣ Specific Date Creation

# Create a datetime object for:

# 15 August 2027, 10:30:00 AM
# Print it in format: DD-MM-YYYY HH:MM:SS



from datetime import datetime

dt =datetime(2027,8,15,15,13,1)

print(dt.strftime("%d-%m-%y %H:%M:%S"))