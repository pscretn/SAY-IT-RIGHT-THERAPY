import sys
import random
import json
from time import sleep
from keyboard_input_letter import KeyOut,clr
from speak_text import SpeakText
import wiringpi
import RPi.GPIO as GPIO
import drivers
GPIO.setwarnings(False)
red = 25
green = 24
l1 = 22 #indicator led
wiringpi.wiringPiSetup()
wiringpi.pinMode(red,1)
wiringpi.pinMode(green,1)
wiringpi.pinMode(l1,1)
wiringpi.digitalWrite(red,0)
wiringpi.digitalWrite(green,0)
wiringpi.digitalWrite(l1,0)
display = drivers.Lcd()
display.lcd_backlight(0)
display.lcd_clear()
words = "aeroplane","apple","bat","ball","cat","dog","elephant","fish","frog","giraffe","horse","house","icecream","jelly","kite","lion","monkey","nest","owl","parrot","pig","panda","penguin","queen","rabbit","rhino","snake","tiger","turtle","zebra"

def lcdprint(text,display=display,num_line=1, num_cols=16):
    if len(text)>num_cols:
        display.lcd_display_string(text[:num_cols], num_line)
        sleep(0.2)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.2)
        sleep(0.2)
    else:
        display.lcd_display_string(text,num_line)
        sleep(0.2)

def spelling():
    wiringpi.digitalWrite(l1,1)
    display.lcd_backlight(0)
    word = random.choice(words)
    spell=""
    for i in word:
        spell += i + " "
    SpeakText("Can you enter the spelling of the word " + word)
    uin = KeyOut()
    clr()
    if uin == word:
        #print(word)
        wiringpi.digitalWrite(green,1)
        display.lcd_backlight(1)
        lcdprint(word)
        SpeakText("that is correct , the spelling of" + word + "is " + spell)

    else:
        #print(word)
        wiringpi.digitalWrite(red,1)
        display.lcd_backlight(1)
        lcdprint(word)
        SpeakText("that is wrong , the spelling of" + word + "is " + spell)
    display.lcd_clear()
    display.lcd_backlight(0)
    wiringpi.digitalWrite(red,0)
    wiringpi.digitalWrite(green,0)
    wiringpi.digitalWrite(l1,0)
