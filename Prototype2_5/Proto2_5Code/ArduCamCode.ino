#include <WiFi.h>
#include <HTTPClient.h>
#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include "ArduCAM.h"

// WiFi credentials
const char* ssid = "YourWiFiSSID";
const char* password = "YourWiFiPassword";

// Server details
const char* serverName = "www.example.com";
const int serverPort = 80;
const String uploadUrl = "/upload";

// Arducam settings
ArduCAM camera(OV7670, SS);
uint8_t vid, pid;

// SD card settings
const int chipSelect = 5; // SD card chip select pin
File imageFile;

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Initialize SD card
  if (!SD.begin(chipSelect)) {
    Serial.println("SD card initialization failed!");
    return;
  }

  // Initialize Arducam
  while (1) {
    Serial.println("Initializing ArduCAM...");
    if (camera.begin() != 0) {
      Serial.println("ArduCAM initialization successful!");
      break;
    }
    delay(1000);
  }

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
}

void loop() {
  // Capture image
  captureImage();

  // Upload image to server
  if (WiFi.status() == WL_CONNECTED) {
    if (uploadImage()) {
      Serial.println("Image uploaded successfully!");
    } else {
      Serial.println("Failed to upload image!");
    }
  } else {
    Serial.println("WiFi connection lost. Reconnecting...");
    delay(1000);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("\nReconnected to WiFi");
  }
  delay(5000); // Delay between uploads
}

void captureImage() {
  Serial.println("Capturing image...");
  camera.set_format(BMP);
  camera.InitCAM();
  camera.OV7670_set_JPEG_size(OV7670_320x240);
  camera.clear_fifo_flag();
  camera.start_capture();
  while (!camera.get_bit(ARDUCHIP_TRIG, CAP_DONE_MASK));
  Serial.println("Image captured!");
}

bool uploadImage() {
  Serial.println("Uploading image...");

  // Open image file
  imageFile = SD.open("image.jpg", FILE_READ);
  if (!imageFile) {
    Serial.println("Failed to open image file!");
    return false;
  }

  // Create HTTP client
  HTTPClient http;
  http.begin(serverName, serverPort, uploadUrl);

  // Set headers
  http.addHeader("Content-Disposition", "attachment; filename=image.jpg");

  // Start POST request
  int httpCode = http.POST(imageFile);
  if (httpCode > 0) {
    Serial.printf("HTTP response code: %d\n", httpCode);
    String response = http.getString();
    Serial.println(response);
    http.end();
    imageFile.close();
    return true;
  } else {
    Serial.printf("HTTP request failed, error: %s\n", http.errorToString(httpCode).c_str());
    http.end();
    imageFile.close();
    return false;
  }
}
