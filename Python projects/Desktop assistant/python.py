import datetime
import pyjokes
import speech_recognition as speech
import pyttsx3

engine = pyttsx3.init('sapi5') # sapi5 is for microsoft voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    recog = speech.Recognizer()

    with speech.Microphone() as source:
        print("python: is listeing...")
        audio = recog.listen(source)

        try:
            query = recog.recognize_google(audio)
            print(f"master:(query)")
            return query
        except:
            print("Try again")

if True:
    query = command().lower()

    if "name" in query:
        speak("Hi, My name is python")
    elif "hello python" in query:
        speak("What can i do for you")
    elif "tell me a joke" in query:
        speak(pyjokes.get_joke())
    elif "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %P")
        speak(f"Time is {time}")
    elif "are you single" in query:
        speak("i am love with firewall but it keeps blocking me")
    elif "exit" in query:
        speak("Have a nice day")
        breakpoint
    else:
        speak("i don't know what you mean")

print(command())
