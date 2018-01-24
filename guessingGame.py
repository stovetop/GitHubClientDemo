#!/usr/bin/python2.7

import os
import sys
import random

# Random Number Guessing Game

# set random value

solution = random.randrange(1,10)


print ("Try guessing a number between 1 and 10")

# Get user input


myguess = input("Pick a number: ")

count = 1


while myguess != solution:
    print ("Nope....not it!")
    count += 1
    myguess = input("Try again: ")
    
print("You guessed it!!")
print("Tries: ",count)