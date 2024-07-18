#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 006"
# Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user-friendly format.
echo "How many slices of pizza did you start with? "
read pizza

echo "How many slices of pizza have you eaten? "
read eaten

echo "You have $[pizza - eaten] slices left."
