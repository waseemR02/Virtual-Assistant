from dependencies.ListenerEngine import ListenerEngine
from dependencies.SpeakerEngine import SpeakerEngine
from features.greetings import Greetings
from features.temporal import Temporal

import keyboard
import os


class Assistant:
    def __init__(self):
        self.se = SpeakerEngine(rate=130, voice='f4')
        self.le = ListenerEngine()

        self.greetings = Greetings()
        self.temporal = Temporal()

        self.se.speak(self.greetings.wish())

        while True:
            if keyboard.is_pressed("space"):
                self.aware()
            else:
                pass

    def aware(self):
        query = self.le.listen().lower()

        if "about yourself" in query:
            self.se.speak(self.greetings.aboutMe())
            
        elif ("what time is it now" in query) or ("what is the time now" in query) or ("what is the time" in query):
            self.se.speak(self.temporal.timenow())
            
        elif "day is today" in query:
            self.se.speak(self.temporal.daynow())
        
        elif (" is the month" in query) or ("month is it" in query):
            self.se.speak(self.temporal.monthnow())
        
        elif (" is the year" in query) or (" year is it" in query):
            self.se.speak(self.temporal.yearnow())
        
        elif ("is today's date" in query) or ("is the date today" in query):
            self.se.speak(self.temporal.datenow())

        elif "kill your process" in query:
            try:
                print("Terminating..")
                os._exit()
            except:
                print("Error while while terminating!!")

        else:
            self.se.speak("I didn't quite understand you.")
        print(query)


def main():
    Assistant()


if __name__ == "__main__":
    main()
