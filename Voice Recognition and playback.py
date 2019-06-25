import speech_recognition as sr
import os
from gtts import gTTS
mic_name="Microphone Array"
sample_rate=48000
chunk_size=2048
r = sr.Recognizer()
welcome="Hello. Please Say something"
tts0=gTTS(welcome,lang='en')
tts0.save('welcome.mp3')

with sr.Microphone(sample_rate=sample_rate,chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    os.system("welcome.mp3")
    audio = r.listen(source)

try:
    check=r.recognize_google(audio)
    print(check)
    # check="Hello Nitasha Gupta. Good morning!"
    tts=gTTS("Did you say "+check,lang='en')
    tts.save("speech.mp3")
    os.system("speech.mp3")
except sr.UnknownValueError:
    error="Google  Speech Recognition could not understand audio!"
    tts2=gTTS(error,lang='en')
    tts2.save("error.mp3")
    os.system("error.mp3")
    print(error)
except sr.RequestError as e:
    print("Could not request results from Google speech Recognition services; {0}".format(e))


