import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate=190
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
#time()
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("wlcome back sir")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=24:
        speak("Good evening")
    else:
        speak("Good Night")
        
    speak(" Basanti at your service! How can i help you")
def takeCommand():

    r = sr.Recognizer()



    with sr.Microphone() as source:

        print("listening...")

        #r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        r.pause_threshold = 1

        audio = r.listen(source)

        try: 

            print("Recognising...")
            query=r.recognize_google(audio, language='en-in')

            print(query)

        except Exception as e:
            print(e)
            speak("Say it again please....")
            return 'None'
        return query
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',465)
    server.ehlo()
    server.starttls()
    server.login("yadavsagar2340@gmail.com","12345")
    server.sendmail("yadavsagar2340@gmail.com",to,content)
    server.close()
def screenshot():
    img=pyautogui.screenshot()
    img.save("G:/sem5/screen/va.png")
def cpu():
    usage=str(psutil.cpu_percent())
    speak("Cpu is at"+usage+"percentage")
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())
if __name__ == '__main__':
    wishme()
    while True:
        query=takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Thank You")
            break
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "kutton ke samne" in query:
            speak("maa chudai kutte")
        elif "send email" in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="saggi2340@gmail.com"
                sendmail(to,content)
                #speak(content)
            except Exception as e:
                speak(e)
                speak("sorry unable to send the message")
        elif "search on internet" in query:
            speak("What should i search?")
            chromepath ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play music" in query:
            songs_dir="C:/Users/Akash Yadav/Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember that" in query:
            speak("What should i remeber?")
            data=takeCommand()
            speak("You said me to remember"+data)
            remember=open("va.txt","w")
            remember.write(data)
            remember.close()
        elif"do you know anything" in query:
            remember=open("va.txt","r")
            speak("you said me to remember that"+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("screenshot taken")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
        
            
                  
    