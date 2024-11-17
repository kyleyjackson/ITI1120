import sys

def min_or_max_index(arr, bool):
    '''
    (int[], bool) => tuple

    If bool is True, then return a tuple with the smallest value and its index
    If bool is False, then return a tuple with the largest value and its index
    '''

    if bool:
        min0 = sys.maxsize # big number

        for i in range(len(arr)):
            if arr[i] < min0:
                min0 = arr[i]

        return (min0, arr.index(min0))
    
    else:
        max0 = 0

        for i in range(len(arr)):
            if arr[i] > max0:
                max0 = arr[i]

        return (max0, arr.index(max0))

print(min_or_max_index([1, 2, 3, 4, 5], True))
print(min_or_max_index([1, 2, 3, 4, 5], False))