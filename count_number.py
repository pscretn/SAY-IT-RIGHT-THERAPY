from speak_text import SpeakText
from mic_input import micinput

def num_count():
    val=""
    SpeakText("Can you Count numbers")
    number = micinput()
    print(number)
    count = 0
    c=0
    if " " in number:
        for i in number:
            if(i !=" "):
                val+=i
            else:
                c+=1
                if str(c) == val:
                    count+=1
                val=""
        if val != "":
            c+=1
            if str(c) == val:
                count+=1
    else:
        for i in number:
            c+=1
            if str(c) == i:
                count+=1
    if(count > 0):
        SpeakText("You have counted upto "+str(count))

num_count()