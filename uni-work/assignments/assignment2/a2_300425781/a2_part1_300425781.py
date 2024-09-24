# imports
import math
import random

# elementary
def elementary_school_quiz(flag, n):
    '''
    (int, int) => int

    Prompts the user with n number of math questions. Logarithmic if flag = 0, exponentiation if flag = 1. 
    Questions are randomized with integers 1 through 10, then returns the number of question answered correctly.

    Returns an integer numRight indicated how many questions the user answered correctly

    Preconditions: flag is either 0 or 1, n is either 1 or 2
    '''
    
    q = 1 # current question number
    numRight = 0 # number of correct questions
    n = int(n) # convert
    sameRand = -1 # prevents same question twice

    if flag == '0': # log
        while n > 0: # ask questions until there are no more questions left
            rand = random.randint(0, 10) # initialize random number

            while rand == sameRand:
                rand = random.randint(0, 10) # initialize random number

            strRand = str(2 ** rand)
            ans = str(int(math.log(2 ** rand, 2))) # answer to question
            # print(ans)

            print('Question ' + str(q) + ':')
            studentAns = input('2 to the what equals ' + strRand + ', i.e. what is the result of log_2 (' + strRand + ')? ')

            # check if right or wrong
            if (ans == studentAns):
                numRight += 1
                print('Correct!')
            else:
                print('Incorrect.')

            # question finished
            n -= 1
            q += 1
        
        return numRight

    elif flag == '1': # exponentiation
        while n > 0: # ask questions until there are no more questions left
            rand = random.randint(0, 10) # initialize random number

            while rand == sameRand:
                rand = random.randint(0, 10) # initialize random number
            
            strRand = str(rand)
            ans = str(int(2 ** rand)) # answer to question
            # print(ans)

            print('Question ' + str(q) + ':')
            studentAns = input('What does 2 to the power of ' + strRand + ' equal? ')

            # check if right or wrong
            if (ans == studentAns):
                numRight += 1
                print('Correct!')
            else:
                print('Incorrect.')

            # question finished
            n -= 1
            q += 1
        
        return numRight

# high
def high_school_quiz(a, b, c):
    '''
    (number, number, number) => none

    Takes 3 coefficients for a quadratic equation and prints the equation first, then prints its solution(s)

    No checks are done here, they are done in the main section at the bottom
    '''



# main

# print welcome messages
def welcomeMessage(str, type):
    '''
    (string, int) => none

    Prints a welcome message board based on the type specified

    Precondition: type is an integer with value -1, 0, or 1
    '''

    if type == -1: # intro board
        str = 'Welcome to my math quiz generator!'

    elif type == 0: # elementary school
        str = str + ', welcome to my quiz generator for elementary school students!'

    elif type == 1: # high school
        str = 'Quadratic equation: ax^2 + bx + c = 0, solver for ' + str

    strLen = len(str) #length of inputted string
    b = '*' # border
    s = ' ' # empty spaces

    #printing the board
    print()
    print(b * (strLen + 10))
    print(b + s * (strLen + 8) + b)
    print(b + '  __' + str + '__  ' + b)
    print(b + s * (strLen + 8) + b)
    print(b * (strLen + 10))
    print()

# begin the quiz
welcomeMessage('', -1) # print welcome board

name = input("What is your name? ") # take name

# take grade input
status = input("Hi " + name + ". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status == '1': # if they are in elementary school
    welcomeMessage(name, 0)

    typeQuestion = input('What type of question(s) would you like?\nChoose 0 for inverse of exponentiation, or 1 for exponentiation: ')

    if typeQuestion != '0' and typeQuestion != '1': # check if the type of question is proper
        print('Invalid choice, only 0 or 1 is accepted.')
    
    else: # if it is...
        numQuestions = input('How many practice question would you like to do?\nPlease choose from 0, 1, or 2: ')

        if numQuestions != '0' and numQuestions != '1' and numQuestions != '2': # check if the number of questions is proper
            print('Invalid choice, only 0, 1, or 2 is accepted.')

        elif numQuestions == '2': # begin the quiz if it is
            print(name + ', here are your 2 questions:')

            val = elementary_school_quiz(typeQuestion, numQuestions)
            
            if val == 0: # no questions right
                print('I think you need more practice ' + name + '.')
            
            elif val == int(numQuestions): # all questions right
                print('Great job ' + name + '! You\'ll definitely get an A next time!')

            elif val == int(numQuestions) // 2: # 1/2 questions right
                print('You did ok ' + name + ', but I think you can do better.')
        
        elif numQuestions == '1':
            print(name + ', here is your question:')

            val = elementary_school_quiz(typeQuestion, numQuestions)

            if val == 0: # no questions right
                print('I think you need more practice ' + name + '.')
            
            elif val == int(numQuestions): # all questions right
                print('Great job ' + name + '! You\'ll definitely get an A next time!')

            elif val == int(numQuestions) // 2: # 1/2 questions right
                print('You did ok ' + name + ', but I think you can do better.')

elif status == '2': # if they are in high school
    welcomeMessage(name, 1)

    flag = True
    while flag:
        question = input(name + ", would you like a quadratic equation solved? [YES/NO]:")
        question = question.lower().strip() # force lowercase and remove whitespace on ends

        if question != "yes":
            flag = False

        else:
            print("Good choice!")

            # coefficients
            a = input('Enter a number for the first coefficient a: ')
            b = input('Enter a number for the second coefficient b: ')
            c = input('Enter a number for the final coefficient c: ')
 
else:
    print('You are not a part of this software\'s targeted audience.')

print("Good bye " + name + "!")