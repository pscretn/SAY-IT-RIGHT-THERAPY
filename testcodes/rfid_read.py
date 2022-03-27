import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()

def rfidread():
        try:
            print("reading")    
            val = reader.read()
            
            print(val[0])
        except:
            pass

rfidread()
