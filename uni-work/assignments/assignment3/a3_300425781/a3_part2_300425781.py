#! NO ARRAYS, TUPLES, OR SET DICTIONARIES

# imports
import math
import string

# 2.1
def sum_odd_divisors(n):
    '''
    (int) => int/None

    Takes an integer n and returns the sum of all positive integers of n

    Returns:
        > int: if n != 0
        > None: if n == 0
    '''

    # new stuff
    sum = 0
    i = 1
    n = abs(n)

    # return None if n == 0
    if n == 0:
        return
    
    # otherwise
    else:
        while i <= n:
            if n % i == 0:
                sum += i
            
            i += 1

    return sum


# 2.2
def series_sum():
    '''
    () => int/float/None
    
    Prompts the user for a non-negative integer, then returns the result of the series 1/1^2 + ... + 1/n^2
    
    Returns:
        > int: if the inputted integer is 0
        > float: if the inputted integer is greater than 0
        > None: if the inputted integer is negative
    '''

    # new ints
    i = 1
    sum = 0

    # input
    n = int(input('Please enter a non-negative integer: ').strip())

    if n == 0:
        return 1000
    
    elif n < 0:
        return
    
    else:
        while i <= n:
            sum += 1/(i ** 2)

            i += 1

    return sum + 1000


# 2.3
def pell(n):
    '''
    (int) => int/None
    
    Takes an integer n and returns the nth pell number

    Returns:
        > int: if n > -1
        > None: if n < 0
    '''

    if n < 0:
        return 

    elif n < 3:
        return n
    
    else:
        i = 1
        j = 0
        k = 1

        while i < n:
            l = 2 * k + j
            j = k
            k = l
            i += 1
    
    return k


# 2.4
def countMembers(s):
    '''
    (string) => int
    
    Returns the amount of times the following characters appear in the string s
        > lowercase letters from e => j (inclusive)
        > uppercase letters from F => X (inclusive)
        > numbers between 2 => 6 (inclusive)
        > The exclamation point (!), comma (,), and backslash(\)
    '''

    # brute force check
    i = 0
    n = 0

    while i < len(s):
        # lowercase check
        if s[i] == 'e' or s[i] == 'f' or s[i] == 'g' or s[i] == 'h' or s[i] == 'i' or s[i] == 'j': 
            n += 1

        # uppercase check
        elif s[i] == 'F' or s[i] == 'G' or s[i] == 'H' or s[i] == 'I' or s[i] == 'J' or s[i] == 'K' or s[i] == 'L' or s[i] == 'M' or s[i] == 'N' or s[i] == 'O' or s[i] == 'P' or s[i] == 'Q' or s[i] == 'R' or s[i] == 'S' or s[i] == 'T' or s[i] == 'U' or s[i] == 'V' or s[i] == 'W' or s[i] == 'X': 
            n += 1

        # integer check
        elif s[i] == '2'or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6': 
            n += 1

        # special character check
        elif s[i] == '!'or s[i] == '\\' or s[i] == ',': 
            n += 1

        i += 1
    
    return n


# 2.5
def casual_number(s):
    '''
    (string) => int/None
    
    Takes a string s that resembles an integer and returns it in integer form

    Returns:
        > int: if s resembles an integer
        > None: if s does not resemble an integer
    '''

    length = len(s)
    i = 0
    val = ''

    if s.isdigit():
        return int(s)
    
    else:
        while i < length:
            if s[i] == '-' or s[i] == ',':
                if not(s[i + 1].isdigit()):
                    return
                
                elif s[i] == '-' and i > 0:
                    return
                
                elif s[i] == ',':
                    val += ''
                
                else:
                    val += '-'
                
            elif not(s[i].isdigit()) and s[i] != '-' and s[i] != ',':
                return
            
            else:
                val += s[i]

            i += 1
    
    return val
                
print(casual_number('1,241'))