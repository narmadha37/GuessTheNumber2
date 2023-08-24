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
def game_loop():
    secret_number = str(generate_random_number())
    attempts = 0
    
    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        if guess.lower() == 'q':
            print("The secret number was {secret_number}.")
            print("Total attempts: {attempts}")
            break
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a four-digit number.")
            continue
        
        attempts += 1
        if guess == secret_number:
            print("Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        
        hints = check_guess(secret_number, guess)
        print("hints:", " ".join(hints))
            
    print("Thanks for playing!")
