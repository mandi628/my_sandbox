#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 2: If Statements

echo "Challenge 012"
# As for two numbers. If the first one is larger than the second, display the second number first and then the first number.
# Otherwise show the first number first and then the second.
echo "Enter a number: "
read num1

echo "Enter another number: "
read num2

if [ $num1 = $num2 ]
then
  echo "$num1 is equal to $num2"
elif [ $num1 -gt $num2 ]
then
  echo "$num2 is less than $num1"
elif [ $num1 -lt $num2 ]
then
  echo "$num1 is less than $num2"
fi

echo "Thank you!"
