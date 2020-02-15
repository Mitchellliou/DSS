#!/user/bin/env python

import serial
import re

value_count = 0

def filter(distance, value_count): 
    last_value = 0
    
    # If first reading
    if last_value == 0:
        last_value = distance
        value_count = value_count + 1
        
    # If not first reading, and last value and current value are the same
    elif (last_value == distance):
        # If final reading, return
        if value_count == 5:
            print("Consistent reading: " + distance)
            value_count = 0
            return 
        # Otherwise, just increment counter
        value_count = value_count + 1
        print(value_count)
    
    # If not equal, then reset counter and set last value to current value
    else: 
        value_count = 0
        last_value = distance

    



ser = serial.Serial('/dev/ttyACM0', 9600)
while 1: 
    if(ser.in_waiting >0):
        line = ser.readline()
        line_decode = line.decode('utf-8')
        distance = re.search(r'\d+', line_decode)
        # print(type(distance))
        if(distance != None):
            filter(distance.group(), value_count)
            print(distance.group())
            print(value_count)
        # print(distance)
        
