# This example demonstrates using frame differencing with your OpenMV Cam to do
# motion detection. After motion is detected your OpenMV Cam will take picture.

import machine
import network
import os
import random
import sensor
import urequests
import time

SSID = ""  # Network SSID
KEY = ""  # Network key

# Specify the URL of the remote Apache server
url = 'http://raspberry.com/upload_image_endpoint'

sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
sensor.skip_frames(time=2000)  # Wait for settings take effect.
sensor.set_auto_whitebal(False)  # Turn off white balance.

led = machine.LED("LED_RED")

def connect_to_wifi():
    # Init wlan module and connect to network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, KEY)

    while not wlan.isconnected():
        print('Trying to connect to "{:s}"...'.format(SSID))
        time.sleep_ms(1000)

    # We should have a valid IP now via DHCP
    print("WiFi Connected ", wlan.ifconfig())

def get_background_image():
    if not "MovementDetection" in os.listdir():
        os.mkdir("MovementDetection")  # Make a temp directory

    print("About to save background image...")
    sensor.skip_frames(time=2000)  # Give the user time to get ready.

    sensor.snapshot().save("MovementDetection/bg.bmp")
    print("Saved background image - Now detecting motion!")

def detect_movement():
    diff = 10  # We'll say we detected motion after 10 frames of motion.
    while diff:
        img = sensor.snapshot()
        img.difference("MovementDetection/bg.bmp")
        stats = img.statistics()
        # Stats 5 is the max of the lighting color channel. The below code
        # triggers when the lighting max for the whole image goes above 20.
        # The lighting difference maximum should be zero normally.
        if stats[5] > 20:
            diff -= 1

    led.on()
    print("Movement detected! Saving image...")
    sensor.snapshot().save("MovementDetection/snapshot-%d.jpg" % random.getrandbits(32))  # Save Pic.
    led.off()

def send_image_to_server():
    # Send a POST request with the image as payload
    response = urequests.post(url, "MovementDetection/bg.bmp")

    # Check the response
    if response.status_code == 200:
        print("Image uploaded successfully!")
    else:
        print("Failed to upload image:", response.status_code)


connect_to_wifi()
get_background_image()
while True:
    detect_movement()
    send_image_to_server()
