# https://docs.python.org/3/library/time.html#time.strftime
import time
hr = int(time.strftime('%H'))
min = int(time.strftime('%M'))
sec = int(time.strftime('%S'))
if(hr<12 and hr>1):
    print("Good Morning sir!")
elif(hr>12 and hr<17):
    print("Good Afternoon sir!")
elif(hr>17 and hr<20):
    print("Good Evening Sir!")
else:
    print("Good night sir")