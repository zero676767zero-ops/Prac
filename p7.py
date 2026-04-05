# sudo apt install python3-pip
# pip install Adafruit_DHT

# vcc -> Pin 1
# gnd -> Pin 6
# out -> Pin 7 (GPIO4)

import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

gpio_pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read(sensor, gpio_pin)
    if humidity is not None and temperature is not None:
        print("Temperature = {:.1f} degree Celcius".format(temperature))
        print("Humidity = {:.1f}%".format(humidity))
        print("-"*80)
    else:
        print("Failed to retrieve data from temperature")
    
    time.sleep(1)
    