import speech_recognition as sr
from process import obj
import RPi.GPIO as GPIO
#from tts import say

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

r = sr.Recognizer()

while True:

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)



#        print("Say something!")
#        GPIO.output(18,GPIO.HIGH)

    #    beep()
        try:
            GPIO.output(18,GPIO.HIGH)
            audio = r.listen(source, timeout=2)
            GPIO.output(18,GPIO.LOW)
        except sr.WaitTimeoutError:
            continue


#        GPIO.output(18,GPIO.LOW)

    try:

        a =str(r.recognize_google(audio))
        obj(a)
    except sr.UnknownValueError:
        continue
    except sr.RequestError as e:
        continue
