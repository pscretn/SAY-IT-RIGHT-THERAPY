import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play


record = sr.Recognizer()
startbeep =  AudioSegment.from_wav("/home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/sounds/startbeep.wav")
stopbeep =  AudioSegment.from_wav("/home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/sounds/endbeep.wav")

def  micinput():
    try:
        with sr.Microphone() as mic:
            record.adjust_for_ambient_noise(mic, duration=0.2)
            play(startbeep)
           # print("Listening...")
            audio = record.listen(mic, timeout=1, phrase_time_limit=20)
        
            #print("Thinking...")
            play(stopbeep)
            text = record.recognize_google(audio)
            text = text.lower()
            return text
    except :
        pass
