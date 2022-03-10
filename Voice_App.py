import speech_recognition as sr
import pyttsx3 as pyx
import random
import pronouncing as pr

record = sr.Recognizer()
hint1 = "Can you repeat after me , the word"
words = "orange","strawberry","apple","man","boy","girl","woman","blue","red"

def SpeakText(voice):
    engine = pyx.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(voice)
    engine.runAndWait()
    engine.stop()

def pronoun(word):
    val=2
    while(val>0):
        print("you said the wrong word , you have "+str(val)+" chances left")
        SpeakText("you said the wrong word , you have "+str(val)+" chances left")
        try:
            with sr.Microphone() as mic:
                record.adjust_for_ambient_noise(mic, duration=0.2)
                print("Listening...")
                audio = record.listen(mic)
                print("Thinking...")
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
                        break
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
            print("Listening...")
            audio = record.listen(mic)
            print("Thinking...")
            text = record.recognize_google(audio)
            text = text.lower()
            checkword(text,word)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
while(True):
    word=random.choice(words)
    print(word)
    SpeakText(hint1+word)
    UserVoice(word)
       