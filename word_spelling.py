import sys
import random
sys.path.append("testcodes")
from speak_text import SpeakText
from keyboard_input import KeyOut
words = "aeroplane","apple","bat","ball","cat","dog","elephant","fish","frog","giraffe","horse","house","icecream","jelly","kite","lion","monkey","nest","owl","parrot","pig","panda","penguin","queen","rabbit","rhino","snake","tiger","turtle","zebra"
def spelling():
    word = random.choice(words)
    spell=""
    for i in word:
        spell += i + " "
    SpeakText("Can you enter the spelling of the word " + word)
    uin = KeyOut()
    if uin == word:
        print(word)
        SpeakText("that is correct , the spelling of" + word + "is " + spell)

    else:
        print(word)
        SpeakText("that is wrong , the spelling of" + word + "is " + spell)
spelling()