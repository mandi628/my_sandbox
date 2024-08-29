#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

echo "Challenge 015"

# Ask the user to enter their favourite colour. If they enter "red", "RED" or "Red" display the message
# "I like red, too", otherwise display the message "I don't like [colour], I prefer red."

echo "What is your favorite color?"
read color

if $color = "red" or $color = "RED" or $color = "Red"
    echo "I like red, too."
else
    echo "I don't like $color, I prefer red."
fi
