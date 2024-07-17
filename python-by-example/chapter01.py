#! /usr/bin/env python3

# Python by Example, by Nichola Lacey
# borrowed from library 2024.07.05

# Chapter 1: The Basics

print("Challenge 001")
# Ask for the user's first name and display the output message 'Hello [First Name]'
first_name = input("What is your first name? ")
print("Hello", first_name)

print("\n~~~~~~~~\n")

print("Challenge 002")
# Ask for the user's first name and then ask for their surname and display the output message
first = input("What is your first name? ")
surname = input("What is your surname? ")
print("Hello", first, surname)

print("\n~~~~~~~~\n")

print("Challenge 003")
# Write code that will display the joke 'What do you call a bear with no teeth?' and on the next line display the answer 'A gummy bear!' Try to create it using only one line of code.
print("What do you call a bear with no teeth?\nA gummy bear!")

print("\n~~~~~~~~\n")

print("Challenge 004")
# Ask the user to enter two numbers. Add them together and display the answer as 'The total is [answer]'.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
answer = a + b
print("The total is", answer)

print("\n~~~~~~~~\n")

print("Challenge 005")
# Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as 'The answer is [answer]'
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("One more number: "))
answer = (x + y) * z
print("The answer is", answer)

print("\n~~~~~~~~\n")

print("Challenge 006")
# Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user-friendly format.
pizza = int(input("How many slices of pizza did you start with? "))
eaten = int(input("How many slices of pizza have you eaten? "))
left = pizza - eaten
print("You have", left, "slices left.")

print("\n~~~~~~~~\n")

print("Challenge 007")
# Ask the user for the name and their age. Add 1 to their age and display the output:
# [Name] next birthday you will be [new age].
name = input("What is your name? ")
age = int(input("How old are you? "))
new_age = age + 1
print(name, "on your next birthday, you will be", new_age)

print("\n~~~~~~~~\n")

print("Challenge 008")
# Ask for the total price of the bill, then ask how many diners there are.
# Divide the total bill by the number of diners and show how much each person must pay.
bill = float(input("How much is the bill? $"))
diners = float(input("How many people are dining? "))
each = bill / diners
print(f'Each person much pay ${each:.2f}.') # Advanced notation of f-string to get two decimal places.
# f at the beginning of the function indicates the format, then the text in the SINGLE quotes, the {var:.decf}.
# There are other features, but I don't need them now.

print("\n~~~~~~~~\n")

print("Challenge 009")
# Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
days = int(input("Enter a number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In", days, "days, there are:")
print(hours, "hours")
print(minutes, "minutes")
print("and", seconds, "seconds")

print("\n~~~~~~~~\n")

print("Challenge 010")
# There are 2.204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds.
weight = float(input("Enter a weight (kg): "))
pounds = 2.204 * weight
print("The weight in pounds is," pounds)
