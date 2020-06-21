# Program to guess your santha's age

appasAge = 42

for y in range(5):
    print(y, "Dai Rish.. please guess santhas ages..!!")
    stringValue = input()

    # Now we are convering string to number
    numberValue = int(stringValue)

    if numberValue == appasAge:
        print("Good Job - you guessed the age correctly")
        break

print("End of the program")
