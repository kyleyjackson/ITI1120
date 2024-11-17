# an implementation with while loop
def linear_search_v1(lst, value):
    '''
    ([], object]) => int

    Returns the index of the first occurrence of value in lst
    Returns -1 if value is not in lst
    '''

    i = -1 

    while i != -1 * len(lst) and lst[i] != value:
        i = i - 1
    
    if i == len(lst):
        return -1
    else:
        return lst.index(value)
     
print(linear_search_v1([1, 2, 3, 4, 5, 4], 4)) # 3
print(linear_search_v1(['a', 'b', '34', 34, 'asfh', 14, 14, 14, 12], 'b')) # 1

# an implementation with for loop
def linear_search_v2(lst, value):
    '''
    ([], object]) => int

    Returns the index of the first occurrence of value in lst
    Returns -1 if value is not in lst
    '''

    i = -1

    while i >= -1 * len(lst):
        if lst[i] == value:
            return lst.index(value)
        
        i -= 1

    return -1

print(linear_search_v2([1, 2, 3, 4, 5, 4], 4))
print(linear_search_v2(['a', 'b', '34', 34, 'asfh', 14, 14, 14, 12], 'b'))

def linear_search_v3(lst, value):
    '''
    ([], object]) => int

    Returns the index of the first occurrence of value in lst
    Returns -1 if value is not in lst
    '''

    lst.append(value)

    i = -1

    while lst[i] != value:
        i = i - 1

    lst.pop()

    if i == -1 * len(lst):
        return -1
    else:
        return lst.index(value)

print(linear_search_v3([1, 2, 3, 4, 5, 4], 4))
print(linear_search_v3(['a', 'b', '34', 34, 'asfh', 14, 14, 14, 12], 'b'))