import speech_recognition as sr
import pyttsx3 as pyx
import pronouncing as pr
from pydub import AudioSegment
from pydub.playback import play
import wiringpi
import random
import drivers
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
r=28
g=27
b=26
red = 25
green = 24
blue = 23
l1 = 22 #indicator led
wiringpi.wiringPiSetup()
wiringpi.pinMode(r,1)
wiringpi.pinMode(g,1)
wiringpi.pinMode(b,1)
wiringpi.pinMode(red,1)
wiringpi.pinMode(green,1)
wiringpi.pinMode(blue,1)
wiringpi.pinMode(l1,1)
wiringpi.digitalWrite(red,0)
wiringpi.digitalWrite(green,0)
wiringpi.digitalWrite(blue,0)
wiringpi.digitalWrite(l1,0)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
record = sr.Recognizer()
colors = "red","green","blue","yellow","pink","cyan"
startbeep =  AudioSegment.from_wav("/home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/sounds/startbeep.wav")
stopbeep =  AudioSegment.from_wav("/home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/sounds/endbeep.wav")
display = drivers.Lcd()
display.lcd_backlight(0)

def  micinput():
    try:
        with sr.Microphone() as mic:
            record.adjust_for_ambient_noise(mic, duration=0.2)
            play(startbeep)
            #print("Listening...")
            display.lcd_backlight(1)
            lcdprint(display,"Listening...",1)
            display.lcd_clear()
            display.lcd_backlight(0)
            audio = record.listen(mic,0,2)
            #print("Thinking...")
            display.lcd_backlight(1)
            lcdprint(display,"Thinking...",1)
            display.lcd_clear()
            display.lcd_backlight(0)
            play(stopbeep)
            text = record.recognize_google(audio)
            text = text.lower()
            return text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

def SpeakText(word):
    engine = pyx.init('espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',"english-us")
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(word)
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

def nameofcolor(color):
    wiringpi.digitalWrite(l1,1)
    SpeakText("Can you, Tell me which color is this ?")
    text = micinput()
    if text == color:
        wiringpi.digitalWrite(green,1)
        display.lcd_backlight(1)
        lcdprint(display,"Good",1)
        sleep(0.5)
        display.lcd_clear()
        lcdprint(display,color,1)
        SpeakText("Good, You Said the Name of color Correctly, The color is "+color)
        display.lcd_clear()
        display.lcd_backlight(0)
    else:
        wiringpi.digitalWrite(red,1)
        display.lcd_backlight(1)
        lcdprint(display,"No Problem",1)
        sleep(0.5)
        display.lcd_clear()
        lcdprint(display,color,1)
        SpeakText("No problem, You Said the wrong Name for the color, The color is "+color)
        display.lcd_clear()
        display.lcd_backlight(0)
    wiringpi.digitalWrite(red,0)
    wiringpi.digitalWrite(green,0)
    wiringpi.digitalWrite(l1,0)
    
def whichcolor():
    color = random.choice(colors)
    if color == "red":
        #red
        wiringpi.digitalWrite(r,1)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,0)
        nameofcolor("red")
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,0)
    elif color == "green":
        #green
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,1)
        wiringpi.digitalWrite(b,0)
        nameofcolor("green")
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,0)
    elif color == "blue":
        #blue
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,1)
        nameofcolor("blue")
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,0)
    elif color == "yellow":
        #yellow
        wiringpi.digitalWrite(r,1)
        wiringpi.digitalWrite(g,1)
        wiringpi.digitalWrite(b,0)
        nameofcolor("yellow")
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,0)
    elif color == "pink":
        #pink
        wiringpi.digitalWrite(r,1)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,1)
        nameofcolor("pink")
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,0)
    elif color == "cyan":
        #cyan
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,1)
        wiringpi.digitalWrite(b,1)
        nameofcolor("cyan")
        wiringpi.digitalWrite(r,0)
        wiringpi.digitalWrite(g,0)
        wiringpi.digitalWrite(b,0)

