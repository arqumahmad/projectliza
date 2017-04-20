import speech_recognition as sr
from beep import beep
import weather
import RPi.GPIO as GPIO
from tts import say

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

r = sr.Recognizer()
# obtain audio from the microphone
def commands():

    if a.find("weather")>-1:
        say(weather.d)
    else if a.find("temperature")>-1:
        say(weather.temp)



while True:

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)



        #print("Say something!")
        GPIO.output(18,GPIO.HIGH)

        beep()
        audio = r.listen(source, timeout=2)
        GPIO.output(18,GPIO.LOW)

    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        a =str(r.recognize_google(audio))
        print a
    except sr.UnknownValueError:
        continue
    except sr.RequestError as e:
        continue
    if a.find("hello") >-1 and a.find("alpha"):
        GPIO.output(17,GPIO.HIGH)
        beep()
        GPIO.output(17,GPIO.LOW)
        commands()
