import wiringpi
import subprocess
import time
button =29
r=28
g=27
b=26
wiringpi.wiringPiSetup()
wiringpi.pinMode(button,0)
wiringpi.pinMode(r,1)
wiringpi.pinMode(g,1)
wiringpi.pinMode(b,1)
#red
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#green
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,0)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#blue
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#yellow
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,0)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#magenta
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#cyan
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
#white
wiringpi.digitalWrite(r,1)
wiringpi.digitalWrite(g,1)
wiringpi.digitalWrite(b,1)
time.sleep(0.2)
wiringpi.digitalWrite(r,0)
wiringpi.digitalWrite(g,0)
wiringpi.digitalWrite(b,0)
subprocess.call(['bash /home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/pronouncing_system.sh'],shell = True)
while(True):
    if wiringpi.digitalRead(button):
        print("killed")
        subprocess.call(['pkill -f rfid_read.py'],shell = True)
        subprocess.call(['bash /home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/pronouncing_system.sh'],shell = True)
