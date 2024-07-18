#! /bin/bash

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

echo "Challenge 009"
# Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
echo "How many days to you want to count? "
read d

h=$[d*24]
m=$[h*60]
s=$[m*60]

echo -e "$d days is:\n$h hours,\n$m minutes, and\n$s seconds."

