# sudo raspi-config

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1200, 720)
camera.start_preview()
sleep(10)
camera.capture('/home/pi/pictures/a1.jpg')
camera.stop_preview()