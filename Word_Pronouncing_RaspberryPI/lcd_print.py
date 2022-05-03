import drivers
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
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
    

