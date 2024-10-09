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


# 2.6
def alienNumbers(s):
    '''
    (string) => int
    
    Takes a string s and returns the sum of the value represented by the following characters
        > T => 1024
        > y => 598
        > ! => 121
        > a => 42
        > N => 6
        > U => 1

    Precondition: s contains no characters outside the specified set
    '''

    return sum(1024 * (i == 'T') + 598 * (i == 'y') + 121 * (i == '!') + 42 * (i == 'a') + 6 * (i == 'N') + (i == 'U') for i in s)


# 2.7
def alienNumbersAgain(s):
    '''
    (string) => int
    
    Takes a string s and returns the sum of the value represented by the following characters
        > T => 1024
        > y => 598
        > ! => 121
        > a => 42
        > N => 6
        > U => 2

    Precondition: s contains no characters outside the specified set
    '''

    sum = 0
    i = 0

    while i < len(s):
        if s[i] == 'T':
            sum += 1024
        
        elif s[i] == 'y':
            sum += 598

        elif s[i] == '!':
            sum += 121

        elif s[i] == 'a':
            sum += 42
        
        elif s[i] == 'N':
            sum += 6
        
        elif s[i] == 'U':
            sum += 2
        
        i += 1
    
    return sum


# 2.8
def encrypt(s):
    '''
    (string) => string
    
    Takes a string s and returns it altered in the following manner
        > Firstly, reverses the string
        > Then the first and last become first and second, then second and second last become third and fourth and so on
    '''

    
    str = ''
    i = -1
    j = 0
    length = len(s)

    # reverse the string
    while i >= -length // 2:
        str +=  s[i] + s[j]

        i -= 1
        j += 1
    
    # fix odd length string issues
    if length % 2 != 0:
        return str[0:length]
    
    else:
        return str

    
# 2.9
def oPify(s):
    '''
    (string) => string
    
    Takes a string s and returns it modified according to the following rules
        > Inserts o and p between every pair of consecutive characters (a => z)
        > If the first letter in the pair is capitalized, insert O
        > If the first letter in the pair is lowercase, insert o
        > If the second letter in the pair is capitalized, insert P
        > If the second letter in the pair is lowercase, insert p
        > If len(s) < 2, return s
    '''

    i = 0
    op = ''
    length = len(s)

    while i < length:
        if i == length - 1: # prevent indexOutOfBounds error
            op += s[i]

        elif s[i].isalpha():
            first = ord(s[i]) # using ord() to check if consecutive via character values
            second = ord(s[i + 1])
            lower1 = ord(s[i].lower())
            lower2 = ord(s[i + 1].lower())

            op += s[i]

            if lower2 - lower1 == 1 and second >= 97 and first <= 90: # capital first, lowercase second
                op += 'Op'
    
            elif lower2 - lower1 == 1 and second <= 90 and first <= 90: # capital first, capital second
                op += 'OP'

            elif lower2 - lower1 == 1 and second <= 90 and first >= 97: # lowercase first, capital second
                op += 'oP'

            elif lower2 - lower1 == 1 and second >= 97 and first >= 97: # lowercase first, lowercase second
                op += 'op' 

        else:
            op += s[i]

        i += 1
    
    return op
        

# 2.10
def nonrepetitive(s):
    '''
    (string) => Boolean
    
    Takes a string s and returns True if no substring appears twice in a row
    '''

    i = 1
    length = len(s)

    while i <= length // 2: # cover all possible substring lengths
        j = 0
        
        while j <= length - 2 * i: # iterate through s to check all starting indexes for substrings of the current length i
            if s[j:j + i] == s[j + i:j + 2 * i]:
                return False
            
            j += 1

        i += 1
    
    return True