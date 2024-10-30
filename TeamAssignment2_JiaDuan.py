# Professor: Linh Vu
# Student: Jia Duan
# Date: 10/30/2024
# CSS 225 - Team Assignment 2

import random
# Description:
# Module 6 introduces us to a lot of modules available already included in Python. 
# Your team is to write a guessing program that will take a number (input) from the user 
# and guess a randomly generated number. Provide the user with an opportunity 
# to guess higher or lower, depending on the randomly generated number. 
# Remember to use python module(s) and nested if…else statements in your code.
def v_1():
    target = random.randint(1,10)
    while True:
        num = int(input("V1: Please enter a number between 1 and 10: "))
        if num > target:
            print("Please guess lower")
        elif num < target:
            print("Please guess higher")
        else:
            print("Well done, you guessed it!")
            break
    
# Extra credit:
# The team can modify the program so that it continues looping allowing the user 
# to keep guessing a number until the user chooses the 'No' option using a prompt
#  (i.e. 'Would you like to guess another number (Y/N)?'. In this version, 
# the program should only terminate when the user selects 'N'.
def v_2():
    target = random.randint(1,10)
    while True:
        num = int(input("V2. Please enter a number between 1 and 10: "))
        if num > target:
            print("That's not right!")
            choice = str(input("Would you like to guess another number (Y/N)?"))
            if choice == "Y":
                print("Please guess lower")
            elif choice == "N":
                print("Bye!")
                exit()
        elif num < target:
            print("That's not right!")
            choice = str(input("Would you like to guess another number (Y/N)?"))
            if choice == "Y":
                print("Please guess higher")
            elif choice == "N":
                print("Bye!")
                exit()
        else:
            print("Well done, you guessed it!")
            break #Exit the program when finish the task

def main():
    v_1()
    v_2()

if __name__ == "__main__":
    main()
