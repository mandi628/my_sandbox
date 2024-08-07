#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 6: While Loop

print("Challenge 050")

# Ask the user to enter a number between 10 and 20. If they enter a
# value under 10, display the message "Too low" and ask them to try
# again. If they enter a value above 20, display the message "Too
# high" and ask them to try again. Keep repeating this until they
# enter a value that is between 10 and 20 and then display the
# message "Thank you"

num = int(input("Enter a number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        num = int(input("Too low, try again: "))
    elif num > 20:
        num = int(input("Too high, try again: "))
print("Thank you.")
