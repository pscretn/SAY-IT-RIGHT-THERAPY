Apple = {'sapple':4.1 ,"maple":4.2,"dupple":4.3,'appel':4.4, 'appell':4.5, 'cappel':3.1, 'chapel':3.2, 'chappel':3.3, 'chappell':2.1, 'chapple':2.2, 'grapple':1.1 }
Strawberry = {'hanberry':4.1,'hansberry':4.2,'dogberry':4.3,'dobberry':4.4,'dobberberry':4.5,'maybury':3.1,'newbury':3.2,'primary':3.3,'scarberry':3.4,'roseberry':2.1,'secondary':2.2,'auberry':1.1}
Girl={'berle':4.1, 'birle':4.2, 'burl':4.3, 'curl':4.4, 'earl':4.5,'hurl':3.1, 'kerl':3.2, 'merl':3.3, 'merle':3.4,'swirl':2.1, 'twirl':2.2,'wurl':1.1}
Boy={'oy':4.1,'oi':4.2,'coy':4.3, 'coye':4.4,'joy':3.2,'ploy':3.3,'toy':2.1,'enjoy':2.2,'roy':2.3,'yoy':1.1}
Cat={'arnatt':4.1, 'at':4.2, 'at-bat':4.3, 'balyeat':3.0, 'bat':2.0,'vat':1.1}
Lion={'ion':4.1,'lyon':4.2,'rion':4.3, 'ryan':3.1, 'ryen':3.2, 'ryon':2.1,'scion':2.2,'dion':1.1}
Dog={'acog':4.1, 'blog':4.2, 'bog':4.3, 'cog':3.1, 'fog':3.2, 'haug':3.3, 'log':2.1, 'snog':2.2, 'zaugg':1.1}

def word_dict(word,wordspoken):
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
    elif word == "girl":
            if Girl.get(wordspoken):
                return int(Girl.get(wordspoken))
            else:
                return 0
    elif word == "boy":
            if Boy.get(wordspoken):
                return int(Boy.get(wordspoken))
            else:
                return 0
    elif word == "cat":
            if Cat.get(wordspoken):
                return int(Cat.get(wordspoken))
            else:
                return 0
    elif word == "lion":
            if Lion.get(wordspoken):
                return int(Lion.get(wordspoken))
            else:
                return 0
    elif word == "dog":
            if Dog.get(wordspoken):
                return int(Dog.get(wordspoken))
            else:
                return 0