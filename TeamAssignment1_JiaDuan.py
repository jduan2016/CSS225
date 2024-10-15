# Professor: Linh Vu
# Student: Jia Duan
# Date: 10/15/2024
# CSS 225 - Team Assignment 1

# Description:
# Your team is to write a program to print a number of options 
# presented to the user and allow the user to select an option from the list.
# although your team can use less than 9 options, 
# but make sure there are at least 5 options. 
# If the user selects a valid choice, the program should print a short message. 
# The message should include the value that the user typed.

# In this example, the final option of '0' is added to 
# the options to exit the program. 
# You may use 'if' and 'elif' statements to complete the program.

# Your program should be posted to Github, 
# one of the team members should create a team GitHub account 
# (separate account from the one you created in Module 2) for viewing by your team. 
# Remember to add each one of your team members and your instructor to the 
# Team GitHub account the same way you added your instructor to view code in GitHub.

# Extra credit:

# The team can modify the program so that it continues 
# looping allowing the user to choose an option each time around. 
# In this version, the program should only terminate when the user selects 0 (Exit).

def print_program_options():
    """ This program prints options for the user to choose.
        The last option can let the user exit the program 
    """
    print('''
             1. Python 
             2. Java 
             3. JavaScript
             4. C#
             5. C++
             6. SQL
             7. Go
             8. MATLAB
             9. R
             0. Exit      
          ''')
def get_input():
    """ This program get user input with data validation
    """
    while True:
        try:
            n = int(input("Enter your option, it must be a non-negative integer. Enter 0 to exit. ") )
        except ValueError:
            print("Not an integer. Please try again.")
        else:
            if n == 0:
                print(f"You entered Option {n}.Goodbye!")
                exit()
            elif n>= 0 and n <= 9:
                print(f"You entered Option {n}. Hello ", end="")
                if n == 1:
                    print("Python!")
                elif n == 2:
                    print("Java!")
                elif n == 3:
                    print("JavaScript!")
                elif n == 4:
                    print("C#!")
                elif n == 5:
                    print("C++!")
                elif n == 6:
                    print("SQL!")
                elif n == 7:
                    print("Go!")
                elif n == 8:
                    print("MATLAB!")
                else: #n == 9:
                    print("R!")
                # break
            else:
                print("You entered a negative number.")
            
def main():
    """The main function calls other functions
    """
    print_program_options()
    get_input()

main()
