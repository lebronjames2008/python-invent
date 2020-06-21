# Program to guess your random number

import random

print("Game rules: Guess a number between 35 and 45")
randomNumberInMemory = random.randint(35, 45)

for y in range(1, 10):
    print(y, "Guess the RANDOM NUMBER !!")
    guessedStringValue = input()

    # Now we are converting string to number
    guessedNumberValue = int(guessedStringValue)

    # Here we are checking if the guessed number is equal
    if guessedNumberValue == randomNumberInMemory:
        print("Good Job - you guessed the age correctly")
        break
    else:
        print("Sorry. Wrong guess!")

print("End of the program")
