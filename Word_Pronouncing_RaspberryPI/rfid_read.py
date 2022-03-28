import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()
import drivers
from word_pron_rfid import wordpronouncing
from word_pron_random import wordpronoun
from identify_color import whichcolor
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



