# Vcc -> Pin 4
# Gnd -> Pin 6
# led gnd -> Pin 9, 20
# led -> 16 GPIO23
# ir sensor -> 18 GPIO24 

import RPi.GPIO as GPIO
from time import sleep

sensor = 18 # GPIO24
led = 16 #GPIO23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        if GPIO.input(sensor) == 0:
            GPIO.output(led, True)
            print("Object Detected")
        else:
            GPIO.output(led, False)
except KeyboardInterrupt:
    print("Some Error Occurred...")
finally:
    GPIO.output(led, False)
    GPIO.cleanup()


