from pynput.keyboard import Key, Listener,KeyCode
import drivers
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
val =''
display = drivers.Lcd()
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

def KeyPress(key):
    global val
    if key == KeyCode(char='1') or hasattr(key, 'vk') and key.vk == 97:
        val+= '1'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='2') or hasattr(key, 'vk') and key.vk == 98:
        val+= '2'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='3') or hasattr(key, 'vk') and key.vk == 99 :
        val+= '3'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='4') or hasattr(key, 'vk') and key.vk == 100:
        val+= '4'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='5') or hasattr(key, 'vk') and key.vk == 101:
        val+= '5'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='6') or hasattr(key, 'vk') and key.vk == 102:
        val+= '6'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='7') or hasattr(key, 'vk') and key.vk == 103:
        val+= '7'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='8') or hasattr(key, 'vk') and key.vk == 104:
        val+= '8'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='9') or hasattr(key, 'vk') and key.vk == 105:
        val+= '9'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='0') or hasattr(key, 'vk') and key.vk == 96:
        val+= '0'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='q'):
        val+= 'q'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='w'):
        val+= 'w'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='e'):
        val+= 'e'
        display.lcd_clear()
        lcdprint(val)  
    elif key == KeyCode(char='r'):
        val+= 'r'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='t'):
        val+= 't' 
        display.lcd_clear()
        lcdprint(val) 
    elif key == KeyCode(char='y'):
        val+= 'y'
        display.lcd_clear()
        lcdprint(val)  
    elif key == KeyCode(char='u'):
        val+= 'u'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='i'):
        val+= 'i'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='o'):
        val+= 'o'   
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='p'):
        val+= 'p'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='a'):
        val+= 'a'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='s'):
        val+= 's'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='d'):
        val+= 'd'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='f'):
        val+= 'f'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='g'):
        val+= 'g'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='h'):
        val+= 'h'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='j'):
        val+= 'j'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='k'):
        val+= 'k' 
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='l'):
        val+= 'l'
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='z'):
        val+= 'z'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='x'):
        val+= 'x'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='c'):
        val+= 'c'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='v'):
        val+= 'v'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='b'):
        val+= 'b'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='n'):
        val+= 'n'  
        display.lcd_clear()
        lcdprint(val)
    elif key == KeyCode(char='m'):
        val+= 'm'  
        display.lcd_clear()
        lcdprint(val)
    elif key == Key.space:
        val+= ' '
        display.lcd_clear()
        lcdprint(val)
    elif key == Key.enter:
        display.lcd_clear()
        return False
    elif key == Key.backspace:
        val = val[:-1]
        display.lcd_clear()
        lcdprint(val)

def KeyOut():
    global val
    with Listener(on_press = KeyPress) as listener:   
        listener.join()
    return val
def clr():
    global val
    val=""
