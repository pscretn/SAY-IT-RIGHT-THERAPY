import wiringpi
import time
ledPin = 25
button=24
wiringpi.wiringPiSetup()
wiringpi.pinMode(ledPin,1)
wiringpi.pinMode(button,0)
while(True):
    print(wiringpi.digitalRead(24))
    wiringpi.digitalWrite(ledPin,1)
    time.sleep(0.5)
    wiringpi.digitalWrite(ledPin, 0)
    time.sleep(0.5)
