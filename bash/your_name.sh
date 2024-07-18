#!/bin/bash

echo "What is your name?"

read name

echo -e "Welcome to bash tutorial," $name

echo "Today is" `date`

echo -e "Your current working directory is:\n" `pwd`

echo $name `date`  >> your_name_log.txt
