import speech_recognition as sr
import pyttsx3 as pyx
import random
import pronouncing as pr
from pydub import AudioSegment
from pydub.playback import play

record = sr.Recognizer()
hint1 = "Can you repeat after me , the word"
words = "orange","strawberry","apple","man","boy","girl","woman","blue","red"
startbeep =  AudioSegment.from_wav("sounds/startbeep.wav")
stopbeep =  AudioSegment.from_wav("sounds/endbeep.wav")
def SpeakText(voice):
    engine = pyx.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    engine.say(voice)
    engine.runAndWait()
    engine.stop()

def pronoun(word):
    val=4
    simword=False
    while(val>0):
        if simword==False:
            print("you said the wrong word , you have "+str(val)+" chances left")
            SpeakText("you said the wrong word , you have "+str(val)+" chances left")
        else:
            simword=False
        try:
            with sr.Microphone() as mic:
                SpeakText(hint1+word)
                print(word)
                record.adjust_for_ambient_noise(mic, duration=0.2)
                play(startbeep)
                print("Listening...")
                audio = record.listen(mic)
                print("Recognizing...")
                play(stopbeep)
                text = record.recognize_google(audio)
                text = text.lower()
                test=False
                if text == word:
                    print("you said the word correctly")
                    SpeakText("you said the word correctly")
                    break
                else:
                    for word1 in pr.rhymes(word):
                        if(text==word1):
                            test=True
                            break
                    if(test):
                        print("You are closer to the word")
                        SpeakText("You are closer to the word")
                        simword=True
                    val-=1
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            val-=1
        except sr.UnknownValueError:
            print("unknown error occured")
            val-=1
    if(val==0):
        print("Not a problem , Let's try other word")
        SpeakText("Not a problem , Let's try other word")
def checkword(text,word):
    if text == word:
        print("you said the word correctly")
        SpeakText("you said the word correctly")
    else:
        pronoun(word)



def  UserVoice(word):
    try:
        with sr.Microphone() as mic:
            record.adjust_for_ambient_noise(mic, duration=0.2)
            play(startbeep)
            print("Listening...")
            audio = record.listen(mic)
            print("Thinking...")
            play(stopbeep)
            text = record.recognize_google(audio)
            text = text.lower()
            checkword(text,word)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

word=random.choice(words)
print(word)
SpeakText(hint1+word)
UserVoice(word)
       
