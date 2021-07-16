import os
import webbrowser

import pyttsx3 as px
import datetime
import speech_recognition as sr
import wikipedia

engine = px.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0])
hour = int(datetime.datetime.now().hour)


def chrome(link):
    chromedir = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chromedir).open(link)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def salutation():
    if 0 <= hour < 12:
        speak("Good morning your majesty!! How can i help you")
    elif 12 <= hour < 18:
        speak("Good afternoon your majesty!! How can i help you")
    else:
        speak("Good evening your majesty!! How can i help you")


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        speak("you said")
        print(query)
        speak(query)

    except Exception:
        print("bol")
        return "none"
    return query


if __name__ == '__main__':
    salutation()
    while True:
        query = take().lower()
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            speak("searching in wikipedia....")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "open movies folder" in query:
            movies = "E:\\movies"
            os.startfile(movies)

        elif "open" in query:
            query = query.replace("open", "") + ".com"
            print(query)
            speak("opening")
            chrome(query)

        if "search" in query:
            query = query.replace("search", "")
            if "in youtube" in query:
                query = query.replace("in youtube", "")
                link = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
                chrome(link)
            else:
                query = query.replace("search", "") and query.replace(" ", "+")
                link = "https://www.google.com/search?q=" + query
                chrome(link)

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"The time is {time}")

        elif "shutdown" in query:
            exit()
