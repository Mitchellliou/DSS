#!/user/bin/env python

import serial
import re

int value_count = 0

def filter(distance, value_count): 
    int last_value = 0
    if value_count == 0:
        last_value = distance
        value_count = value_count + 1
    else if (last_value == distance)
        if value_count == 5:
            print("Consistent reading: " + distance)
            return distance
        value_count = value_count + 1

    



ser = serial.Serial('/dev/ttyACM0', 9600)
while 1: 
    if(ser.in_waiting >0):
        line = ser.readline()
        line_decode = line.decode('utf-8')
        distance = re.search(r'\d+', line_decode)
        # print(type(distance))
        if(distance != None):
            int i = 0
            print(distance.group())
        # print(distance)
        
