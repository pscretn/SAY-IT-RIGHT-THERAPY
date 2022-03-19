import speech_recognition as sr
import pyttsx3 as pyx
import random
import pronouncing as pr
from pydub import AudioSegment
from pydub.playback import play
import drivers
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)#red
GPIO.setup(19, GPIO.OUT)#blue
GPIO.setup(13, GPIO.OUT)#green  
record = sr.Recognizer()
hint1 = "Can you repeat after me , the word"
words = "orange","strawberry","apple","man","boy","girl","blue","red"
startbeep =  AudioSegment.from_wav("sounds/startbeep.wav")
stopbeep =  AudioSegment.from_wav("sounds/endbeep.wav")
display = drivers.Lcd()
GPIO.output(26, False)
GPIO.output(19, False)
GPIO.output(13, False)
def  micinput():
    try:
        with sr.Microphone() as mic:
            record.adjust_for_ambient_noise(mic, duration=0.2)
            play(startbeep)
            print("Listening...")
            lcdprint(display,"Listening...",1)
            display.lcd_clear()
            audio = record.listen(mic)
            print("Thinking...")
            lcdprint(display,"Thinking...",1)
            display.lcd_clear()
            play(stopbeep)
            text = record.recognize_google(audio)
            text = text.lower()
            return text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

def SpeakText(voice):
    engine = pyx.init('espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',"english-us")
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(voice)
    engine.runAndWait()
    engine.stop()
    
def lcdprint(display, text, num_line=1, num_cols=16):
    if len(text)>num_cols:
        display.lcd_display_string(text[:num_cols], num_line)
        sleep(1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.2)
        sleep(1)
    else:
        display.lcd_display_string(text,num_line)
        sleep(1)
            

        
def main():
    #word = random.choice(words)
    word = "strawberry"
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
        lcdprint(display,wordpro,1)
        display.lcd_clear()
        print(wordpro)
        SpeakText(wordpro)
        lcdprint(display,word,1)
        display.lcd_clear()
        print(word)
        SpeakText(word)
        wordspoken = micinput()
        if wordspoken == word:
            #print("you said the word correctly")
            GPIO.output(13, True)
            lcdprint(display,"you said the word correctly",1)
            SpeakText("you said the word correctly")
            display.lcd_clear()
            
            break
        else:
            if wordspoken in pr.rhymes(word):
                #print("you are closer to the word , you have "+str(val)+" chances left")
                GPIO.output(19, True)
                lcdprint(display,"you are closer to the word , you have "+str(val)+" chances left",1)
                SpeakText("you are closer to the word , you have "+str(val)+" chances left")
                display.lcd_clear()
            else:
                #print("you said the wrong word , you have "+str(val)+" chances left")
                GPIO.output(26, True)
                lcdprint(display,"you said the wrong word , you have "+str(val)+" chances left",1)
                SpeakText("you said the wrong word , you have "+str(val)+" chances left")
                display.lcd_clear()
            GPIO.output(19, False)
            GPIO.output(26, False)
        val-=1
    GPIO.output(26, False)
    GPIO.output(13, False)
    GPIO.output(19, False)
if __name__ == '__main__':
    main()
