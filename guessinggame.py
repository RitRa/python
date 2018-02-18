#Rita Raher 18-02-2018
# Guessing game 

# to generate random number you need to import random
import random

target = random.randint(0, 100)
guess = 101

print("Guess a number between 1 and 100")
# loops through until we get the correct number
while guess != target:
    # take a number in the input
    guess = int(input('Guess a number?'))
    if guess == target:
        print("Well done you have completed the guessing game!")
    elif guess < target:
        print("Too low!")
    else:
        print("Too high!")
