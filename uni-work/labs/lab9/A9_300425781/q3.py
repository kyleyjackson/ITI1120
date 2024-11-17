def first_one(L):
    '''
    (int[]) => int
    
    Takes a list of 0's and 1's L, and returns the position of the first 1
    Returns -1 if the list contains no 1's

    Preconditions:
        > L only contains 0 and/or 1
        > All 0 values come before 1 values
    '''

    if 1 in L:
        return L.index(1)

    return -1

print(first_one([0, 0, 0, 0, 0, 0, 1, 1]))
print(first_one([1, 1]))
print(first_one([0, 0, 0]))

def last_zero(L):
    '''
    (int[]) => int
    
    Takes a list of 0's and 1's L, and returns the position of the last 0
    Returns -1 if the list contains no 0's

    Preconditions:
        > L only contains 0 and/or 1
        > All 0 values come before 1 values
    '''

    for i in reversed(range(len(L))):
        if L[i] == 0:
            return i

    return -1

print(last_zero([0, 0, 0, 0, 0, 0, 1, 1]))
print(last_zero([1, 1]))
print(last_zero([0, 0, 0]))