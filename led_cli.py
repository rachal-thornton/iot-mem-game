# Author: Rachal Thornton
# Class: CS 346-01
# Assignment: Final Project
# Due: 04/28/26
# Description: A client model for a memory game on the Raspberry Pi system.

#!/usr/bin/python3

import socket
import sys

host = '199.17.161.147' # Server IP
port = 3147             # Server port

while True:
    # Ask user if they want to play or quit
    command = input("Welcome to the LED Memory Game! Type 'play' or 'quit': ").strip().lower()
    if command == "quit":
        print("Exiting...")
        break
    elif command == "play":
        print("Starting game...")

    else:
        print("Invalid command. Use ''play' or 'quit'.")
        continue

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(command.encode('utf-8'))

        # Main game loop 
        while True:
            reply = s.recv(4096)
            print("Server reply:", reply.decode('utf-8'))

            if "Sequence shown. Input your guess" in reply.decode('utf-8'):
                user_input = input("Enter your guess (comma-separated colors): ")
                s.sendall(("sequence:" + user_input).encode('utf-8'))
            elif "Correct!" in reply.decode('utf-8') or "Incorrect!" in reply.decode('utf-8'):
                print("Game over. Returning to main menu.")
                break
            else:
                print("Unexpected server response. Ending game.")
                break

        s.close()
    except socket.error as e:
        print("Socket error:", e)
        break