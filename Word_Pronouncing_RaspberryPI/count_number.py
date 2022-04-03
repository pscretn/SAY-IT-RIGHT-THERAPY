from speak_text import SpeakText
from mic_input import micinput
import wiringpi
import drivers
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep

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

def num_count():
    wiringpi.digitalWrite(l1,1)
    val=""
    SpeakText("Can you Count numbers")
    number = micinput()
    #print(number)
    count = 0
    c=0
    try:
        if ' ' in number:
            for i in number:
                if(i !=" "):
                    val+=i
                else:
                    c+=1
                    if str(c) == val:
                        count+=1
                    val=""
            if val != "":
                c+=1
                if str(c) == val:
                    count+=1
        else:
            for i in number:
                c+=1
                if str(c) == i:
                    count+=1
    except:
        pass
    if(count > 0):
        wiringpi.digitalWrite(green,1)
        display.lcd_backlight(1)
        lcdprint("1 - "+str(count))
        SpeakText("You have counted upto "+str(count))
        display.lcd_clear()
        wiringpi.digitalWrite(green,0)
    else:
        wiringpi.digitalWrite(red,1)
        display.lcd_backlight(1)
        lcdprint("Try Later")
        SpeakText("okay no problem, lets try again later")
        display.lcd_clear()
        wiringpi.digitalWrite(red,0)
    wiringpi.digitalWrite(l1,0)
    display.lcd_backlight(0)

