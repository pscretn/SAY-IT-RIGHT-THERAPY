import multiprocessing
import pyttsx3 as pyt
from pynput.keyboard import Listener,KeyCode

def KeyPress(key):
	if key == KeyCode(char='q'):
		return False

def KeyOut():
    with Listener(on_press = KeyPress) as listener:   
        listener.join()
def sayFunc(phrase):
    engine = pyt.init()
    engine.setProperty('rate', 160)
    engine.say(phrase)
    engine.runAndWait()

def say(phrase):
	if __name__ == "__main__":
		p = multiprocessing.Process(target=sayFunc, args=(phrase,))
		q = multiprocessing.Process(target=KeyOut)
		p.start()
		q.start()
		while p.is_alive():
			if q.is_alive() == False:
				p.terminate()
			else:
				continue
		p.join()
		q.terminate()


say("this process is running right now, press q to stop say the word")