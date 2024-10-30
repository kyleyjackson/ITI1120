def first_neg(arr):
    '''
    (int[]) => int

    Takes a list of numbers and returns the index of the first negative number
    '''

    i = 0

    while i < len(arr):
        if arr[i] < 0:
            return i

        i += 1

    return