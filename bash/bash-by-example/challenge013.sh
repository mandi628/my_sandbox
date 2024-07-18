#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

echo "Challenge 013"
# Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message "Too high", otherwise diaplay, "Thank you."

echo "Enter a number less than 20: "
read num

if [ $num -ge 20 ]
then
  echo "Too high!"
else
  echo "Thank you."
fi
