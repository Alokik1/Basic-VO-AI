import datetime
import os
import smtplib
import webbrowser
from tkinter import *

import pyttsx3
import speech_recognition as sr
import wikipedia
from PIL import Image, ImageTk
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")


def takecommmand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("Say that again please")
        return "None"
    return query


class Widget:
    def __init__(self):
        root = Tk()

        root.title('Jarvis(Mark-1)')
        root.geometry('1320x700')

        img = ImageTk.PhotoImage(Image.open(r"D:\white.png"))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand="no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Run Jarvis\' to Give commands')

        userFrame = LabelFrame(root, text="User", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText, bg='#3B3B98', fg='white')
        left2.config(font=("Century Gothic", 24, 'bold'))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="Jarvis", font=('Black ops one', 10, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, bg='#3B3B98', fg='white')
        left1.config(font=("Century Gothic", 24, 'bold'))
        left1.pack(fill='both', expand="yes")

        self.compText.set('Hello, I am Jarvis! What can i do for you Sir ??')

        btn = Button(root, text='Run Jarvis', font=('Black ops one', 10, 'bold',), bg='#4b4b4b', fg='white',command=self.clicked).pack(
            fill='x', expand='no')
        btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy ).pack(
            fill='x', expand='no')

        root.bind("<Return>",self.clicked)    
        root.mainloop()


    def clicked(self):
        print('Working')
        query = takecommmand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query.lower():
             speak("opening youtube")
             url = "youtube.com"
             chrome_path = 'C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\Application %s'
             webbrowser.get(chrome_path).open(url)

        elif 'open gmail' in query.lower():
             speak("opening g-mail")
             url = "gmail.com"
             chrome_path = 'C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs %s'
             webbrowser.get(chrome_path).open(url)


        elif 'play music' in query.lower():
            speak("Alright sir playing music")
            songs_dir = "C:\\Users\hp\\Music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'play videos' in query.lower():
            speak("Alright here's some entertainment for you sir")
            video_dir = "E:\\Video"
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))


        elif 'thank you' in query.lower():
            speak("Its my pleasure sir to always help you")

        elif 'sorry' in query.lower():
            speak("well if you really are then say it to my master")

        elif 'please' in query.lower():
            speak("Don't say please sir!!!... I'm always here to help you")

        elif 'what can you do' in query.lower():
            speak("its better if you ask what kind of assistant you are")

        elif 'what kind of assistant are you' in query.lower():
            speak("kind of helpful")

        elif 'help me' in query.lower():
            speak("always ready to help you ALokik sir")

        elif 'what is your name' in query.lower():
            speak("Selena sir")

        elif 'ok google' in query.lower():
            speak("thats not me sir....why are confusing me with her?")

        elif 'hey siri' in query.lower():
            speak("Finally some another female AI you can talk to")

        elif 'i want to be rich' in query.lower():
            speak("so do i")

        elif 'play me some songs,jarvis' in query.lower():
            speak("Alright sir! i will try for you")
            songs_dir = "C:\\Users\hp\\Music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[30]))


        elif 'What do you think about this project ' in query.lower():
            speak("I just hope it helps you clear your exams ")
        else:
            webbrowser.open(query)

if __name__ == '__main__':
    speak("INITIALIZING Selena")
    wishme()
    widget = Widget()
