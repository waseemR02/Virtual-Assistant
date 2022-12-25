import speech_recognition as sr
recording = sr.Recognizer()

with sr.Microphone(device_index=0) as source: 
	recording.adjust_for_ambient_noise(source)
	print("Please Say something:")
	audio = recording.listen(source, timeout=3)

try:
	print("You said: \n" + recording.recognize_google(audio))
except Exception as e:
	print(e)
