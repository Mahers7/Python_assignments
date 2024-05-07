
import random

def generate_computer_number():
    return random.randint(1, 21)

def take_guess(guess, computer_number):
    if guess == computer_number:
        print("Nice!, you got it")
        return True
    elif guess < computer_number:
        print("Too low!")
    else:
        print("Too high!")
    return False

def play_game():
    computer_number = generate_computer_number()
    guesses = 0

    while True:
        guess = input("Take a guess (enter 'x' to quit, 'n' for a new game, or 's' to show the number): ")
        
        if guess.lower() == 'x':
            print("Goodbye!")
            return False
        
        elif guess.lower() == 'n':
            print("Starting a new game!")
            return True
        
        elif guess.lower() == 's':
            print("The hidden number is:", computer_number)
            continue
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number or command ('x' to quit, 'n' for a new game, or 's' to show the number).")
            continue
        
        guesses += 1
        if take_guess(guess, computer_number):
            print("You took", guesses, "guesses.")
            return True

def main():
    print("Welcome to the Number Guessing Game!")
    play_again = True
    
    while play_again:
        play_again = play_game()

if __name__ == "__main__":
    main()
