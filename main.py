import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speak function - takes text as input and speaks it
def speak(text):
    engine.say(text)
    engine.runAndWait()
    

# speech to text function
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
    
    
text = takecommand()
speak(text)




