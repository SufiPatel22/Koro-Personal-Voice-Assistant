from types import coroutine
import pyttsx3
import speech_recognition as sr
from Features import GoogleSearch
from win10toast import ToastNotifier
import datetime
import webbrowser
import subprocess
import os,sys
import pywikihow
from pywikihow import search_wikihow
import winshell
import ctypes
import time
import pyjokes
from pywikihow import search_wikihow
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)###speed of thr reading text default 200 

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning !")
        print("I'm genius,your personal voice assistance.")
        Speak("Good Morning !")
        
    elif hour>=12 and hour<18:
        print("Good Afternoon !")
        Speak("Good Afternoon !")   
        
    else:
        print("Good Evening !") 
        Speak("Good Evening !")  

def TakeCommand():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def TaskExe():
    wishMe()
    while True:

        query = TakeCommand()

        if 'google search' in query:
            GoogleSearch(query)

        elif 'youtube search' in query:
            Query = query.replace("koro","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'open stackoverflow' in query:
            Speak("ok prajwal,just a second")
            Speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            Speak("ok prajwal,just a second")
            Speak("playing music")
            music_dir = 'D:\\music\\english'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            Speak("ok prajwal,just a second")
            Speak("showing time")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            Speak("ok prajwal,just a second")
            Speak("opening visual studio code")
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe "
            os.startfile(codePath)
        
        elif 'close code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'open new' in query:
            Speak("opening uTorrent")
            newPath = "C:\\Users\\Admin\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            os.startfile(newPath)

        elif 'close new' in query:
            os.system("TASKKILL /F /im uTorrent.exe")

        elif 'open chrome' in query:
            Speak("opening chrome")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'close chrome' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'open word' in query:
            Speak("opening word")
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)

        elif 'close word' in query:
            os.system("TASKKILL /F /im WINWORD.exe")

        elif 'open control panel' in query:
            Speak("opening controlpanel")
            controlpanelPath = "%windir%\\System32\\Control.exe"
            os.startfile(controlpanelPath)

        elif 'close control panel' in query:
            os.system("TASKKILL /F /im Control.exe")

        elif 'open excel' in query:
            Speak("opening excel")
            excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excelPath)

        elif 'close excel' in query:
            os.system("TASKKILL /F /im excel.exe")

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'how' in query:
            while True:
                Speak("please tell me what you want to know ")
                how = TakeCommand()
                try:
                    if "exit" in how or "close" in how:
                        Speak("Thank you !!!")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        Speak(how_to[0].summary)
                except Exception as e:
                    Speak("sorry sir, i am not able to find this")


        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("koro","")
            Speak("you tell me to remind you that:" + rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query: 
            remember = open('data.txt','r')
            Speak("you tell me that" + remember.read())         
            print(remember.read())
################################not worining whats app#########################################
        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("koro ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)
####################################################################
        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("koro" , "")
            GoogleMaps(Place)

        elif 'online' in query:

            from Automations import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)
########################not worining note##################################
        elif 'write a note' in query:

            from Automations import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad

            CloseNotepad()
##########################################################################################
        elif 'joke' in query:
            Speak(pyjokes.get_joke())

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "log off" in query or "sign out" in query:
            Speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'lock window' in query:
            Speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            Speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            Speak("Recycle Bin Recycled")
        elif 'play my' in query:
            Speak("ok prajwal,just a second")
            Speak("playing your favourite song from youtube")
            webbrowser.open("https://www.youtube.com/watch?v=b4iOwqZCmv4&list=RDb4iOwqZCmv4&index=2")
####################################################################3  
        elif 'website' in query:
            Speak("ok sir, Launching......")
            query = query.replace("koro","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www.'+ web1 +'.com'
            webbrowser.open(web2)
            Speak("launched!")

        elif 'search on google ' in query:
            import wikipedia as googlescrap
            query = query.replace("koro","")
            query = query.replace("google search","")        
            query = query.replace("google","")
            Speak("this is what i found in the web")
            pywhatkit.search(query)

            try:
                result = googlescrap.summary(query,2)
                Speak(result)

            except:
                Speak("no data found!!!!! sorry ")

###############################################################################
        elif 'corona cases' in query:

            from Features import CoronaVirus

            Speak("Which Country's Information ?")

            cccc = TakeCommand()

            CoronaVirus(cccc)

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break

TaskExe()
