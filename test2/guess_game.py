# guess_game.py

import random

def generate_random_number():
    return random.randint(1000, 9999)
def check_guess(secret_number, guess):
    hints = []
    for i in range(4):
        if guess[i] == secret_number[i]:
            hints.append("circle")
        elif guess[i] in secret_number:
            hints.append("X")
    return hints

 
        


