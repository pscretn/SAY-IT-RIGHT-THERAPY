import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import drivers
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
display = drivers.Lcd()
from lcd_print import lcdprint

record = sr.Recognizer()
startbeep =  AudioSegment.from_wav("/home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/sounds/startbeep.wav")
stopbeep =  AudioSegment.from_wav("/home/pi/SAY-IT-RIGHT-THERAPY/Word_Pronouncing_RaspberryPI/sounds/endbeep.wav")

def  micinput():
    try:
        with sr.Microphone() as mic:
            record.adjust_for_ambient_noise(mic, duration=0.2)
            play(startbeep)
            lcdprint("Listening...")
            audio = record.listen(mic, timeout=1, phrase_time_limit=20)
            display.lcd_clear()
            lcdprint("Thinking...")
            play(stopbeep)
            text = record.recognize_google(audio)
            text = text.lower()
            display.lcd_clear()
            return text
    except :
        pass
    display.lcd_clear()
    display.lcd_backlight(0)
