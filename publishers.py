import json
import os
import time
import random 
from paho.mqtt import client as mqtt_client

#TCP Connection
broker = 'mosquitto' #οριστηκε στο docker-compose
port = 1883 #standard mqtt port 
topic = "publishers/data" #προσωρινος φακελος που στελνονται οι μετρησεις απο sensors
device_name = os.environ.get('DEVICE_NAME') #διαβαζει ονομα sensor απο το docker-compose ('DEVICE_NAME')
client_id = f'python-mqtt-{device_name}' # ονομα συνδεσης broker , mqtt id 