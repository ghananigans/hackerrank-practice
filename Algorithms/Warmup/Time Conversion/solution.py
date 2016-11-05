#!/bin/python3

time = input().strip()

if time[-2:] == "AM":
    print("%02d%s" % (int(time[:2]) % 12, time[2:-2]))
elif time[-2:] == "PM":
    print("%02d%s" % ((int(time[:2]) % 12) + 12, time[2:-2])) 
else:
    assert(False)

