from pynput.keyboard import Key, Listener,KeyCode
val =''
def KeyPress(key):
    global val
    if key == KeyCode(char='1') or hasattr(key, 'vk') and key.vk == 97:
        val+= '1'
    elif key == KeyCode(char='2') or hasattr(key, 'vk') and key.vk == 98:
        val+= '2'
    elif key == KeyCode(char='3') or hasattr(key, 'vk') and key.vk == 99 :
        val+= '3'
    elif key == KeyCode(char='4') or hasattr(key, 'vk') and key.vk == 100:
        val+= '4'
    elif key == KeyCode(char='5') or hasattr(key, 'vk') and key.vk == 101:
        val+= '5'
    elif key == KeyCode(char='6') or hasattr(key, 'vk') and key.vk == 102:
        val+= '6'
    elif key == KeyCode(char='7') or hasattr(key, 'vk') and key.vk == 103:
        val+= '7'
    elif key == KeyCode(char='8') or hasattr(key, 'vk') and key.vk == 104:
        val+= '8'
    elif key == KeyCode(char='9') or hasattr(key, 'vk') and key.vk == 105:
        val+= '9' 
    elif key == KeyCode(char='0') or hasattr(key, 'vk') and key.vk == 96:
        val+= '0'
    elif key == KeyCode(char='q'):
        val+= 'q'
    elif key == KeyCode(char='w'):
        val+= 'w'  
    elif key == KeyCode(char='e'):
        val+= 'e'  
    elif key == KeyCode(char='r'):
        val+= 'r'  
    elif key == KeyCode(char='t'):
        val+= 't'  
    elif key == KeyCode(char='y'):
        val+= 'y'  
    elif key == KeyCode(char='u'):
        val+= 'u'  
    elif key == KeyCode(char='i'):
        val+= 'i'  
    elif key == KeyCode(char='o'):
        val+= 'o'   
    elif key == KeyCode(char='p'):
        val+= 'p'
    elif key == KeyCode(char='a'):
        val+= 'a'  
    elif key == KeyCode(char='s'):
        val+= 's'  
    elif key == KeyCode(char='d'):
        val+= 'd'  
    elif key == KeyCode(char='f'):
        val+= 'f'  
    elif key == KeyCode(char='g'):
        val+= 'g'  
    elif key == KeyCode(char='h'):
        val+= 'h'  
    elif key == KeyCode(char='j'):
        val+= 'j'  
    elif key == KeyCode(char='k'):
        val+= 'k' 
    elif key == KeyCode(char='l'):
        val+= 'l'
    elif key == KeyCode(char='z'):
        val+= 'z'  
    elif key == KeyCode(char='x'):
        val+= 'x'  
    elif key == KeyCode(char='c'):
        val+= 'c'  
    elif key == KeyCode(char='v'):
        val+= 'v'  
    elif key == KeyCode(char='b'):
        val+= 'b'  
    elif key == KeyCode(char='n'):
        val+= 'n'    
    elif key == Key.space:
        val+= ' '
    elif key == Key.enter:
        return False
    elif key == Key.backspace:
        val = val[:-1]

def KeyOut():
    with Listener(on_press = KeyPress) as listener:   
        listener.join()
    return val

