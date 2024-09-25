#== Exercise 3A ==#
def is_divisible(n, m):
    '''
    (int, int) => Boolean

    Returns True if n is divisible by m, else returns False
    '''

    return n % m == 0

n = input('Enter 1st integer: ')
m = input('Enter 2nd integer: ')
o = is_divisible(int(n), int(m))

if o:
    print(n + ' is divisible by ' + m)

else:
    print(n + ' is not divisible by ' + m)
