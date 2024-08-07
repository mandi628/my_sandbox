#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 7: Random

print("Challenge 059")

# Display five colours and ask the user to pick one. If they pick the same
# as the program has chosen, say "Well done", otherwise display a witty
# answer which involves the correct colour, e.g. "I bet you are GREEN
# with envy" or "You are probably feeling BLUE right now". Ask them to
# guess again; if they have still not got it right, keep giving them
# the same clue and ask the user to enter a colour until they guess it
# correctly.

import random

colors = ["red", "green", "orange", "blue", "purple"]
print(colors)
choice = random.choice(colors)

pick = input("Choose a color from the list: ")

if pick == choice:
    print("Well done.")
while pick != choice:
    if choice == "green":
        print("I bet you are GREEN with envy.")
    elif choice == "blue":
        print("You are probably feeling BLUE right now.")
    elif choice == "red":
        print("Don't see RED, just guess again!")
    elif choice == "orange":
        print("ORANGE you glad I didn't say banana?")
    elif choice == "purple":
        print("You're no PURPLE dinosaur!")
    pick = input("Choose another color: ")
print("You got it right!")

""" Solution from book:
import random
colour = random.choice(["red", "blue", "green", "white", "pink"])
print("Select from red, blue, green, white or pink")
tryagain = True
while tryagain == True:
    theirchoice = input("Enter a colour: ")
    theirchoice = theirchoice.lower()
    if colour == theirchoice:
        print("Well done.")
        tryagain = False
    else:
        if colour == "red":
            print("I bed you are seeing RED right now!")
        elif colour == "blue":
            print("Don't feel BLUE.")
        elif colour == "green":
            print("I bet you are GREEN with envy right now.")
        elif colour == "white":
            print("Are you WHITE as a sheet, as you didn't guess correctly?")
        elif colour == "pink":
            print("Shame you are not feeling in the PINK, as you got it wrong!")
