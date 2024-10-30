def ah(l, x, y):
    '''
    (list, int, int) => tuple
    
    Takes a list of numbers l and two integers x and y. Returns a tuple consisting of an integer representing the number of elements in l
    and the minimum element of l that is between x and y (inclusive)

    Preconditions:
        > x <= y
        < l is a list of numbers
    '''

    arr = []

    # take all elements between x and y inclusive 
    for i in range(len(l)):
        if l[i] >= x and l[i] <= y:
            arr.append(l[i])

    arr.sort()
    
    return (len(arr), arr[0])

# print(ah([5, 1, -2.5, 10, 13, 8], 2, 11))