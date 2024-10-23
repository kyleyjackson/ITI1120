def fib(n):
    '''
    (int) => int[]

    Returns the n fibonacci numbers as a list
    '''

    arr = []
    first = 0
    second = 1

    for i in range(n):
        temp = first + second
        first = second
        second = temp

        arr.append(first)
    
    return arr