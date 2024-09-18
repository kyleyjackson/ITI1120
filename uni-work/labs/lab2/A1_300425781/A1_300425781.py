# imports
import math

####################
# Exercise One
####################
def repeater(s1, s2, n):
    '''
    (string, string, int) => string

    Returns a string starting with '_' then alternating s1 and s2 n number of times, ending with '_'
    '''

    str = s1 + s2 # combine string 
    # print('_' + (str * n) + '_')
    return '_' + (str * n) + '_'

# repeater('A', 'X', 5)

####################
# Exercise Two
####################
def roots(a, b, c):
    '''
    (number, number, number) => none

    Prints the roots of the quadratic equation with coefficients a, b, and c along with a formatted message
    Preconditions: a is non-zero, a, b, and c are such that (b^2) - 4ac is positive
    '''

    rootOne = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a) # first root
    rootTwo = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a) # change to - for second root

    # nice message
    print('The quadratic equation with coefficients a = ' + str(a) + ', b = ' + str(b) + ', c = ' + str(c))
    print('has the following solutions (roots): \n' + str(rootOne) + ' and ' + str(rootTwo))

# roots(-1, 4, 1.5)

####################
# Exercise Three
####################
def real_roots(a, b, c):
    '''
    (number, number, number) => Boolean

    Returns True if the roots of the quadratic equation with coefficients a, b, and c are real, otherwise returns false
    '''

    # print(((b ** 2) - 4 * a * c) >= 0)
    return ((b ** 2) - 4 * a * c) >= 0

# real_roots(1, 1, 1)

####################
# Exercise Four
####################
def reverse(x):
    '''
    (int) => int

    Returns the integer x with its digits swapped around
    Precondition: x is a two-digit integer
    '''

    temp = str(x)[1]
    temp1 = str(x)[0]

    # print(int(temp + temp1))
    return int(temp + temp1)

# reverse(91)
