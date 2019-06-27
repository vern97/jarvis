import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


class User:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
        speak("Alright. I'll call you " + self.name + " for now on.")

    def get_user(self):
        speak("Hello, " + self.name + ". What can I do for you?")


class Jarvis(User):

    def __init__(self, name):
        User.__init__(self, name)

    def jarvis(self, data):
        if "how are you" in data:
            speak("I am fine")

        if "what time is it" in data:
            speak(ctime())

        if "where is" in data:
            data = data.split(" ")
            location = data[2]
            speak("Hold on " + self.name + ", I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    def run_jarvis(self):

        time.sleep(2)
        self.get_user()

        while 1:
            data = recordAudio()
            self.jarvis(data)


# initialization
jarvis = Jarvis("Vern")

jarvis.run_jarvis()
