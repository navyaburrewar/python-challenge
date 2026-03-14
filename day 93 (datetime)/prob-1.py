### practical programs

## age calculator
from datetime import datetime

birth = datetime(2005,9,21)
today=datetime.now()

age =today -birth

print(age.days//365 )