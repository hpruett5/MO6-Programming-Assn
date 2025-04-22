import datetime
from datetime import date

#13.1 

now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now_str, file=output)

#13.2
with open('today.txt','rt') as input:
    today_string = input.read()

print (today_string)

#13.3 
import time
fmt = "%Y-%m-%d\n"
print(time.strptime(today_string,fmt))
