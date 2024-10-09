def is_sorted(arr):
    '''
    (list) => Boolean
    
    Takes a list arr and hreturns True if the the list is sorted from smallest to largest
    returns false otherwise

    Precondition: arr is a list of numbers
    '''

    # array of length 1 is sorted
    if len(arr) == 1:
        return True


    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True

# print(is_sorted([-5, -1, 3, 7, 11]))
# print(is_sorted([0, -1, 7]))
# print(is_sorted([5, 10, 15, 24, 29]))
# print(is_sorted([3]))