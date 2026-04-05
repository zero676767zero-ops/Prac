# Pin : vcc -> pin 1, gnd -> pin 6, DO -> Pin 11(GPIO 17)
# Led : + long leg terminal -> Pin 12(GPIO 18) , -ve short leg -> Pin 14(Gnd)

import RPi.GPIO as GPIO
from time import sleep 

FLAME_DO = 17
ALERT = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(FLAME_DO, GPIO.IN)
GPIO.setup(ALERT, GPIO.OUT)

GPIO.output(ALERT, False)
print("Flame Sensor Ready....")

try:
    while True:
        value = GPIO.input(FLAME_DO)
        print("Sensor Output(DO) =", value)
        # 0 means flame detected
        if value == 0:
            GPIO.output(ALERT, True)
            print("Flame Detected, ALERT ON!!!")
        else:
            GPIO.output(ALERT, False)
            print("No Flame Detected, ALERT OFF!!!")
        sleep(0.5)
except KeyboardInterrupt:
    print("Some Error Occurred")
finally:
    GPIO.cleanup()

