#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 005"
# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as 'The answer is [answer]'
echo "Enter a number: "
read a

echo "Enter another number: "
read b

echo "And one more: "
read c

echo "The answer is $[(a + b) * c]."
