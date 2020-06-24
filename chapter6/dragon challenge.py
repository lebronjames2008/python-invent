import random
import time


def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()


def chooseItem():
    print('You have a Sword and a Candy')
    print('Which one do you want, 1 or 2.')
    itemChosen = input()
    if itemChosen == '1':
        print('You got a Sword')

    if itemChosen == '2':
        print('Yoy got Candy ')

    return itemChosen


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave are you choosing to go in, 1 or 2')
        cave = input()

    return cave


def checkCave(chosenCave, itemChosen):
    print('you approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps in front of you and opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave) and itemChosen == 2:
        print('Gives you his treasure')
        print('And eats your candy happily')

    elif chosenCave == str(friendlyCave) and itemChosen == 1:
        print('Gives you his treasure')
        print(' And farts at you')

    elif chosenCave != str(friendlyCave) and itemChosen == 1:
        print("Dies because you stab it with your new sword")

    elif chosenCave != str(friendlyCave) and itemChosen == 2:
        print('gobbles you up in 1 bite,a nd enjoys your piece of candy')


# This is the start of the program
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    itemChosenend = chooseItem()

    caveNumber = chooseCave()

    checkCave(caveNumber, itemChosenend)

    print('Do you want to play again?(yes or no)')

    playAgain = input()