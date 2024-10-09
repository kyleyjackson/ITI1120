def arithmetic(arr):
    '''
    (list) => Boolean
    
    Takes a list arr and hreturns True if the difference between each pair of consecutive numbers is the same
    returns false otherwise

    Precondition: arr is a list of numbers
    '''

    # sequence of length 1 is arithmetic 
    if len(arr) == 1:
        return True

    diff = 0

    for i in range(len(arr) - 1):
        if i == 0:
            diff = arr[i + 1] - arr[i]
        
        else:
            if not(diff == arr[i + 1] - arr[i]):
                return False
    
    return True

# print(arithmetic([-5, -1, 3, 7, 11]))
# print(arithmetic([0, -1, 7]))
# print(arithmetic([5, 10, 15, 24, 29]))
# print(arithmetic([3]))