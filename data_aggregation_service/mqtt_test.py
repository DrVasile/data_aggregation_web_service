import time

from data_subscriber import DataSubscriber


BROKER_HOST_ADDRESS = "mqtt.thingsboard.cloud"
BROKER_HOST_PORT = 1883
DEVICES_TELEMETRY_TOPIC = "v1/devices/me/attributes"
TOKEN_BUS_A = "BJC20mCMkNH0ZFlQXraX"
TOKEN_BUS_B = "DgBK86rUvy7Vmtw48qkl"
TOKEN_BUS_C = "rEMJIkcBXQaGAo8KphPL"
TOKEN_BUS_D = "epSC5PagsipnzBg7OEH4"
KEEP_ALIVE_TIME = 60

execution_flag = True


print("Creating the subscriber instance...")

mqtt_subscriber_a = DataSubscriber("bus-A", BROKER_HOST_ADDRESS, BROKER_HOST_PORT, DEVICES_TELEMETRY_TOPIC, TOKEN_BUS_A)

print("Connecting to the broker.")
mqtt_subscriber_a.connect()


print("Subscribing to a topic.")
mqtt_subscriber_a.subscribe()

while True:
    time.sleep(1)
