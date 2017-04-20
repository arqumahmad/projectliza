import weather
import subprocess
import os
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

def say(words):
    GPIO.output(27,GPIO.HIGH)
    tempfile = "temp.wav"
    devnull = open("/dev/null","w")
    subprocess.call(["pico2wave", "-w", tempfile, words],stderr=devnull)
    subprocess.call(["aplay", tempfile],stderr=devnull)
    os.remove(tempfile)
    GPIO.output(27,GPIO.LOW)
#say(weather.d)
