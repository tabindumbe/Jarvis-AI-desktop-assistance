import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import psutil # pip install psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time

engine = pyttsx3.init()
wolframalpha_app_id = 'tabindumbe@gmail.com'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    speak ("The current time is")
    speak(Time)
    
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Mac-Roy!")
    time_()
    date_()

    #greetings

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Jarvis at your service")
    speak("What can i do for you sir?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('tabindumbe@gmail.com','Firstlove9.')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/nana/Desktop/screenshot.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())
    



if __name__ == '__main__':
    
    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()

        if 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching....")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content=TakeCommand()

                speak("Who is the receiver?")
                receiver=input("Enter Receiver's Email :")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak("Unable to send Email.")

        elif 'search in chrome' in query:
            speak('What should i search?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #opens only websites with '.com' extension
           

        elif 'search youtube' in query:
            speak('What should i search?')
            search_Term = TakeCommand().lower()
            speak("Here we go to YOUTUBE!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('What should i search?')
            search_Term = TakeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_Term)


        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going Offline Sir!')
            quit()

        elif 'word' in query:
            speak('Opening MS Word....')
            ms_word = r'C:/office/Office14/WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak('What should i write, Sir?')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("Sir should i include Date and Time?")
            ans = TakeCommand()

            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, SIR!')
            else:
                file.write(notes)

        elif 'show note' in query:
             speak('showing notes')
             file = open('notes.txt','r')
             print(file.read())
             speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir = 'C:/SONGS'
            music = os.listdir(songs_dir)
            speak('What should i play?')
            speak('select a number....')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('I could not understand you. Please Try Again.')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in query:
                no = random.randint(1,100)
            
            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'calculate' in query:
            app_id = "tabindumbe@gmail.com"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")


           

        elif 'remember that' in query:
            speak("What should i remember?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You asked me to remember that'+remember.read())

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=42d002fb61134c8eb8081f52073a88b3")
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top headlines from the Business Industry')
                print('==========TOP HEADLINES=========='+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                    print(str(e))

        elif 'stop listening' in query:
            speak("For how long should i stp listening?")
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")


        












        


    





