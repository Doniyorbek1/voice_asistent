import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import playsound

# Ovoz chiqarish (O‘zbek tilida)
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")   

# Nutqni tinglash va matnga aylantirish
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Gapiring...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language="uz-UZ")
            print(f"Siz aytdingiz: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Kechirasiz, tushunolmadim.")
            return None
        except sr.RequestError:
            print("Ovoz xizmatiga ulanishda xatolik.")
            return None

# Ovozli yordamchi
def assistant():
    speak("Salom! Qanday yordam bera olaman?")
    while True:
        command = listen()
        if command:
            if "salom" in command:
                speak("Salom! Sizga qanday yordam bera olaman?")
            elif "ob havo" in command:
                speak("Bugungi ob-havo quyoshli, harorat 25 daraja.")
            elif "xayr" in command or "to‘xtat" in command:
                speak("Xayr! Ko‘rishguncha!")
                break
            else:
                speak("Kechirasiz, bu buyruqni tushunmadim.")

# Yordamchini ishga tushirish
assistant()
