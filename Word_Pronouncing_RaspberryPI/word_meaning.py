import sys
import drivers
import json
from time import sleep
from keyboard_input_letter import KeyOut,clr
from speak_text import SpeakText
import wiringpi
import RPi.GPIO as GPIO
import drivers


GPIO.setwarnings(False)
l1 = 22 #indicator led
words = json.load(open('/home/pi/SAY-IT-RIGHT-THERAPY/json_file/dictionary.json'))
wiringpi.wiringPiSetup()
wiringpi.pinMode(l1,1)
wiringpi.digitalWrite(l1,0)
display = drivers.Lcd()
display.lcd_backlight(0)
display.lcd_clear()

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

def wordmeaning():
    display.lcd_backlight(0)
    wiringpi.digitalWrite(l1,1)
    SpeakText("Enter the word you want to know the meaning of")
    print("Enter the word you want to know the meaning of:")
    word = KeyOut()
    word = word.lower()
    clr()
    display.lcd_backlight(0)
    if(words.get(word)):
        display.lcd_backlight(1)
        lcdprint(word)
        SpeakText("The meaning of "+word+" is ")
        display.lcd_clear()
        SpeakText(words.get(word))
    else:
        display.lcd_backlight(1)
        lcdprint("Not Found")
        SpeakText("Word not found")
        print("Word not found")
        display.lcd_clear()
    display.lcd_backlight(0)
    wiringpi.digitalWrite(l1,0)

