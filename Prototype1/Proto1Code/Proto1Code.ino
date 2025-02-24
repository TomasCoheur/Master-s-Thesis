#include <ArduinoMqttClient.h>
#include <WiFiNINA.h>
#include "arduino_secrets.h"
#include <Arduino_MKRIoTCarrier.h>

MKRIoTCarrier carrier;

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = "IP of the Raspberry Pi"; // insert here the IP address of your Rasperry Pi
int        port     = 1883;
const char topic1[]  = "temperature";
const char topic2[]  = "humidity";

//set interval for sending messages (milliseconds)
const long interval = 5000;
unsigned long previousMillis = 0;

int count = 0;

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  CARRIER_CASE = false;
  carrier.begin();
  carrier.display.setRotation(0);

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();
}

void loop() {
  // call poll() regularly to allow the library to send MQTT keep alive which
  // avoids being disconnected by the broker
  mqttClient.poll();

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time a message was sent
    previousMillis = currentMillis;

    float celsius = carrier.Env.readTemperature();
    float fahrenheit = (celsius * 1.8) + 32;

    Serial.print("Sending message to topic: ");
    Serial.println(topic1);
    Serial.print("celsius: ");
    Serial.print(celsius);
    Serial.println("C");

    float recorded_humidity = carrier.Env.readHumidity();

    Serial.print("Sending message to topic: ");
    Serial.println(topic2);
    Serial.print("humidity: ");
    Serial.print(recorded_humidity);
    Serial.println("%");

    // send message, the Print interface can be used to set the message contents
    mqttClient.beginMessage(topic1);
    mqttClient.print(celsius);
    mqttClient.endMessage();

    mqttClient.beginMessage(topic2);
    mqttClient.print(recorded_humidity);
    mqttClient.endMessage();

    Serial.println();
  }
}
