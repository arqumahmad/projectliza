#import weather
import os
import sys
#import RPi.GPIO as GPIO
from gtts import gTTS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

def say(words):

    tts = gTTS(text=words, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

#say(weather.d)
