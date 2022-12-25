import speech_recognition as sr


class ListenerEngine:
    '''
    ListenerEngine initializes the 'engine' for listening the commands from the user and transcripts it for further processing. It uses the google public api so it's not a long term solution but it works for now.
        \n
        Defaults:
        * device : 0 (microphone)
        * timeout : 3 seconds
        * language : english US
    '''

    def __init__(self, device: int = 0, timeout: int = 3, language: str = 'en-us'):

        self.device = device
        self.timeout = timeout
        self.language = language

        # intializing an instance for recognizing
        self.listener = sr.Recognizer()

    def listen(self):

        with sr.Microphone(device_index=self.device) as source:
            self.listener.adjust_for_ambient_noise(source)
            print('listening...')
            audio = self.listener.listen(source, timeout=self.timeout)

        try:
            print("transcripting...")
            command = self.listener.recognize_google(
                audio, language=self.language)
        except Exception as e:
            print("Error while transcripting!!! or no command was given")
            print(e)

        return command
