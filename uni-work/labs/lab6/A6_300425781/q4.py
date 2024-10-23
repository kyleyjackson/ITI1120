def sum_5_consecutive(arr):
    '''
    (int[]) => Boolean
    
    Takes a list of integers and returns True if there are 5 consecutive numbers that add to 0.
    Otherwise returns False
    '''

    i = 0

    while i < len(arr) - 4:
        if arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] + arr[i + 4] == 0:
            return True
    
        i += 1
    
    return False