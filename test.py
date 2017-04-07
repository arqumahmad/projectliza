import speech_recognition as sr
from beep import beep
import weather

from tts import say

# obtain audio from the microphone
while True:
    say('Hello Arqum, What can I do for you?')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)


        print("Say something!")
        beep()
        audio = r.listen(source)

    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    word_set = {"weather", "climate", "temperature"}
    string_to_be_searched = str(r.recognize_google(audio))

    for w in string_to_be_searched.split():
        if w in word_set:
            say(weather.d)
