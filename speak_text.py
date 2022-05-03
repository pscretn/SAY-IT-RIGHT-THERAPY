import pyttsx3 as pyx

def SpeakText(voice):
    engine = pyx.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(voice)
    engine.runAndWait()
    engine.stop()
