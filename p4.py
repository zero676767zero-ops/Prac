# sudo apt install python3-pip
# pip3 install telepot 

import telepot
from telepot.loop import MessageLoop
from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO

red = 22
yellow = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0)

GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0)

def action(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]
    print("Received: " + command)
    if "on" in command.casefold():
        message = "on "
        if "red" in command.casefold():
            message += "red"
            GPIO.output(red, 1)
        elif "yellow" in command.casefold():
            message += "yellow"
            GPIO.output(yellow, 1)
        message += " light"
        telegram_bot.sendMessage(chat_id, message)
    
    if "off" in command.casefold():
        message = "off "
        if "red" in command.casefold():
            message += "red"
            GPIO.output(red, 0)
        elif "yellow" in command.casefold():
            message += "yellow"
            GPIO.output(yellow, 0)
        message += " light"
        telegram_bot.sendMessage(chat_id, message)

telegram_bot = telepot.Bot("")
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()


try:
    while True:
        sleep(10)
finally:
    GPIO.output(red, 0)
    GPIO.output(yellow, 0)
    GPIO.cleanup()