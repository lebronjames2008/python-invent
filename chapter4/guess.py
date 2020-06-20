# This is a guess the number game
import random

guessesTaken = 0

print('Hello! What is your name?')
playername = input()

number = random.randint(1, 20)
print('Well, ' + playername + ', I am thinking of a number between 1 and 20, You have 6 guesses!')

while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + playername + '! You guessed my number in ' +
                        guessesTaken + ' guesses!')


if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)
