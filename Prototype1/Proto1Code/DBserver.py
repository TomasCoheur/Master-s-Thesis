import mysql.connector
import paho.mqtt.client as mqtt
import time

# MySQL database initialization
mysql_host = "localhost"  # Change this to your MySQL server's address
mysql_user = "remotepc"  # Change this to your MySQL username
mysql_password = "arduino"  # Change this to your MySQL password
mysql_database = "arduino"  # Change this to your MySQL database name

# Create MySQL connection
conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
cursor = conn.cursor()

# MQTT broker settings
mqtt_broker = "localhost"  # Change this to your MQTT broker's address
mqtt_port = 1883
mqtt_topics = ["humidity", "temperature"]  # Change this to the topics you want to subscribe to

humidity_payload = 0
temp_payload = 0

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    for topic in mqtt_topics:
        client.subscribe(topic)

# MQTT on_message callback
def on_message(client, userdata, msg):
    global humidity_payload, temp_payload
    counter = 0
    ts = time.time()
    print(msg.topic+" "+str(msg.payload))
    # Insert data into MySQL database
    try:
        payload = float(msg.payload.decode('utf-8'))
    except ValueError:
        print("Invalid float value received:", msg.payload.decode('utf-8'))
        return

    if msg.topic == "humidity":
        humidity_payload = payload
        insert_query = "INSERT INTO Sensors (time, humidity, temperature) VALUES (%s, %s, %s)"
    elif msg.topic == "temperature":
        temp_payload = payload
        insert_query = "INSERT INTO Sensors (time, humidity, temperature) VALUES (%s, %s, %s)"

    data = (ts, humidity_payload, temp_payload)
    cursor.execute(insert_query, data)
    conn.commit()

# Create MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start MQTT client loop
client.loop_forever()
