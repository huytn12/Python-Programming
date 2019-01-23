#!/usr/bin/env python3.6

message = input("Please enter a message!")
count = input("Number of repeats [1]: ").strip()

if count:
    count = int(count)
else:
    count = 1

def printMessage(message, count):
    while count > 0:
        print(message)
        count -= 1

printMessage(message,count)



