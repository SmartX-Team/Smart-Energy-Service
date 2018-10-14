import threading, logging, time
import multiprocessing
import msgpack

from kafka import TopicPartition
from kafka import KafkaConsumer
from kafka.errors import KafkaError

import requests, json
import time
import os
import sys
import subprocess
import urllib, urllib2

from time import localtime, strftime



cmd ="curl -XPOST 'http://localhost:8086/query' --data-urlencode 'q=CREATE DATABASE 'Sensordata''"
subprocess.call([cmd], shell=True)

cmd ="curl -XPOST 'http://localhost:8086/query' --data-urlencode 'q=CREATE DATABASE 'Weather''"
subprocess.call([cmd], shell=True)

timeout = 100
actual_data=[]

consumer = KafkaConsumer('Device1', bootstrap_servers=['localhost:9091'])
partitions = consumer.poll(timeout)
while partitions == None or len(partitions) == 0:

        consumer = KafkaConsumer('Device1', bootstrap_servers=['localhost:9091'])
        message = next(consumer)
        print(message.value)

        str1 = message.value
        str2 = str1.split(',')
        device_name = str2[0]
        str4 = str2[1]
        str5 = str2[2]
        str6 = str2[3]
        str4 = str4.split(' ')
        time_val = str4[1]
        str5 = str5.split(' ')
        temperature = str5[1]
        str6 = str6.split(' ')
        humidity = str6[1]

        device_name2 = device_name.split(':')
        device_name = device_name2[1]

        time_val2 = time_val.partition(':')
        time_val = time_val2[2]

        temperature2 = temperature.split(':')
        temperature = temperature2[1]

        humidity2 = humidity.split(':')
        humidity = humidity2[1]

        #variables = "dev1"
        Aircon_temp = '18'
        #cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Sensordata' --data-binary 'dev1_temperature, value=%s\ndev1_humidity, value=%s\next_temperature, value=%s\next_humidity, value=%s\nAircon_temp, value=%s'" % (temperature, humidity, Aircon_temp)
        #cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Sensordata' --data-binary 'dev1_temperature,host=host1 value=%s\ndev1_humidity,host=host1 value=%s\nAircon_temp,host=host1 value=%s'" % (temperature, humidity, Aircon_temp)
        #cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Sensordata' --data-binary 'dev1,host=host1 field key=temperature, field value=%s, field key=humidity, field value=%s, field key=Aircon_temp field value=%s'" % (temperature, humidity, Aircon_temp)
        #cmd = "curl -i -XPOST 'http://localhost:8086/query?db=Sensordata' --data-urlencode 'q=SELECT * INTO 'temperature' FROM 'temperature'"
        #{"results":[{"statement_id":0,"series":[{"name":"result","columns":["time","written"],"values":[["1970-01-01T00:00:00Z",2]]}]}]}
        cmd = "curl -XPOST 'http://localhost:8086/write?db=Sensordata' --data-binary 'dev1,location=Gwangju temperature=%s,humidity=%s,Aircon_temp=%s'" % (temperature, humidity, Aircon_temp)
        subprocess.call([cmd], shell=True)


        #variables = "dev1"
        #cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Sensordata' --data-binary '%s,host=%s,region=Gwangju_tower_room1 value=%s\n%s,host=Aircon_temp,region=Gwangju_tower_room1 value=%s'" % (variables, device_name, humidity, variables, Aircon_temp)
        #subprocess.call([cmd], shell=True)

        #variables = "Aircon_temp"
        #cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Sensordata' --data-binary 'Aircon_temp,region=Gwangju %s=\"%s\"'" % (variables, weather_stat)
