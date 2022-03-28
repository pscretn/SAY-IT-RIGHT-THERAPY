import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()
import wiringpi
import time
import drivers
from word_pron_rfid import wordpronouncing
from word_pron_random import wordpronoun
from identify_color import whichcolor
r=28
g=27
b=26
wiringpi.wiringPiSetup()
wiringpi.pinMode(r,1)
wiringpi.pinMode(g,1)
wiringpi.pinMode(b,1)
#red
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#green
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,0)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#blue
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#yellow
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,0)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#magenta
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#cyan
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#white
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
display = drivers.Lcd()
display.lcd_backlight(0)
while True :
        try:
                val = reader.read()
                if val[0] == 223688273618:
                        print("boy")
                        wordpronouncing("boy")
                elif val[0] == 293752221425:
                        print("mango")
                        wordpronouncing("mango")
                elif val[0] == 569479343776:
                        print("orange")
                        wordpronouncing("orange")
                elif val[0] == 500762422793:
                        print("yellow")
                        wordpronouncing("yellow")
                elif val[0] == 925553136382:
                        print("Colors")
                        whichcolor()
                else:
                        print("Random")
                        wordpronoun()
        except:
                pass



