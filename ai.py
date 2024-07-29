import pyttsx3      #ctrl+x # ctrl+slash/ #install pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak('good morning!')
    
    elif hour>=12 and hour<18:
        speak(' good afternoon')
    else:
        speak('good evening')
    speak("I AM OID SIR, PLEASE TELL ME HOW MAY I HELP YOU!")
def takecommand():
# it takes microophone input from the user and written string output
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print('listening...')
        r.pause_threshold = 0.5
        audio=r.listen(source)

    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")#f string
    
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "NONE"
    return query
     

if __name__=='__main__':
    wishme()
    while True:
      query = takecommand().lower()
    #logic for exceuting tasks based on query
      if 'wikipedia' in query:
          speak('SEARCHING WIKIKPEDIA....')
          query = query.replace('wikipedia','')
          results = wikipedia.summary(query,sentences=20)
          speak('according to wikipedia')
          print(results)
          speak(results)
      elif'open youtube'in query:
          webbrowser.open("youtube.com")
    
      elif'open google'in query:
          webbrowser.open("google.com")

    #   elif'play music'in query:
    #       webbrowser.open("youtube.com")
      elif 'the time' in query:
          strtime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f" sir the time is{strtime}")
