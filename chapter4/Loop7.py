# Program to guess your random number

import random

print("Game rules: Guess a number between 35 and 45")
randomNumberInMemory = random.randint(35, 45)

# Program to ask how many guesses the user would like
print("How many guesses would you like?")
totalGuessString = input()
totalguess = int(totalGuessString)

for y in range(1, totalguess):
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
