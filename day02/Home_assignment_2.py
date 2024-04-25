import random

computer_number = random.randrange(1, 21)
gusesses = 0
while True:
   guess = int(input("take a guess!"))
   if guess == computer_number:
      print("Good for you, correct guess!")
      break
   elif guess < computer_number:
      print("Too Low!")
   else:
      print("Too High!")

