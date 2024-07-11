#! /usr/bin/env python3

print("Welcome to Guess my Number!")
print("This is a two player game...")

x = int(input("Player 1, enter the secret number (0-9): "))
guess = int(input("Player 2, enter your guess: "))

if guess < x:
    print("Too low! Player 1 wins!")
if guess > x:
    print("Too high! Player 1 wins!")
if guess == x:
    print("You got it! Player 2 wins!")
