from beep import beep
import random


greet=["Hello","Hi","Hey"]
import weather
from news import world
from news import local
import RPi.GPIO as GPIO
from tts import say
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)



def command(data):
    b=data

    if (b.find('weather')>-1):
        say(weather.d)
    elif (b.find('temperature')>-1):
        say(weather.temp)
    elif(b.find('news')>-1) or b.find('headlines')>-1:
        if (b.find('international')>-1):
            world()
        else:
            local()

    elif(b.find('light')>-1) and b.find('on')>-1:

        GPIO.output(16,GPIO.HIGH)
    elif(b.find('light')>-1) and(b.find('off')>-1 or b.find('of')>-1):
        GPIO.output(16,GPIO.LOW)

    elif(b.find('open')>-1) and b.find('door')>-1:

        GPIO.output(20,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
    elif(b.find('close')>-1) and b.find('door')>-1:

        GPIO.output(21,GPIO.HIGH)
        GPIO.output(20,GPIO.LOW)
