# ### timestamp


# he time

# 🗓 Jan 1, 1970 — 00:00:00 UTC  ###################3

# is popularly called:
# ⏱ Unix Epoch

# or simply
# ⏱ Epoch Time
# 📖 Other Common Names

# People also call it:
# Unix Time Zero
# Epoch Start
# POSIX Epoch (in technical systems)




from datetime import datetime

dt = datetime(2025, 2, 21, 0, 0, 0)
print(dt.timestamp())




# What is the use of Unix Epoch / timestamps?

# Let’s keep it simple and practical.

# 🎯 Main Use

# Computers use timestamps to:
# ⏱ Store and calculate time easily using numbers
# Instead of long date text.

# 💻 Why Computers Prefer Timestamps
# 1️⃣ Easy to Store

# Instead of:


# 21 February 2025, 10:30:45 AM
# Store:
# 1740114045

# Numbers take less space and are faster.

# 2️⃣ Easy to Compare Times
# 1740114045 > 1600000000

# ✔ Bigger number = later time
# Very fast for computers.

# 3️⃣ Easy Time Calculations
# ⏳ Find time difference
# End − Start = Seconds passed

# Used for:

# Video duration
# Task timers
# Download time
# Game timers

# 4️⃣ Works Worldwide 🌍

# Dates look different in different countries:

# Country	Format
# US	MM/DD/YYYY
# India	DD/MM/YYYY
# Japan	YYYY/MM/DD



# If timestamps count seconds after 1970,
# how do we represent dates before 1970?


# Answer: We Use Negative Timestamps

# Dates before
# 🗓 Jan 1, 1970 — 00:00:00 UTC
# are stored as negative seconds.

# After 1970 → Positive seconds

# Before 1970 → Negative seconds



