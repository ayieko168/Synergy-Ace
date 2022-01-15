import pyperclip as pp
import time
import random, string
from pynput import keyboard
import socket

## VARIABLES
HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
CLIENTS_LIST = []


## KEYBOARD LISTENER
print(f"Setting up the Keyboard Listener...")
def on_activate():
    print('Global hotkey activated!')
    
    try:
        for client_socket in CLIENTS_LIST:
            for i in range(3):
                clipboard_text = pp.paste()
                client_socket.sendall(str.encode(f"{clipboard_text}"))
                time.sleep(0.1)
    except Exception as e:
        print(f"Exception Server:: {e}")

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+c'), on_activate)

l = keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release))
l.start()

print("Listener Active.")

def get_local_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    
    return str(local_ip)


print(f"Setting up this Computer as a Server...")
print(f"The server IP Address is [{get_local_ip()}]")

# Setup sever socet
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen()
while True:
    
    ## Wait for connection
    client_socket, client_address = soc.accept()
    print(f"[NEW CLIENT] Connected to {client_address}")
    
    ## Add new connection to list
    CLIENTS_LIST.append(client_socket)
    client_socket.send(str.encode('Welcome to the Aces Synergy Universal Clipboard! '))
    


    

    
