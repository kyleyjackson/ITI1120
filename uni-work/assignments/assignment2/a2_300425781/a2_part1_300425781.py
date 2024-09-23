# imports
import math
import random

# elementary
def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
    '''
    (int, int) => int

    Prompts the user with n number of math questions. Logarithmic if flag = 0, exponentiation if flag = 1. 
    Questions are randomized with integers 1 through 10, then returns the number of question answered correctly.
    Preconditions: flag is either 0 or 1, n is either 1 or 2
    '''
    
    rand = random.randint(0, 10) # random number for questions
    
    if flag == 0: # check if question type is appropriate
        if n != 0 or n != 1 or n != 2: # check if number of questions is appropriate
            print('Invalid choice, please enter 0, 1, or 2.')
            # ask for input again

        elif n == 0:
            # return value to make console say bye-bye
            pass

        else: # if it is...
            while n > 0: # ask questions until there are no more questions left
                pass

            pass

    elif flag == 1: # repeat same as above
        if n != 0 or n != 1 or n != 2:
            print('Invalid choice, please enter 0, 1, or 2.')
            return
        
        else:
            while n > 0:
                pass
            
            pass

    else: # if flag parameter is invalid
        print('Invalid choice, please enter 0 or 1.')
        # recursively call?

# high
def high_school_quiz(a, b, c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''
    (number, number, number) => none

    Takes 3 coefficients for a quadratic equation and prints the equation first, then prints its solution(s)
    '''



# main

# your code for the welcome message goes here

# print welcome messages
def welcomeMessage(str, type):
    '''
    (string, int) => none

    Prints a welcome message board based on the type specified
    Precondition: type is either 0 , 1, or 2
    '''

    if type == 0:
        pass

    elif type == 1:
        pass

    else: 
        pass

    strLen = len(str) #length of inputted string
    b = '*' # border
    s = ' ' # empty spaces

    #printing the board
    print(b * (strLen + 10))
    print(b + s * (strLen + 8) + b)
    print(b + '  __' + str + '__  ' + b)
    print(b + s * (strLen + 8) + b)
    print(b * (strLen + 10))

name = input("What is your name? ")

status = input("Hi " + name + ". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status == '1':
    # your code goes here
    pass

elif status == '2':

    # your code for welcome message
    flag = True
    while flag:
        question = input(name + ", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question = question.lower()

        if question != "yes":
            flag = False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
 
else:
    # your code goes here
    pass

print("Good bye " + name + "!")