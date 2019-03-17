"""An automated script to let user to select song of their choice, accessed via number inputs ranging between 1 and 10.
Modules Used: pygame, mixer, os
Libraries Used: pynput, keyboard
"""

import os
file = os.listdir('./')
mp3files = list(filter(lambda f: f.endswith('.mp3') ,file))
# print(mp3files)

#Taking keyboard input
from pynput import keyboard
#For audio files
from pygame import mixer
#Intializing mixer
mixer.init()

def on_press(key):
    #Check for an error
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        # pass
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))

    #For space, alt, shift, backspace,caps,  enter, fucntion key, ctlr
    if key == keyboard.Key.space or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl_l or key ==keyboard.Key.alt or key == keyboard.Key.caps_lock or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key==keyboard.Key.backspace or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r or key == keyboard.Key.shift or key == keyboard.Key.enter or key == keyboard.Key.down or key == keyboard.Key.up or key == keyboard.Key.right or key == keyboard.Key.left or key == keyboard.Key.num_lock or key == keyboard.Key.page_down or key == keyboard.Key.page_up or key == keyboard.Key.home or key == keyboard.Key.end or key == keyboard.Key.insert or key == keyboard.Key.delete or key == keyboard.Key.tab:
        return True

    #For escape 
    if key == keyboard.Key.esc:
        return False
    global mp3files
    lists=[]
    for i in range(0, 11):
        lists.append(str(i))
    if key.char:
        if key.char in lists:
            if int(key.char)<len(mp3files):
                mixer.music.load(mp3files[int(key.char)])
                mixer.music.play()
        else:
            pass
    else:
        pass

# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
