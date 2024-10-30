def inner_product(arr, arr1):
    '''
    (int[], int[]) => int
    
    Takes two lists of equal length and returns their dot product (x1y1 + ... + xnyn)

    Precondition: arr and arr1 are equal in length
    '''

    dot = 0

    for i in range(len(arr)):
        dot += arr[i] * arr1[i]
    
    return dot