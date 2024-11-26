def digit_sum(n):
    '''
    (int) => int
    
    Returns the sum of all digits of n

    Precondition: n is a non-negative integer
    '''

    if n < 10: # avoid maximum recursion depth error
        return n
    
    return (n % 10 + digit_sum(int(n / 10)))



def digital_root(n):
    '''
    (int) => int
    
    Returns the digital root of n

    Precondition: n is a non-negative integer
    '''

    if n < 10:
        return digit_sum(n)
    
    return digit_sum(digit_sum(n))