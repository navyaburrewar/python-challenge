## prob-2

## days remaining in year 


from datetime import datetime
future =datetime(2026,12,31)
today =datetime(2026,3,14)
remaining_days= future-today
print(remaining_days.days)




####   the below one gives the  complete date and time

from datetime import datetime
future =datetime(2026,12,31)
today =datetime.now()
remaining= future-today
print(remaining)