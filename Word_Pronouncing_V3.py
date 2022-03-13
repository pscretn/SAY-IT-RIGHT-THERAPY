import speech_recognition as sr
import pyttsx3 as pyx
import random
import pronouncing as pr
from pydub import AudioSegment
from pydub.playback import play

record = sr.Recognizer()
hint1 = "Can you repeat after me , the word"
words = "orange","strawberry","apple","man","boy","girl","woman","blue","red"
startbeep =  AudioSegment.from_wav("sounds\startbeep.wav")
stopbeep =  AudioSegment.from_wav("sounds\endbeep.wav")

def  micinput():
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
            return text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

def SpeakText(voice):
    engine = pyx.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(voice)
    engine.runAndWait()
    engine.stop()

def main():
    word = random.choice(words)
    wordpro=""
    for i in pr.phones_for_word(word)[0]:
        if(i.isalpha()):
            wordpro+=i
        elif(i==" "):
            wordpro+=" "
    wordpro = wordpro.lower()
    val=3
    while(val>=0):
        SpeakText(hint1)
        print(wordpro)
        SpeakText(wordpro)
        print(word)
        SpeakText(word)
        wordspoken = micinput()
        if wordspoken == word:
            print("you said the word correctly")
            SpeakText("you said the word correctly")
            break
        else:
            if wordspoken in pr.rhymes(word):
                print("you are closer to the word , you have "+str(val)+" chances left")
                SpeakText("you are closer to the word , you have "+str(val)+" chances left")
            else:
                print("you said the wrong word , you have "+str(val)+" chances left")
                SpeakText("you said the wrong word , you have "+str(val)+" chances left")
        val-=1
if __name__ == '__main__':
    main()
