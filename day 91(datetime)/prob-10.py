## converting string to date (strptime)

## it is used to convert string into datetime obj

## syntax
#  datetime.strptime(string,format)


## ex-1

from datetime import datetime
date_str="21-09-2005"
date_obj=datetime.strptime(date_str,"%d-%m-%Y")    
print(date_obj)



## PROB-2

from  datetime import datetime
d_string="2003-09-27"

s_obj = datetime.strptime(d_string, "%Y-%m-%d")
print(s_obj)