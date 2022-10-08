import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio
import pyjokes
import random
import requests
import time
 
# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id) 

 # 1 for female and 0 for male voice

doing = ("Doing good, but not as you. ", "Looking good outside, but not inside.", "Just talking with you, sir", "In which terms, emotionally or financially?")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    print("Happy Birthday Master")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 20
        audio = r.listen(source)

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        
        if 'Mango' in query:

            print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("Sorry Master, I don't understand")
        return "None"
    return query



if __name__ == '__main__':

    
    speak("Mango Assistance Initializing......")
    speak("How can i help you?, Master Riddo")
    speak("")

    while True:
        query = take_command().lower()

        
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
       
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\EDOS 2\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
    
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")

        elif 'who are you' in query:
            speak("I'm Mango. developed by Ahmed Shahmir Riddo")

        elif 'hello' in query:
            speak("Hi, Sir. I am Mango.")

        elif 'how are you' in query:
            speak('I am fine and What about you?, sir')

        elif 'fine' in query:
            speak("I am glad to know!")

        elif 'Thank you'in query:
            speak("Youre most welcome")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())


        elif 'good morning' in query:
            speak("Very Good Morning too, sir")
            print("Very Good Morning")
     
        elif 'good night' in query:
            speak("Good Night, Sir")
            print("Good Night, Sir")



        elif 'what are you doing' in query:
            speak(random.choice(doing))

        elif 'Are you a robot' in query:
            speak("Yes, I am a Robot. Shahmir Riddo created me")

        elif 'who is ri' in query:
            speak("SHahmir Riddo is a Programmer.")

        elif 'what is your name' in query:
            speak("My name is mango, what is your name?")

        elif 'my name is' in query:
            speak("Hello"+query)

        elif 'news' in query:
            webbrowser.open("bbcnews.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'how old are you' in query:
            speak("I am unborn")

        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=R0rKB_bsUNg")

        elif 'wish me' in query:
            speak("Happy Birthday")

        elif 'open calculator' in query:
            speak("Opening calculator")
            webbrowser.open("https://calculator-online.net/")

        elif 'open facebook' in query:
            speak("Opening FB")
            webbrowser.open("www.facebook.com")

        
  

        

    
    
        elif 'sleep' in query:
            exit(0)





