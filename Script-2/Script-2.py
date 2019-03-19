"""An automated script to produce beeps on press of keys. This is for aged people, to ensure them whether a key has been pressed or not."""
"""
Modules Used: pynput, pygame
Libraries Used: keyboard, winsound, mixer
"""

#importing time
import time
#importing winsound for a beep
import winsound
#Taking keyboard input
from pynput import keyboard
# from pynput.keyboard import Key, Controller
#For audio files
from pygame import mixer
#Intializing mixer
mixer.init()

def on_press(key):
    time.sleep(0.00000000000001)
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    print("A special key has been pressed")
    #Check for an error
    # try:
    #     print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #     # pass
    #     print('special key {0} pressed'.format(key))
    pass

def on_release(key):
    print('{0} released'.format(key))
    #For space, alt, shift, backspace,caps,  enter, function key, ctlr
    if key == keyboard.Key.space or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl_l or key ==keyboard.Key.alt or key == keyboard.Key.caps_lock or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key==keyboard.Key.backspace or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r or key == keyboard.Key.shift or key == keyboard.Key.enter or key == keyboard.Key.down or key == keyboard.Key.up or key == keyboard.Key.right or key == keyboard.Key.left or key == keyboard.Key.num_lock or key == keyboard.Key.page_down or key == keyboard.Key.page_up or key == keyboard.Key.home or key == keyboard.Key.end or key == keyboard.Key.insert or key == keyboard.Key.delete or key == keyboard.Key.tab:
        return True

    #For escpae 
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key.char:
        pass

# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
