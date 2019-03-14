"""An automated script to let user to select song of their choice, accessed via number inputs.
Modules Used: pynput, pygame
Libraries Used: keyboard, mixer
"""
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
    #TODO: To let the input be in
    if key == keyboard.Key.space or key == keyboard.Key.ctrl_r or key == keyboard.Key.ctrl_l or key ==keyboard.Key.alt or key == keyboard.Key.caps_lock or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key==keyboard.Key.backspace or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r or key == keyboard.Key.shift or key == keyboard.Key.enter or key == keyboard.Key.down or key == keyboard.Key.up or key == keyboard.Key.right or key == keyboard.Key.left or key == keyboard.Key.num_lock or key == keyboard.Key.page_down or key == keyboard.Key.page_up or key == keyboard.Key.home or key == keyboard.Key.end or key == keyboard.Key.insert or key == keyboard.Key.delete or key == keyboard.Key.tab:
        return True

    #TODO: To terminate the program
    #For escpae 
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key.char:
        if key.char == '1':
            mixer.music.load("Starboy.mp3")
            mixer.music.play()
        elif key.char == '2':
            mixer.music.load("Major.mp3")
            mixer.music.play()

#TODO: Access the input
# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()