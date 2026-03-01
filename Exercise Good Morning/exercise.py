# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

import time

local_time = int(input("Enter your local time: "))

if local_time >= 7 and local_time < 12:
    print("Good Morning")
elif local_time >= 13 and local_time < 17:
    print("Good Afternoon")
elif local_time >= 17 and local_time < 19:
    print("Good Evening")

else:
    print("Good Night")

timestamp = time.strftime("This is the local time of your local machine %A, %d %b %Y %H:%M:%S %p")
print(timestamp)
