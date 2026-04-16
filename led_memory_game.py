# Author: Rachal Thornton
# Class: CS 346-01
# Assignment: Final Project
# Due: 04/28/26
# Description: A program to handle memory game logic using led lights and a client-server model for processing user input.

# Imports
import random
import time
from gpiozero import LED

# Assign led lights to GPIO pins
r_led = LED(20)  # Red led; change GPIO pin as needed
g_led = LED(21)  # Green led; change GPIO pin as needed
y_led = LED(16)  # Yellow led; change GPIO pin as needed

# MemGame: class to describe an instance of a game
class MemGame:
    # __init__: Constructor to initialize memory game
    # Pre: Client has requested to play game
    # Post: Creates an instance of a memory game
    def __init__(self):
        self.sequence = []  # Correct sequence of lights
        self.client_sequence = []   # Client-guessed sequence of lights

    # generate_sequence: Method to generate a random sequence of led colors
    # Pre: Client is playing a round
    # Post: A sequence of 5 random led colors are chosen
    def generate_sequence(self, length=5):
        self.sequence = [random.choice(['red', 'green', 'yellow']) for _ in range(length)]

    # add_user_input: Method to add client input 
    # Pre:
    # Post: 
    def add_client_input(self, color):
        self.client_sequence.append(color)

    # check_client_sequence: Method to check if client inputted sequence matches correct sequence of led colors
    # Pre: Sequence has been generated
    # Post: Returns true or false based on if client sequence matches correct sequence
    def check_client_sequence(self):
        return self.client_sequence == self.sequence

    # reset_game: Method to reset game
    # Pre: Game is initialized
    # Post: Resets sequence and guesses
    def reset_game(self):
        self.sequence = []
        self.client_sequence = []

    # light_up: Method to light up a specific led color with a clear on/off rhythm
    # Pre: Color chosen
    # Post: Specified led lights up for 1 second, then stays off longer
    def light_up(self, color):
        on_time = 1.0
        off_time = 0.8

        if color == "red":
            r_led.on()
            time.sleep(on_time)
            r_led.off()
        elif color == "green":
            g_led.on()
            time.sleep(on_time)
            g_led.off()
        elif color == "yellow":
            y_led.on()
            time.sleep(on_time)
            y_led.off()

        time.sleep(off_time)