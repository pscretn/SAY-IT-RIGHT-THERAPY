import sys
import random
sys.path.append("testcodes")
from keyboard_input import KeyOut

def add():
    a = random.randint(0,51)
    b = random.randint(0,51)
    print("What is %d + %d ?" % (a,b))
    c = a + b
    ans = int(KeyOut())
    if ans == c:
        print("Correct answer  %d + %d is %d" % (a,b,c))
    else:
        print("Wrong answer   %d + %d is %d" % (a,b,c))

def sub():
    a = random.randint(0,51)
    b = random.randint(0,a)
    print("What is %d - %d ?" % (a,b))
    c = a - b
    ans = int(KeyOut())
    if ans == c:
        print("Correct answer  %d - %d is %d" % (a,b,c))
    else:
        print("Wrong answer   %d - %d is %d" % (a,b,c))