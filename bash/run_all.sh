#!/bin/bash

echo "Today is " `date` # Prints date

`pwd`
### echo -e "\nEnter the path to directory" # Asks user for path to directory
#NOTE: not currently working properly in Termux; keeps saying directory does not exist
# Tried with the file in my_sandbox directory, as well as moving the script to my home directory
read the_path

echo -e "\nYour path has the following files and folders: " # Lists the files and folders in the directory given above
ls $the_path
