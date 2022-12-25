from dependencies.ListenerEngine import ListenerEngine
from dependencies.SpeakerEngine import SpeakerEngine


def main():
    se = SpeakerEngine(rate=150, voice='m2')
    se.speak("Welcome back, sir")

    le = ListenerEngine()
    while True:
        command = le.listen().lower()

        print("you said: " + command)
        se.speak("you said: " + command)


if __name__ == "__main__":
    main()
