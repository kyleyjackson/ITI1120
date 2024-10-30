def sum_odd_while_v2(n):
    '''
    (int)) => int

    Returns the sum of all odd integers between 5 and n
    '''

    i = 5
    m = 0
    
    while i <= n:
        m += i * (i % 2)
        i += 1
    
    return m