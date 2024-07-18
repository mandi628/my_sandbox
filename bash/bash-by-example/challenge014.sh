#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

echo "Challenge 014"
# Ask the user to enter a number between 10 and 20 (inclusive).
# If they enter a number within this range, display the message "Thank you",
# otherwise display the message "Incorrect answer"

echo "Enter a number between 10 and 20: "
read num

if [ $num -le 10 ]
then
  echo "Incorrect answer."
elif [ $num -ge 20 ]
then
  echo "Incorrect answer."
else
  echo "Thank you."
fi
