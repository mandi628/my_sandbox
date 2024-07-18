#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 010"
# There are 2.204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds.
echo "Enter a weight in kilograms: "
read weight

kg_wt=$[(weight*2204)/1000]

echo "The weight in pounds is $kg_wt pounds."
