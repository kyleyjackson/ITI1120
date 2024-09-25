#== Exercise 3B ==#
def is_divisible(n, m):
    '''
    (int, int) => Boolean

    Returns True if n is divisible by m, else returns False
    '''

    return n % m == 0

def is_divisible23n8(n):
    '''
    (int) => string
    
    Returns 'yes' if n is divisible by 2 or 3, but not 8.
    Otherwise, returns 'no'
    '''

    if (is_divisible(n, 2) or is_divisible(n, 3)) and not(is_divisible(n, 8)):
        print(str(n) + ' is divisible by 2 or 3, but not 8')
        return 'yes'

    else:
        print('It is not true that ' + str(n) + ' is divisible by 2 or 3, but not 8')
        return 'no'

n = int(input('Enter an integer: '))
print(is_divisible23n8(n))