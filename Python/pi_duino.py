#!/user/bin/env python

import serial
import re
import firebase_admin
from firebase_admin import credentials, firestore

value_count = 0
last_value = 0
last_updated_value = 0

value_count_distance = 0
last_value_distance = 0
last_updated_value_distance = 0

def add_firebase_value(sensor_reading, input_string): 
    value_string = re.search(r'\w+', input_string).group()
    # value_string = "test"

    doc_ref = db.collection(u'User').document(u'KitchenShelf')
    doc_ref.update({
        value_string: str(sensor_reading)
    })
    print("Finished")

def filter_distance(sensor_reading, input_string): 
    global last_value_distance
    global value_count_distance
    global last_updated_value_distance
    # print("Distance last value: " + str(last_value_distance) + " Value_count: " + str(value_count_distance))

    # If first reading
    if last_value_distance == 0:
        last_value_distance = sensor_reading
        value_count_distance = value_count_distance + 1
        
    # If not first reading, and last value and current value are the same
    elif (last_value_distance == sensor_reading):
        # If final reading, return
        if value_count_distance == 5:
            print("Consistent Distance reading: " + sensor_reading)
            if(sensor_reading != last_updated_value_distance):
                add_firebase_value(sensor_reading, input_string)
                last_updated_value_distance = sensor_reading
                print("Uploaded Distance: " + sensor_reading)
            value_count_distance = 0
            return 
        # Otherwise, just increment counter
        value_count_distance = value_count_distance + 1
        # print(value_count)
    
    # If not equal, then reset counter and set last value to current value
    else: 
        value_count_distance = 0
        last_value_distance = sensor_reading

def filter_weight(sensor_reading, input_string): 
    global last_value
    global value_count
    global last_updated_value
    # print("weight last value: " + str(last_value) + " Value_count: " + str(value_count))

    # If first reading
    if last_value == 0:
        last_value = sensor_reading
        value_count = value_count + 1
        
    # If not first reading, and last value and current value are the same
    elif (last_value == sensor_reading):
        # If final reading, return
        if value_count == 5:
            print("Consistent Weight reading: " + sensor_reading)
            if(sensor_reading != last_updated_value):
                add_firebase_value(sensor_reading, input_string)
                last_updated_value = sensor_reading
                print("Uploaded Weight: " + sensor_reading)
            value_count = 0
            return 
        # Otherwise, just increment counter
        value_count = value_count + 1
        # print(value_count)
    
    # If not equal, then reset counter and set last value to current value
    else: 
        value_count = 0
        last_value = sensor_reading

last_value = 0
ser = serial.Serial('/dev/ttyACM0', 9600)

cred = credentials.Certificate("./ServiceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

while 1: 
    if(ser.in_waiting >0):
        line = ser.readline()
        line_decode = line.decode('utf-8')
        input_string = re.search(r'\d+', line_decode)
        determine = re.search(r'\w+', line_decode).group()

        # print(type(sensor_reading))
        # print(determine)
        if(input_string != None):
            if(determine == 'Distance'):
                filter_distance(input_string.group(), line_decode)
            else: 
                filter_weight(input_string.group(), line_decode)
            # print(sensor_reading.group())()
            # print(value_count)
        # print(sensor_reading)
        
