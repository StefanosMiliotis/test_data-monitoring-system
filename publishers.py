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

def connect_mqtt(): #χρησιμοποιηθηκε paho-mqtt version 2 για υποστηριξη νεοτερων εκδοσεων mqtt
    # For paho-mqtt 2.0.0, you need to add the properties parameter.
    def on_connect(client, userdata, flags, rc, properties=None): #επιπλεον πληροφοριες απο broker , αν δεν στειλει θεωρησε none
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID    
    # For paho-mqtt 2.0.0, you need to set callback_api_version.
    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
