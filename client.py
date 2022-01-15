import pynput
import pyperclip as pp
import time
import random, string
from pynput import keyboard
import socket

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
CLIENTS_LIST = []

print("Setting up this computer as a client...")
server_ip = input(f"Enter the IP of the server\n >>> ")

soct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soct.connect((server_ip, PORT))

while True:
    try:
        data = soct.recv(1024).decode('utf-8')
        print(f"add {data} to clipboard")
        pp.copy(data)
    except KeyboardInterrupt:
        break
    
