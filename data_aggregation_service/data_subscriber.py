import json
import time
import paho.mqtt.client as mqtt_client


class DataSubscriber:

    def __init__(self, instance_id, host, port, topic, username, password=""):

        mqtt_client.Client.connected_flag = False
        mqtt_client.Client.suppress_puback_flag = False

        self.mqttClientInstance = mqtt_client.Client(instance_id)
        self.mqttClientInstance.on_connect = self.on_connect
        self.mqttClientInstance.on_disconnect = self.on_disconnect
        self.mqttClientInstance.on_log = self.on_log
        self.mqttClientInstance.on_publish = self.on_publish
        self.mqttClientInstance.on_message = self.on_message
        self.mqttClientInstance.username_pw_set(username, password)
        self.broker = host
        self.port = port
        self.topic = topic

    @staticmethod
    def on_log(client_instance, user_data, logging_level, buffer):
        print(logging_level, "| Log: ", buffer)

    @staticmethod
    def on_connect(client_instance, user_data, flags, return_code):
        if return_code == 0:
            client_instance.connected_flag = True
            print("Client is connected.")
        else:
            print("Error upon connection.")
            print("Return code: ", return_code)
            client_instance.loop_stop()

    @staticmethod
    def on_disconnect(client_instance, user_data, flags, result_code=0):
        print("Client has been disconnected with result code: ", result_code)

    @staticmethod
    def on_message(client_instance, user_data, message):

        print("The received message: ", str(message.payload.decode("utf-8")))
        print("The topic: ", str(message.topic))
        print("The qos: ", str(message.qos))

        if message.retain == 1:
            print("This is a retained message.")

    @staticmethod
    def on_publish():
        print("Data has been published.")

    def connect(self):
        self.mqttClientInstance.connect(self.broker, self.port)

        while not self.mqttClientInstance.is_connected():
            self.mqttClientInstance.loop()
            time.sleep(1)

    def subscribe(self):

        self.mqttClientInstance.subscribe(self.topic)
