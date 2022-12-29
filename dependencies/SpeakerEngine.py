import pyttsx3


class SpeakerEngine:
    '''
    SpeakerEngine initializes the 'engine' for speech capabilities for the assistant. It's defaults are 
    * rate=150
    * voice=f5.\n
    There are other voices available in the host system such as 
    * f1, f2, ...f5
    * mb-us1 (mbrola for less robotic and stiff sound)
    * m1, m2, ...m5
    '''

    def __init__(self, rate: int = 150, voice: str = 'f5'):
        try:
            # initializing the speaking engine
            self.engine = pyttsx3.init()

            # setting voice for speech synthesizer
            self.engine.setProperty('voice', voice)

            # Speech rate set to 150
            self.engine.setProperty('rate', rate)

        except Exception as e:
            print("Error while initializing the Speaker Engine!!!")
            print(e)

    def speak(self, string):
        self.engine.say(string)
        self.engine.runAndWait()
        print("done..")
