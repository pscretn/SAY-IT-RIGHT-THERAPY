import random
from keyboard_input_num import KeyOut,clr
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

def mul():
    wiringpi.digitalWrite(l1,1)
    a = random.randint(0,51)
    b = random.randint(0,51)
    SpeakText("What is %d * %d ?" % (a,b))
    display.lcd_backlight(1)
    lcdprint(str(a)+" * "+str(b))
    c = a * b
    ans = int(KeyOut())
    clr()
    if ans == c:
        wiringpi.digitalWrite(green,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" * "+str(b)+" = "+str(c))
        SpeakText("Correct answer,  %d * %d is %d" % (a,b,c))
        display.lcd_clear()
        wiringpi.digitalWrite(green,0)
    else:
        wiringpi.digitalWrite(red,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" * "+str(b)+" = "+str(c))
        SpeakText("Wrong answer,   %d * %d is %d" % (a,b,c))
        display.lcd_clear()
        wiringpi.digitalWrite(red,0)
    wiringpi.digitalWrite(l1,0)
    display.lcd_backlight(0)

def div():
    wiringpi.digitalWrite(l1,1)
    a = random.randint(0,51)
    
    if a%19==0:
        b=19
    elif a%18==0:
        b=18
    elif a%17==0:
        b=17
    elif a%16==0:
        b=16
    elif a%15==0:
        b=15
    elif a%14==0:
        b=14
    elif a%13==0:
        b=13
    elif a%12==0:
        b=12
    elif a%11==0:
        b=11
    elif a%10==0:
        b=10
    elif a%9==0:
        b=9
    elif a%8==0:
        b=8
    elif a%7==0:
        b=7
    elif a%6==0:
        b=6
    elif a%5==0:
        b=5
    elif a%4==0:
        b=4
    elif a%3==0:
        b=3
    elif a%2==0:
        b=2
    else:
        b=1
    
    SpeakText("What is %d / %d ?" % (a,b))
    display.lcd_backlight(1)
    lcdprint(str(a)+" / "+str(b))
    c = a / b
    ans = int(KeyOut())
    clr()
    if ans == c:
        wiringpi.digitalWrite(green,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" / "+str(b)+" = "+str(c))
        SpeakText("Correct answer,  %d / %d is %d" % (a,b,c))
        display.lcd_clear()
        wiringpi.digitalWrite(green,0)
    else:
        wiringpi.digitalWrite(red,1)
        display.lcd_backlight(1)
        lcdprint(str(a)+" / "+str(b)+" = "+str(c))
        SpeakText("Wrong answer,   %d / %d is %d" % (a,b,c))
        display.lcd_clear()
        wiringpi.digitalWrite(red,0)
    wiringpi.digitalWrite(l1,0)
    display.lcd_backlight(0)
