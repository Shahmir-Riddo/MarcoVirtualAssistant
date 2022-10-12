import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio
import pyjokes
import random
import requests
import wolframalpha
import datetime as dt
import time



 
# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id) 

 # 1 for female and 0 for male voice

doing = ("Doing good, but not as you. ", "Looking good outside, but not inside.", "Just talking with you, sir", "In which terms, emotionally or financially?")
greeting = ("What we gonna do today?", "Whats the plans for today", "master, are you busy?")
hlo = ("Hello, master", "Sup, Master", "hey master","Hi, Master", "Hola, Master", "Greetings, master")




def speak(audio):
    engine.say(str(audio))
    engine.runAndWait()

def wish():
    tem = dt.datetime.now().strftime("%H:")
    if tem == "1":
        speak("Good Morning!, Master ")
        speak("The is 1 AM. ")

    elif tem == "10" :
        speak("good night Master. Time to sleep. ")

    


    
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("______________")
        print("Listening...")
        r.pause_threshold = 1
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

    
    speak("Marco Assistance Activated......")
    speak("How can i help you?, Master Riddo")
    speak("")
    print('\033[1;32;49m' + """


 ███▄ ▄███▓ ▄▄▄       ██▀███  ▄████▄  ▒█████  
▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒██▀ ▀█ ▒██▒  ██▒
▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▓█    ▄▒██░  ██▒
▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄ ▒▓▓▄ ▄██▒██   ██░
▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒ ▓███▀ ░ ████▓▒░
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ░▒ ▒  ░ ▒░▒░▒░ 
░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░  ▒    ░ ▒ ▒░ 
░      ░     ░   ▒     ░░   ░░       ░ ░ ░ ▒  
       ░         ░  ░   ░    ░ ░         ░ ░  
                             ░                
                                                             

 
  VOICE ASSISTANT""")

    while True:
        query = take_command().lower()
        wish()

        
        
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
            speak(random.choice(hlo))
            speak(random.choice(greeting))
            a = take_command()
            speak("Ok, Master")

        elif 'who are you' in query:
            speak("I'm Marco. A Voice Assistant Robot developed by Ahmed Shahmir Riddo")

        elif 'hello' in query:
            speak("Hi, Sir. I am Marco.")

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

        elif 'who is ri' in query:
            speak("Shahmir Riddo is a Programmer.")

        elif 'your name' in query:
            speak("My name is marco, what is your name?")
            
            r = open("name.txt", "w")
            name = take_command()
            for line in name:
	
	    
                 r.write(line.replace('my name is', ','))
                
            speak("Hello" + name)
            r.close()

        elif 'what is my name' in query:
            speak("I forgot, please tell me what is your name?")
            
            r = open("name.txt", "w")
            name = take_command()
            for line in name:
	
	            r.write(line.replace('my name is', ''))
                
            speak("Hello" + name)

        
        elif 'news' in query:
            webbrowser.open("bbcnews.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'how old are you' in query:
            speak("I am 1000 years old")

        elif 'music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=R0rKB_bsUNg")

        elif 'stop music' in query:
            time.sleep(60)

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
	
	            rembr.write(line.replace("I", "you"))
                
            speak("You told me to remember that " + data)
            rembr.close()

               
        elif 'what did you remember'  in query:
            rm = open("data.txt", "r")
            speak("You told me to remember that you" + rm.read())

        elif 'remind me'  in query:
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

        elif 'time' in query:

            time=dt.datetime.now().strftime("%H:%M:%S")   #24 hour format
            
            speak("The Current time is: ")
            speak(time)

        elif 'can you get smart' in query:
            speak("No, I cant change myself!!")

        elif 'are we friends' in query:
            speak("Yes, We are")

        elif 'bangladesh' in query:
            speak("Bangladesh  , officially the People's Republic of Bangladesh, is a country in South Asia. It is the eighth-most populous country in the world, with a population exceeding 165 million people in an area of 148,460 square kilometres (57,320 sq mi).[7] Bangladesh is among the most densely populated countries in the world, and shares land borders with India to the west, north, and east, and Myanmar to the southeast; to the south it has a coastline along the Bay of Bengal. It is narrowly separated from Bhutan and Nepal by the Siliguri Corridor; and from China by the Indian state of Sikkim in the north. Dhaka, the capital and largest city, is the nation's political, financial and cultural center. Chittagong, the second-largest city, is the busiest port on the Bay of Bengal. The official language is Bengali, one of the easternmost branches of the Indo-European language family.")
        
        elif 'bored' in query:
            speak("")
        elif 'sleep' in query:
            time.sleep(600)

 
