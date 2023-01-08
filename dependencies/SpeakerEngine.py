import pyttsx3


class SpeakerEngine:
    '''
    SpeakerEngine initializes the 'engine' for speech capabilities for the assistant. It's defaults are 
    * rate=150
    * voice=male.\n
    There are other voices available in the host system such as 
    * 1 - female
    * 0 - male
    '''

    def __init__(self, rate: int = 150, voice: str = 'f5'):
        try:
            # initializing the speaking engine
            self.engine = pyttsx3.init()

            # setting voice for speech synthesizer
            # 1 is for female and 0 is for male but if female voice
            # is not present it defaults to male
            voices = self.engine.getProperty('voice') 
            self.engine.setProperty('voice', voices[1])

            # Speech rate set to 150
            self.engine.setProperty('rate', rate)

        except Exception as e:
            print("Error while initializing the Speaker Engine!!!")
            print(e)

    def speak(self, string):
        self.engine.say(string)
        self.engine.runAndWait()
        print("done..")
