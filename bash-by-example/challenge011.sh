#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 011"
# Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number
# in a user-friendly format.
echo "Enter a number greater than 100: "
read a

echo "Enter a number less than 10: "
read b

gz=$[a/b]
rem=$[a%b]

echo "$a divided by $b is $gz with $rem left over."
