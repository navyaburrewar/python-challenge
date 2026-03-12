## formated date(strftime)

# syntax
## strftime


from datetime import datetime

present =datetime.now()
print(present.strftime("%d-%m-%y"))
print(present.strftime("%A-%B-%y"))

# Common Format Codes
# Code Meaning 
# %Y Full year 
# %m Month 
# %d Day
# %H Hour
# %M Minute 
# %S Second 
# %A Day name 
# %B Month name