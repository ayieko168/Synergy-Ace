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
        for i in range(2):
            clipboard_text = pp.paste()
            client_socket.send(str.encode(f"{clipboard_text}"))
            time.sleep(0.1)
    except:
        pass

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

server_running = input("Is there a server already running? ([Y]es/[N]o)\n[Default = No] >>> ").lower()

# Chose how to start the socket, as a server or as a client
if server_running.strip() == '': server_running = 'n'
if server_running in ['n', 'no']:
    print(f"Setting up this Computer as a Server...")
    print(f"The server IP Address is [{get_local_ip()}]")
    
    # Setup sever socet
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((HOST, PORT))
    soc.listen()
    while True:
        client_socket, client_address = soc.accept()
        print(f"[NEW CLIENT] Connected to {client_address}")
        client_socket.send(str.encode('Welcome to the Aces Synergy Universal Clipboard! '))
    
else:
    
    print("Setting up this computer as a client...")
    server_ip = input(f"Enter the IP of the server\n >>> ")
    
    soct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soct.connect((server_ip, PORT))
    
    while True:
        data = soct.recv(1024)
        if data:
            print(f"add {data.decode('utf-8')} to clipboard")
    

    










