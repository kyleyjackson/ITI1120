def count_digits(n):
    '''
    (int) => int
    
    Returns the number if digits in integer n
    '''

    if n // 10 == 0:
        return 1
    
    return 1 + count_digits(n // 10)

print(count_digits(123456789))