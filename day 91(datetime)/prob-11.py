# ## timedelta

# ## time delta which is nothing but data calculations
# ## which will find differnce b/w 2 dates


# Think of timedelta = a time gap

# It represents a duration like:

# number of days
# hours
# minutes
# seconds
# You use it to do date math ➕➖


# ## add days to todays(future date)

# from datetime import datetime,timedelta

# today =datetime.now()
# future = today+timedelta(days =10)

# print(future)



## prob-2  ### printing two days back date

# from datetime import datetime ,timedelta
# tommorow = "2005-09-21"

# d_obj=datetime.strptime(tommorow, "%Y-%m-%d" )

# yesturday = d_obj-timedelta(days=2)
# print(yesturday)



##  subtract two dates (find difference)


from datetime import datetime,timedelta

d1=datetime(2005,9,21)
d2=datetime(2003,9,27)

diff=d1-d2
print(diff)