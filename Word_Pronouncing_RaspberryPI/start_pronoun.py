import wiringpi
import subprocess
import time
button =29
wiringpi.wiringPiSetup()
wiringpi.pinMode(button,0)
subprocess.call(['bash /home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/pronouncing_system.sh'],shell = True)
while(True):
    if wiringpi.digitalRead(button):
        print("killed")
        subprocess.call(['pkill -f rfid_read.py'],shell = True)
        subprocess.call(['bash /home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/pronouncing_system.sh'],shell = True)
