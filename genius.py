from types import coroutine
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os,sys
import time
import pywikihow
from pywikihow import search_wikihow
import pywhatkit
import keyword
import subprocess
import ctypes
import winshell
from twilio.rest import Client
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)###speed of thr reading text default 200 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning !")
        speak("Good Morning !")
        
    elif hour>=12 and hour<16:
        print("Good Afternoon !")
        speak("Good Afternoon !")   
        
    else:
        print("Good Evening !") 
        speak("Good Evening !")  
        
    assiname =("Genius")
    speak("I am your Assistant")
    speak(assiname)


def takeCommand():
   
    r = sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:  
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()
        
       #------------------- AI ------------------
       
        if 'how are you' in query:
            speak('I am fine, Thank you')
            speak("How are you ??")

        elif "good" in query or "fine" in query:
            speak('Its good to know that your fine')

        elif 'go to sleep' in query:
            speak("Thanks for giving me your time")
            speak("i am going to sleep good night.")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Infinity Square.")

        #---------------- Browser Based ----------------

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("ok ,just a second")
            speak("opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            speak("ok ,just a second")
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        
        elif 'play my' in query:
            speak("ok ,just a second")
            speak("playing your favourite song from youtube")
            webbrowser.open("https://www.youtube.com/watch?v=gR2irrU9Xeo&list=PLRBp0Fe2GpglTnOLbhyrHAVaWsCIEX53Y&ab_channel=NoCopyrightSounds")

        elif 'how' in query:
            speak("ok ,just a second")
            speak("activating how to do mode")
            speak("how to do mode activated")
            while True:
                speak("please tell me what you want to know ")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("ok , how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

        elif 'search on google ' in query:
            import wikipedia as googlescrap
            query = query.replace("Genius","")
            query = query.replace("google search","")        
            query = query.replace("google","")
            speak("this is what i found in the web")
            pywhatkit.search(query)

            try:
                result = googlescrap.summary(query,2)
                speak(result)

            except:
                speak("no data found!!!!! sorry ") 
        
        #------------------- Opening Applications ----------------
        
        elif 'play music' in query:
            speak("ok ,just a second")
            speak("playing music")
            music_dir = 'D:\\music\\english'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in query:
            speak("ok ,just a second")
            speak("opening visual studio code")
            codePath = "D:\Microsoft VS Code\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            
        elif 'close code' in query:
            os.system("TASKKILL /F /IM Code.exe")

        elif 'open chrome' in query:
            speak("ok ,just a second")
            speak("opening chrome")
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'open word' in query:
            speak("ok ,just a second")
            speak("opening word")
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)
            
        elif 'close word' in query:
            os.system("TASKKILL /F /IM WINWORD.EXE")

        elif 'open control panel' in query:
            speak("ok ,just a second")
            speak("opening controlpanel")
            controlpanelPath = "C:\Windows\System32\Control.exe"
            os.startfile(controlpanelPath)
            
        elif 'close control panel' in query:
            os.system("TASKKILL /F /IM Control.exe")
            
        elif 'open excel' in query:
            speak("ok ,just a second")
            speak("opening excel")
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excelPath)
            
        elif 'close excel' in query:
            os.system("TASKKILL /F /IM EXCEL.EXE")
            
        elif 'open powerpoint' in query:
            speak("ok ,just a second")
            speak("opening powerpoint")
            powerpntPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(powerpntPath)
            
        elif 'close powerpoint' in query:
            os.system("TASKKILL /F /IM POWERPNT.EXE")    

        #------------------------- System Based --------------------

        elif 'the time' in query:
            speak("ok ,just a second")
            speak("showing time")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
        
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("Genius","")
            speak("you tell me to remind you that:" + rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query: 
            remember = open('data.txt','r')
            speak("you tell me that" + remember.read())         
            print(remember.read())

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'online' in query:

            from Automations import OnlinClass

            speak("Tell Me The Name Of The Class .")

            Class = takeCommand()

            OnlinClass(Class)