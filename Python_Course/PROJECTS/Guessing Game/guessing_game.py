from random import random

random_number = int(round(random(), 1) * 10)
guesses = 0
correct = False

while guesses != 4 and correct is not True:
    if guesses < 3:
        guess = int(input("Guess: "))
        if guess == random_number:
            print('You win!')
            correct = True
            break
        else:
            guesses += 1
    else:
        print('Sorry, you failed!')
        break