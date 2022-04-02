
import random
import pronouncing as pr
from word_dictionary import word_dict
from mic_input import micinput
from speak_text import SpeakText

hint1 = "Can you repeat after me , the word"
words = "lion","girl","boy"


def main():
    #word = random.choice(words)
    word = "boy"
    wordpro=""
    for i in pr.phones_for_word(word)[0]:
        if(i.isalpha()):
            wordpro+=i
        elif(i==" "):
            wordpro+=" "
    wordpro = wordpro.lower()
    val=3
    while(val>=0):
        SpeakText(hint1)
        print(wordpro)
        SpeakText(wordpro)
        print(word)
        SpeakText(word)
        wordspoken = micinput()
        if wordspoken == word:
            print("you said the word correctly")
            SpeakText("you said the word correctly")
            break
        else:
            points = word_dict(word,wordspoken)
            if points > 0:
                print("you are closer to the word ,your score is "+str(points)+" , you have "+str(val)+" chances left")
                SpeakText("you are closer to the word ,your score is "+str(points)+" , you have "+str(val)+" chances left")
            else:
                print("you said the wrong word , you have "+str(val)+" chances left")
                SpeakText("you said the wrong word , you have "+str(val)+" chances left")
        val-=1
if __name__ == '__main__':
    main()
