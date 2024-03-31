import random

def magic_guesser():
    randomiser = input("Pick a range of numbers: ")
    magic_number = random.randrange(int(randomiser))
    your_guess = input("Pick a number between 0 and {} minus 1: ".format(randomiser))
    if int(your_guess) == magic_number:
        print("You WON")
        print("the number was {}".format(magic_number))
    elif int(your_guess) != magic_number: 
        print("You LOST, try the game again.")
        print("The number was {}".format(magic_number))

magic_guesser()