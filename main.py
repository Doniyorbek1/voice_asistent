import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + e)
        return said.lower()

text = get_audio()

if "hello" in text:
    speak('hello what is your name?')
if "what is your name" in text:
    speak('my name is macbook air and mr robot')
    
"""endi qiladigan ishimiz
   men yozmoqchi bo'lgan asistentni ovozli boshqaruvga o'tkazish yani 
   biror buyruq bersangiz uni bajarish"""

