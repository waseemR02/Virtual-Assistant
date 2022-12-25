import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'f5')
rate = 140
engine.setProperty('rate', rate)
engine.say('konnichiwa , What would you like me to do? ')

engine.runAndWait()