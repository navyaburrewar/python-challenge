# Add Days to Date Take today’s date 
# and print the date after 100 days.

from datetime import datetime,timedelta

today =datetime.today().date()

days =100
coming_dates =today +timedelta(days=days)
print(coming_dates)