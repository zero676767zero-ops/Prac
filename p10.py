# Smoke sensor - vcc -> Pin 2 (5V),gnd -> Pin 6, DO -> Pin 11(GPIO17)
# LED - LL -> 13(GPIO 27), SL -> Pin 14(Gnd)

import RPi.GPIO as GPIO
from time import sleep 

SMOKE_DO = 17
LED_PIN = 27 

GPIO.setmode(GPIO.BCM)

GPIO.setup(SMOKE_DO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, False) 

try:
    while True:
        smoke_value = GPIO.input(SMOKE_DO)
        if smoke_value == 0:
            print("Smoke/Gas Detected")
            GPIO.output(LED_PIN, GPIO.HIGH)
        else: 
            print("No Smoke Detected. Air is clean")
            GPIO.output(LED_PIN, GPIO.LOW)
        sleep(0.5)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()