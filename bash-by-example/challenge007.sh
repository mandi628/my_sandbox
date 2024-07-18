#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 007"
# Ask the user for the name and their age. Add 1 to their age and display the output:
# [Name] next birthday you will be [new age].
echo "What is your name? "
read name

echo "How old are you? "
read age

echo "$name, on your next birthday, you will be $[age + 1]."
