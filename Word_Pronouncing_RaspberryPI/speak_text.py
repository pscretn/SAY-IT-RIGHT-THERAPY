import pyttsx3 as pyx


def SpeakText(voice):
    engine = pyx.init('espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',"english-us")
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(voice)
    engine.runAndWait()
    engine.stop()

    
