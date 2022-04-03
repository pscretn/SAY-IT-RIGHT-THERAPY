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