#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 004"
# Ask the user to enter two numbers. Add them together and display the answer as 'The total is [answer]'.
echo "Enter a number: "
read a

echo "Enter another number: "
read b

echo "The total is $[a + b]."
