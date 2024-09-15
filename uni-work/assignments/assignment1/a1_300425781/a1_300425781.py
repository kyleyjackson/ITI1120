# Name: Kyle Yang Jackson
# Student Number: 300425781
# Course: ITI1120
# Assignment One
# Year: 2024

# imports
import turtle
import math

####################
# Question One
####################
def mh2kh(s):
    '''
    (number) -> number
    
    Returns the input speed in km/h
    '''

    print(1.609344 * s)
    return 1.609344 * s

####################
# Question Two
####################
def pythagorean_pair(a, b):
    '''
    (number, number) -> Boolean

    Returns True if numbers a and b form a pythagorean pair, returns false otherwise
    '''

    c = math.sqrt((a ** 2 + b ** 2))

    if (round(c, 0) == c):
        print(round(c, 0) == c)
        return True
    else:
        print(round(c, 0) == c)
        return False

####################
# Question Three
####################
def in_out(xs, ys, side):
    '''
    (number, number, number) -> Boolean

    Returns True if the query point is inside of the boundaries of the specified square
    Precondition: side must be non-negative
    '''
    if (side < 0):
        print('Side length must be non-negative!')
        return
    
    xInput = input("Enter the x coordinate of the query point: ")
    xc = float(xInput)

    yInput = input("Enter the y coordinate of the query point: ")
    yc = float(yInput)

    
    if ((xc >= xs and xc <= xs *+side) and (yc >= ys and yc <= ys + side)):
        print((xc >= xs and xc <= xs + side) and (yc >= ys and yc <= ys + side))
        return True
    else:
        print((xc >= xs and xc <= xs + side) and (yc >= ys and yc <= ys + side))
        return False

####################
# Question Four
####################
def safe(n):
    '''
    (number) -> Boolean

    Returns False if the number n does not contain 9 and cannot be divided by 9, otherwise returns True
    Precondition: n must be non-negative
    '''

    nStr = str(n)

    if (n < 0):
        print('n must be non-negative!')
        return
    elif('9' in nStr or n % 9 == 0):
        print(not('9' in nStr or n % 9 == 0))
        return False
    else:
        print(not('9' in nStr or n % 9 == 0))
        return True
    
####################
# Question Five
####################
def quote_maker(quote, name, year):
    '''
    (string, string, number) -> string

    Returns a formatted quote after given the quote, author, and year
    '''

    year = str(year)

    print('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"')
    return ('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"')

####################
# Question Six
####################
def quote_displayer():
    '''
    () -> string

    Returns a formatted quote after the user inputs the quote, author, and year
    '''

    quote = input('Enter the quote: ')
    name = input('Enter the name of the author of your quote: ')
    year = input('Enter the year the quote was created: ')

    print('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"')
    return ('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"')
