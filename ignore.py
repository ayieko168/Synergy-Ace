###################################
from pynput import keyboard

def on_activate():
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+c'), on_activate)

with keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)) as l:
    l.join()
    

#####################################
text = ''.join(random.choices( string.ascii_letters+string.digits, k=16 ))

for i in range(4):
    print(f"Copying {text} to clipboard in {4-i}")
    time.sleep(1)

pp.copy(text)
