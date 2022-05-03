import sys
import json
from unicodedata import unidata_version

from pyparsing import locatedExpr
sys.path.append("testcodes")
from keyboard_input import KeyOut
from speak_text import SpeakText
words = json.load(open('json_file/dictionary.json'))

def word_meaning():
    SpeakText("Enter the word you want to know the meaning of")
    print("Enter the word you want to know the meaning of:")
    word = KeyOut()
    if(words.get(word)):
        SpeakText("The meaning of "+word+" is ")
        SpeakText(words.get(word))
    else:
        SpeakText("Word not found")
        print("Word not found")
word_meaning()