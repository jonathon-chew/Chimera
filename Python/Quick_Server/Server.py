#! /opt/homebrew/bin/python3

import os
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipAddress = s.getsockname()[0]

choice = input("Which folder would you like to share? (as a file path)")

os.chdir(choice)

print(f"Go to {ipAddress}:8000")
os.system(f'python3 -m http.server')
