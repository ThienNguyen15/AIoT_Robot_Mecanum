print("AIoT Project")
# paho-mqtt tương thích tốt với nhiều server

import random
import time
import sys
from Adafruit_IO import MQTTClient
from AI_Detection_Traffic_Signs import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"] # 2 topics
AIO_USERNAME = "Adafruit_Name"
AIO_KEY = "Adafruit_Key"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
sensor_type = 0 # ...
counter_ai = 5
ai_res = ""
prev_res = ""
while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        #TODO
        print("Random data publishing...")
        if sensor_type == 0:
            print("Updating temperature...")
            temp = random.randint(0, 50)
            client.publish("cambien1", temp)
            sensor_type = 1
        elif sensor_type == 1:
            print("Updating light...")
            light = random.randint(0, 30000)
            client.publish("cambien2", light)
            sensor_type = 2
        elif sensor_type == 2:
            print("Updating humidity...")
            humi = random.randint(0, 100)
            client.publish("cambien3", humi)
            sensor_type = 0

    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        prev_res = ai_res
        ai_res, image, accuracy = image_detector()
        print("AI Output: ", ai_res.strip() + " " + accuracy)
        if prev_res != ai_res:
            client.publish("ai", ai_res)

        client.publish("tile", accuracy)
        client.publish("image", image)

    time.sleep(1)
    pass
