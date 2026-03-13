## 11 days
## 11 . weekdays functions

# 1️⃣ weekday() Method
# ✅ What it does

# Returns the day of the week as a number (0–6)

# Number	Day
# 0	Monday
# 1	Tuesday
# 2	Wednesday
# 3	Thursday
# 4	Friday
# 5	Saturday
# 6	Sunday


## weekday()

import datetime

day = datetime.date(2025,2,2)
print(day.weekday())




## another method

# 2️⃣ isoweekday() Method (Very Similar)

# This one follows ISO standard numbering.

# Number	Day
# 1	Monday
# 2	Tuesday
# 3	Wednesday
# 4	Thursday
# 5	Friday
# 6	Saturday
# 7	Sunday



## isoweekday()

import datetime
day = datetime.date(2025,9,21)
print(day.isoweekday())


