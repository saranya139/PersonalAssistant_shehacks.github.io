import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess


print('Success is sweet but secret is sweat , hello I am your personal assistant,Olivia,Come,lets work together.')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')
engine.setProperty("rate",178)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greetUser():
    hour = datetime.datetime.now().hour
    if (hour >= 0) and (hour < 12):
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif (hour >= 12) and (hour < 18):
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am hearing you🧏...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry can you please say that once again")
            return "None"
        return statement


speak("Success is sweet but secret is sweat , hello I am your personal assistant,Olivia Come,lets work together.")
greetUser()


if __name__ == '__main__':

    while True:
        speak("What can I do for you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if 'say hi' in statement:
            speak("Hello nice to hear you")
            time.sleep(3)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Olivia ,your personal assistant' 'I will do simple task like opening youtube,google chrome,'
                  'gmail ,gmeet, gclassroom,tinkerhub,predict time,search wikipedia'
                  'and get top headline news from The Hindu' 'I am here to make your work simple')
            print('I am Olivia ,your personal assistant. I will do simple task like opening youtube,google chrome,gmail,'
                  'gmeet, gclassroom,tinkerhub,predict time,search wikipedia and get top headline news from The Hindu.'
                  'I am here to make your work simple.')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Darsana Gayathri Saranya")
            print("I was built by Darsana Gayathri Saranya")

        elif "positive words" in statement or "motivational quotes" in statement or "inspirational words" in statement:
            speak("you must be the change you wish to see in the world by Mahatma Gandhi ")
            print("you must be the change you wish to see in the world by Mahatma Gandhi ")

        elif 'thank you' in statement:
            speak("welcome, and thank you for spending your valuable time with me. see you later.")
            time.sleep(3)

        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            answers = wikipedia.summary(statement, sentences=1)
            speak("According to Wikipedia")
            print(answers)
            speak(answers)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(3)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(3)

        elif 'open classroom' in statement:
            webbrowser.open_new_tab("https://classroom.google.com")
            speak("Google classroom is open now")
            time.sleep(3)

        elif 'open meet' in statement:
            webbrowser.open_new_tab("https://meet.google.com")
            speak("Google meet is open now")
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(3)

        elif "open github" in statement:
            webbrowser.open_new_tab("https://github.com/")
            speak("Here is github")
            time.sleep(3)

        elif "open tinkerhub" in statement:
            webbrowser.open_new_tab("https://tinkerhub.org/")
            speak("Here is tinkerhub")
            time.sleep(3)

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.thehindu.com/news/")
            speak('Here are some headlines from The Hindu,Happy reading')
            time.sleep(3)

        elif 'time' in statement:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {Time}")

        elif 'weather' in statement:
            news = webbrowser.open_new_tab("https://www.windy.com/?9.963,76.296,5")
            speak('please search your region and get the weather update')
            time.sleep(3)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Olivia is shutting down,Good bye')
            print('your personal assistant Olivia is shutting down,Good bye')
            break

time.sleep(3)
