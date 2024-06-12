import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.secret_number = random.randint(1, 20)
        self.guesses = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        
        self.guess_label = tk.Label(self.root, text="Enter your guess:")
        self.guess_label.pack()
        
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.reset_button = tk.Button(self.root, text="Restart Game", command=self.reset_game)
        self.reset_button.pack()
        
        self.show_button = tk.Button(self.root, text="Show Number", command=self.show_number)
        self.show_button.pack()
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()
        
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.guesses += 1
            
            if guess == self.secret_number:
                messagebox.showinfo("Result", f"Good for you, correct guess! It took you {self.guesses} guesses.")
                self.reset_game()
            elif guess < self.secret_number:
                messagebox.showinfo("Result", "Too low!")
            else:
                messagebox.showinfo("Result", "Too high!")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
    
    def reset_game(self):
        self.secret_number = random.randint(1, 20)
        self.guesses = 0
        self.guess_entry.delete(0, tk.END)
        messagebox.showinfo("Game Reset", "The game has been reset.")
    
    def show_number(self):
        messagebox.showinfo("Secret Number", f"The hidden number is {self.secret_number}.")

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()