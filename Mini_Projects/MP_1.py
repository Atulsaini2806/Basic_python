#Guess the number game

import random 
target = random.randint(1,100)

while True:
    guess = int(input("Guess a number: "))
    
    if guess < target:
        print("Too low! Try again.......")
    elif guess > target:
        print("Too high! Try again.........")
    else:
        print("Congratulations! You guessed the correct number.")
        break

print("The game is over.......................")        