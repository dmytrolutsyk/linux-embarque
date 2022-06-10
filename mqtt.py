#!/usr/bin/env python

from datetime import datetime
import paho.mqtt.client as paho

broker="test.mosquitto.org"
port=1883

def date_format():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return(dt_string)

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def publish(message):
    date_format()
    client1= paho.Client("f")                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker, port)                                 #establish connection
    date = date_format()
    ret= client1.publish("esgi/smartlock/list",f"{message} -> {date}") 

if __name__ == '__main__':
    publish()
