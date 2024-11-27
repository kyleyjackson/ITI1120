def gcd(a, b):
    '''
    (int, int) => int
    
    Returns the greatest common factor of a and b

    Precondition: a >= b
    '''

    if b == 0:
        return a
    
    return gcd(b, a % b)

print(gcd(36, 20))
print(gcd(12, 8))