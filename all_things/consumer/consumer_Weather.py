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


cmd ="curl -XPOST 'http://localhost:8086/query' --data-urlencode 'q=CREATE DATABASE 'Weather''"
subprocess.call([cmd], shell=True)

timeout = 100
actual_data=[]

consumer = KafkaConsumer('weather', bootstrap_servers=['localhost:9091'])
partitions = consumer.poll(timeout)
while partitions == None or len(partitions) == 0:

        consumer = KafkaConsumer('weather', bootstrap_servers=['localhost:9091'])
        message = next(consumer)
        print(message.value)

        str1 = message.value
        str2 = str1.split(',')
        weather_stat = str2[0]
        str4 = str2[1]
        str5 = str2[2]
        str6 = str2[3]
        str4 = str4.split(' ')
        time_val = str4[1]
        str5 = str5.split(' ')
        temperature = str5[1]
        str6 = str6.split(' ')
        humidity = str6[1]

        weather_stat2 = weather_stat.split(':')
        weather_stat = weather_stat2[1]

        time_val2 = time_val.partition(':')
        time_val = time_val2[2]

        temperature2 = temperature.split(':')
        temperature = temperature2[1]

        humidity2 = humidity.split(':')
        humidity = humidity2[1]

        variables = "temperature"
        cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Weather' --data-binary '%s,host=weather,region=Gwangju_outdoor value=%s'" % (variables, temperature)
        subprocess.call([cmd], shell=True)

        variables = "humidity"
        cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Weather' --data-binary '%s,host=weather,region=Gwangju_outdoor value=%s'" % (variables, humidity)
        subprocess.call([cmd], shell=True)

        variables = "weather_stat"
        cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Weather' --data-binary 'weather,region=Gwangju %s=\"%s\"'" % (variables, weather_stat)
        #cmd = "curl -i -XPOST 'http://localhost:8086/write?db=Weather' --data-urlencode 'chunked=true' --data-urlencode 'chunk_size=20000' --data-urlencode '%s,host=weather,region=Gwangju value=%s'" % (variables, weather_stat)
        #cmd = "curl -i -XPOST 'http://localhost:8086/query' --data-urlencode 'db=Weather' --data-urlencode 'chunked=true' --data-urlencode 'chunk_size=20000' --data-urlencode 'q=SELECT * FROM weather' "
              #"  '%s,host=weather,region=Gwangju_outdoor value=%s'" % (variables, weather_stat)
        subprocess.call([cmd], shell=True)




