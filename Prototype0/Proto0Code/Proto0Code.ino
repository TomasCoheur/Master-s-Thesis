/*
 *  Simple HTTP get webclient test
 */
#include "config.h"

#include <Arduino_MKRIoTCarrier.h>

MKRIoTCarrier carrier;

// set up the 'temperature' and 'humidity' feeds
AdafruitIO_Feed *temperature = io.feed("temperature");
AdafruitIO_Feed *humidity = io.feed("humidity");

void setup() {
  Serial.begin(9600);
  delay(100);

  delay(500);
  CARRIER_CASE = false;
  carrier.begin();
  carrier.display.setRotation(0);

  // connect to io.adafruit.com
  Serial.print("Connecting to Adafruit IO");
  io.connect();

  // wait for a connection
  while(io.status() < AIO_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  // we are connected
  Serial.println();
  Serial.println(io.statusText());
}

void loop() {

  io.run();

  float celsius = carrier.Env.readTemperature();
  float fahrenheit = (celsius * 1.8) + 32;

  Serial.print("celsius: ");
  Serial.print(celsius);
  Serial.println("C");

  Serial.print("fahrenheit: ");
  Serial.print(fahrenheit);
  Serial.println("F");
  
  // save fahrenheit (or celsius) to Adafruit IO
  temperature->save(celsius);

  float recorded_humidity = carrier.Env.readHumidity();

  Serial.print("humidity: ");
  Serial.print(recorded_humidity);
  Serial.println("%");

  // save humidity to Adafruit IO
  humidity->save(recorded_humidity);

  // wait 5 seconds (5000 milliseconds == 5 seconds)
  delay(5000);
}
