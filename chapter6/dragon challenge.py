# Dragon Realm Game
import random
import time


# ----------------------------------------------------
# Def statement is for defining that this is the Intro
def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()


# ----------------------------------------------------
def chooseitem():
    print('You found a Sword(1) and Candy(2)')
    print('Do you want 1 or 2')

    itemChosen = input()
    if itemChosen == '1':
        print('You got a Sword')

    if itemChosen == '2':
        print('You got Candy ')

    return itemChosen


# ----------------------------------------------------
# Def statement to tell that its asking you to choose a cave
def chooseCave():
    cave = ''
    # Cave is function here is equal to a blank string
    while cave != '1' and cave != '2':
        # This function is to make sure the user typed 1 or 2, and not something else.
        # Also the and is a another type of operator just like or and it is a boolean operator.
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


# ----------------------------------------------------
def checkCave(chosenCave, itemChosen):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    caveNumber = random.randint(1, 2)

    if chosenCave == str(caveNumber) and itemChosen == '1':
        print(' Friendly Dragon: Gives you his treasure! ')
    if chosenCave == str(caveNumber) and itemChosen == '2':
        print("Dragone Farts at you")
    if chosenCave != str(caveNumber) and itemChosen == "1":
        print("You win")
    if chosenCave != str(caveNumber) and itemChosen == "2":
        print("The Dragon eats you")


# ----------------------------------------------------
# progarm starts here

# ----------------------------------------------------
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    # The choose cave function lets the player type in the the cave they want to go into.

    itemChosenDisplay = chooseitem()

    caveNumber = chooseCave()

    checkCave(caveNumber, itemChosenDisplay)
    # This is the function that will display either if it will give you treasure or gobble you up.
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    # This is the playagain function where you press y or yes to play again or no to stop playing.
