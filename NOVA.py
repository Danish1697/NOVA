import pyttsx3
import webbrowser
import speech_recognition as sr
import time
import os
import pywhatkit

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

def Wishme():
    time_teller = time.strftime("%H")
    if (int(time_teller)<12):
        engine.say("Good Morning Sir")
        engine.runAndWait()
    elif (int(time_teller)<18):
        engine.say("Good Afternoon Sir")
        engine.runAndWait()
    else:
        engine.say("Good Night Sir")
        engine.runAndWait()

def speak(speech):
    engine.say(speech)
    engine.runAndWait()

def takeCommand():
    reconizer=sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source :
        print("Say Something...")
        audio =reconizer.listen(source)
        try:
            query = reconizer.recognize_google(audio)
            print(f'User said : {query}')
            return query
        except Exception as e:
            return 'Could not recoginized the voice...'

if __name__=="__main__":
    speak("Hello My name is Nova..Nice to meet you..How are you ")
    Wishme() 

    while True:
        query = takeCommand().lower()

        if ("open youtube" in query):
            speak("Opening Youtube Sir.")
            webbrowser.open("www.youtube.com")
        elif ("open google" in query):
            speak("Opening google sir")
            webbrowser.open("www.google.com")
        elif ("send message" in query):
            time_hour = time.strftime("%H")
            time_minute = time.strftime("%M")
            speak(f"In {int(time_minute)+1} Seconds WhatsApp will open and after 2 seconds Message will be Delivered ! ")
            try:
                pywhatkit.sendwhatmsg("Mobile Number","Hello world",int(time_hour),int(time_minute)+1,2)
            except Exception:
                speak("Message has been sent Sir !!")
        elif("nova" in query):
            speak("Yes Sir. How may i help you?")
        elif ("sleep" in query):
            speak("Activating Sleep mode.")
            break 
        elif ("play music" in query):
            os.startfile("Path of music file")  #USE \\
