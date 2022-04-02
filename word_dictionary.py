import json
words = json.load(open('json_file/words.json'))


def word_dict(word,wordspoken):
    if word == "apple":
        if words["Apple"].get(wordspoken):
            return int(words["Apple"].get(wordspoken))
        else:
            return 0
    elif word == "strawberry":
        if words["Strawberry"].get(wordspoken):
            return int(words["Strawberry"].get(wordspoken))
        else:
            return 0
    elif word == "girl":
            if words["Girl"].get(wordspoken):
                return int(words["Girl"].get(wordspoken))
            else:
                return 0
    elif word == "boy":
            if words["Boy"].get(wordspoken):
                return int(words["Boy"].get(wordspoken))
            else:
                return 0
    elif word == "cat":
            if words["Cat"].get(wordspoken):
                return int(words["Cat"].get(wordspoken))
            else:
                return 0
    elif word == "lion":
            if words["Lion"].get(wordspoken):
                return int(words["Lion"].get(wordspoken))
            else:
                return 0
    elif word == "dog":
            if words["Dog"].get(wordspoken):
                return int(words["Dog"].get(wordspoken))
            else:
                return 0