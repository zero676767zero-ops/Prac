import RPi.GPIO as GPIO
from time import sleep 

# GPIO.setmode(GPIO.BOARD)
# ledPin = 15

GPIO.setmode(GPIO.BCM)
ledPin = 22

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    while True:
        GPIO.output(ledPin, True)
        sleep(1)
        GPIO.output(ledPin, False)
        sleep(1)
finally:
    GPIO.output(ledPin, False)
    GPIO.cleanup