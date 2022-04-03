import random
from keyboard_input import KeyOut,clr
import drivers
from time import sleep
from speak_text import SpeakText
import wiringpi
import RPi.GPIO as GPIO
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
        
def add():
    wiringpi.digitalWrite(l1,1)
    a = random.randint(0,51)
    b = random.randint(0,51)
    SpeakText("What is %d + %d ?" % (a,b))
    display.lcd_backlight(1)
    lcdprint(str(a)+" + "+str(b))
    c = a + b
    ans = int(KeyOut())
    clr()
    if ans == c:
        wiringpi.digitalWrite(green,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" + "+str(b)+" = "+str(c))
        SpeakText("Correct answer, %d + %d is %d" % (a,b,c))
        display.lcd_backlight(0)
        display.lcd_clear()
        wiringpi.digitalWrite(green,0)
    else:
        wiringpi.digitalWrite(red,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" + "+str(b)+" = "+str(c))
        SpeakText("Wrong answer, %d + %d is %d" % (a,b,c))
        display.lcd_backlight(0)
        display.lcd_clear()
        wiringpi.digitalWrite(red,0)
    wiringpi.digitalWrite(l1,0)
    display.lcd_backlight(0)

def sub():
    wiringpi.digitalWrite(l1,1)
    a = random.randint(0,51)
    b = random.randint(0,a)
    SpeakText("What is %d - %d ?" % (a,b))
    display.lcd_backlight(1)
    lcdprint(str(a)+" - "+str(b))
    c = a - b
    ans = int(KeyOut())
    clr()
    if ans == c:
        wiringpi.digitalWrite(green,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" - "+str(b)+" = "+str(c))
        SpeakText("Correct answer,  %d - %d is %d" % (a,b,c))
        display.lcd_clear()
        wiringpi.digitalWrite(green,0)
    else:
        wiringpi.digitalWrite(red,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" - "+str(b)+" = "+str(c))
        SpeakText("Wrong answer,   %d - %d is %d" % (a,b,c))
        display.lcd_clear()
        wiringpi.digitalWrite(red,0)
    wiringpi.digitalWrite(l1,0)
    display.lcd_backlight(0)
    

