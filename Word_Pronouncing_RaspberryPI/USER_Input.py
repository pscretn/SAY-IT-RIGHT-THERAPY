import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)  


try:
    while True:
         button_state = GPIO.input(20)
         if button_state == False:
             GPIO.output(21, True)
             print('Button Pressed...')
             exec(open("Word_Pronouncing_Rpi.py").read())
         else:
             GPIO.output(21, False)
except:
    GPIO.cleanup()
