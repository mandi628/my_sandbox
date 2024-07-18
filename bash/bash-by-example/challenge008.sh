#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 008"
# Ask for the total price of the bill, then ask how many diners there are.
# Divide the total bill by the number of diners and show how much each person must pay.
echo "How much is the bill? (whole number) "
read bill

echo "How many diners are there? "
read diners

amount=$((bill/diners))

echo "Each person must pay $amount dollars."
