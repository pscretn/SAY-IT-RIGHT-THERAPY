import RPi.GPIO as GPIO
import wiringpi
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()
import drivers
from time import sleep
#from Word_Pronouncing_rfid import wordpronouncing
red = 25
wiringpi.wiringPiSetup()
wiringpi.pinMode(red,1)
display = drivers.Lcd()
display.lcd_clear()
wiringpi.digitalWrite(red,0)
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
        
while True :
        try:
                val = reader.read()
                if val[0] == 223688273618:
                        print("boy")
                        wiringpi.digitalWrite(red, 1)
                        lcdprint(display,"boy",1)
                elif val[0] == 293752221425:
                        print("mango")
                        wiringpi.digitalWrite(red, 1)
                        lcdprint(display,"mango",1)
                elif val[0] == 569479343776:
                        print("orange")
                        wiringpi.digitalWrite(red, 1)
                        lcdprint(display,"orange",1)
                elif val[0] == 500762422793:
                        print("yellow")
                        wiringpi.digitalWrite(red, 1)
                        lcdprint(display,"yellow",1)
                elif val[0] == 500762422793:
                        print("black")
                        wiringpi.digitalWrite(red, 1)
                        lcdprint(display,"black",1)
                
                display.lcd_clear()
                wiringpi.digitalWrite(red, 0)
        except:
                pass
