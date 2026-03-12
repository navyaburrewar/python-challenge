## ACCESSING  individual attribute from date and time


from datetime import datetime

present =datetime.now()
print(present.year)
print(present.month)
print(present.day)
print(present.hour)
print(present.minute)
print(present.second)