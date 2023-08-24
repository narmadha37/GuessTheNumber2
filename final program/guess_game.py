import random

def generate_random_number():
    return random.randint(1000, 9999)

def get_clues(secret_number, guess):
    clues = []
    for i in range(4):
        if guess[i] == secret_number[i]:
            clues.append('circle')
        elif guess[i] in secret_number:
            clues.append('x')
    return clues

def play_game():
    secret_number = str(generate_random_number())
    attempts = 0

    while True:
        guess = input("Enter your guess (4-digit number) or 'q' to quit: ")

        if guess.lower() == 'q':
            print(f"The secret number was {secret_number}.")
            print(f"Total attempts: {attempts}")
            break
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        
        clues = get_clues(secret_number, guess)
        print("Clues:", " ".join(clues))

if __name__ == "__main__":
    play_game()
