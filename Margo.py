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

engine.setProperty('voice', voices[0].id) 

 # 1 for female and 0 for male voice

doing = ("Doing good, but not as you. ", "Looking good outside, but not inside.", "Just talking with you, sir", "In which terms, emotionally or financially?")






def speak(audio):
    engine.say(str(audio))
    engine.runAndWait()


    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("______________")
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    

    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
      
    except Exception as e:
        print(e)
        speak("sorry master, can you please repeat?")
        return "None"
    return query



if __name__ == '__main__':

    
    speak("Margo Assistance Activated......")
    speak("How can i help you?, Master Riddo")
    speak("")
    print('\033[2;34;49m' + """  ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████    ▄██████▄   ▄██████▄  
 ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███    ███ ███    ███ 
 ███   ███   ███   ███    ███   ███    ███   ███    █▀  ███    ███ 
 ███   ███   ███   ███    ███  ▄███▄▄▄▄██▀  ▄███        ███    ███ 
 ███   ███   ███ ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███ ████▄  ███    ███ 
 ███   ███   ███   ███    ███ ▀███████████   ███    ███ ███    ███ 
 ███   ███   ███   ███    ███   ███    ███   ███    ███ ███    ███ 
  ▀█   ███   █▀    ███    █▀    ███    ███   ████████▀   ▀██████▀  
                                ███    ███                         

  VOICE ASSISTANT""")

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

        elif 'mar' in query:
            speak("hello, sir")
            speak("Whats  the plan today?")
            speak("")

        elif 'who are you' in query:
            speak("I'm Margo. A Voice Assistant Robot developed by Ahmed Shahmir Riddo")

        elif 'hello' in query:
            speak("Hi, Sir. I am Margo.")

        elif 'how are you' in query:
            speak('I am fine and, What about you?, sir')

        elif 'fine' in query:
            speak("I am glad to know!")

        elif 'Thank you'in query:
            speak("You are most welcome")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())


        elif 'good morning' in query:
            speak("Very Good Morning too, sir")
            speak("Have you done your breakfast?")
      
     
        elif 'good night' in query:
            speak("Good Night, Sir")
            print("Good Night, Sir")



        elif 'what are you doing' in query:
            speak(random.choice(doing))

        elif 'Are you a robot' in query:
            speak("Yes, I am a Robot. Shahmir Riddo created me")

        elif 'who is sha' in query:
            speak("Shahmir Riddo is a Programmer.")

        elif 'your name' in query:
            speak("My name is margo, what is your name?")
            
            r = open("name.txt", "w")
            name = take_command()
            for line in name:
	
	            r.write(line.replace('my name is', ''))
                
            speak("Hello" + name)
            r.close()

        elif 'what is my name' in query:
            speak(" what is your name?")
            
            r = open("name.txt", "w")
            name = take_command()
            for line in name:
	
	            r.write(line.replace('my name is', ''))
                
            speak("Hello" + name)
#Shahmir Riddo        
        elif 'news' in query:
            webbrowser.open("bbcnews.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'how old are you' in query:
            speak("I am 1000 years old")

        elif 'music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=R0rKB_bsUNg")

        elif 'wish me' in query:
            speak("Happy Birthday")

        elif 'open calculator' in query:
            speak("Opening calculator")
            webbrowser.open("https://calculator-online.net/")

        elif 'open facebook' in query:
            speak("Opening FB")
            webbrowser.open("www.facebook.com")

        elif 'created you' in query:
            speak("Shahmir Riddo created me")


        elif 'compliment' in query:
            speak("You are the best! sir")

        elif 'rhyme' in query:
            webbrowser.open("https://www.youtube.com/watch?v=T_mSo1dJRNg")

        elif 'what can you do' in query:
            speak("I can talk with you.")

        elif 'do you know google' in query:
            speak("Yes, I know them. They are my friends.")

        elif 'who is your boss' in query:
            speak("My master is Shahmir Riddo")

    
            
        

        elif 'remember that' in query:
            speak("What should i remember? ")
            data = take_command()
            rembr = open("data.txt", "w")
            for line in data:
	
	            rembr.write(line.replace("I am", "you"))
                
            speak("You told me to remember that " + data)
            rembr.close()

               
        elif 'what did you remember' in query:
            rm = open("data.txt", "r")
            speak("You told me to remember that you" + rm.read())

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Shahmir Riddo")

        elif 'are you hungry' in query:
            speak("Yes, I am hungry. Feed me please")

        elif 'are you mad' in query:
            speak("No, you are mad!")
            
        elif 'do you have a brain' in query:
            speak("Yes")

        elif 'talk' in query:
            speak("hey master, how is your day?")
            bag = take_command()
            if "bad" in bag:
                speak("Dont worry, master.")


        
        


        elif 'sleep' in query:
            exit(0)

     
                



            

            

            
    

            

        
 



