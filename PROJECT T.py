# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:09:46 2022

@author: SAI
"""

import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as data_taker:
     print("Say Something")
    voice = listener.listen(data_taker)
    instruct = listener.recognize_google(voice)
    instruct = instruct.lower()
    print(instruct)
except:
    pass
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as data_taker:
     print("Say Something")
    voice = listener.listen(data_taker)
    instruct = listener.recognize_google(voice)
    instruct = instruct.lower()
    print(instruct)
    if'Max' in instruct:
        print(instruct)
except:
    pass
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Hello how are u ')
engine.say('Hey what you want')
engine.say('what is your hobby?')
engine.say('play the song srivali')
engine.runAndWait()

try:
    with sr.Microphone() as data_taker:
        print("Say Something")
        voice = listener.listen(data_taker)
        instruct = listener.recognize_google(voice)
        instruct = instruct.lower()
        print(instruct)
        if'Max' in instruct:
            print(instruct)
except:
    pass




