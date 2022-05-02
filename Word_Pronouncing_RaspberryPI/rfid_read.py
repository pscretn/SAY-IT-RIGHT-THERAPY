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
from simple_maths import add,sub
from count_number import num_count
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
                        print("hat")
                        wordpronouncing("hat")
                elif val[0] == 844850409053:
                        print("aeroplane")
                        wordpronouncing("aeroplane")
                elif val[0] == 399423441364:
                        print("egg")
                        wordpronouncing("egg")
                elif val[0] == 788836979286:
                        print("fan")
                        wordpronouncing("fan")
                elif val[0] == 618787920249:
                        print("ball")
                        wordpronouncing("ball")
                elif val[0] == 168230392398:
                        print("count number")
                        num_count()
                elif val[0] == 293752221425:
                        print("add")
                        add()
                elif val[0] == 912154169348:
                        print("substract")
                        sub()
                elif val[0] == 925553136382:
                        print("Colors")
                        whichcolor()
                elif val[0] == 500762422793:
                        print("random words")
                        wordpronoun()
  
        except:
                pass



