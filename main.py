# paho-mqtt tương thích tốt với nhiều server
print("AIoT Project")

import time
import sys
from Adafruit_IO import MQTTClient
from AI_Detection_Traffic_Signs import *

AIO_USERNAME = "Adafruit_Name"
AIO_KEY = "Adafruit_Key"

def connected(client):
    print("Ket noi thanh cong ...")

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

counter_ai = 1
ai_res = ""
prev_res = ""
accuracy = "0"
prev_accuracy = "0"

# while True:
#     counter_ai = counter_ai - 1
#     if counter_ai <= 0:
#         counter_ai = 1
#         prev_accuracy = accuracy
#         if int(prev_accuracy) >= 75:
#             prev_res = ai_res
#         new_state, ai_res, image, accuracy = image_detector()
#         print("AI Output: ", ai_res.strip() + " " + accuracy + "%")
#         change_history(ai_res.strip())
#         change_accuracy(accuracy)
#         change_traffic_sign(ai_res.strip())
#         if prev_res != ai_res and int(accuracy) >= 75:
#             # Publish data to Adafruit Server
#             client.publish("p.ai", ai_res)
#             client.publish("p.image", image)
#             client.publish("p.tile", accuracy + "%")
#             client.publish("ai", new_state)
#         # getkey_input(new_state)
#     time.sleep(1)
#     pass
