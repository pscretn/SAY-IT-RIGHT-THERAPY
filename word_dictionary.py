Apple = {'app':1.1 ,"maple":5.0}
Strawberry = {'straw':2.0,'berry':3.0}

def  word_dict(word,wordspoken):
    if word == "apple":
        if Apple.get(wordspoken):
            return int(Apple.get(wordspoken))
        else:
            return 0
    elif word == "strawberry":
        if Strawberry.get(wordspoken):
            return int(Strawberry.get(wordspoken))
        else:
            return 0
