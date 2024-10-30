# 5.16
def indexes(str, s):
    '''
    (str, str) => int[]

    Returns a list contained indecies of s in str
    '''

    arr = []

    for i in range(len(str)):
        if str[i] == s:
            arr.append(i)
    
    return arr

# print(indexes('mississippi', 'i'))

# 5.17
def doubles(arr):
    '''
    (int[]) => None

    Prints the integers in the list that are exactly double the previous integer in the list.
    Prints one integer per line.
    '''

    for i in range(len(arr) - 1):
        if arr[i] * 2 == arr[i + 1]:
            print(arr[i + 1])

# doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5])

# 5.18
def four_letter(arr):
    '''
    (str[]) => str[]
    
    Returns a list of all the 4 letter words in arr
    '''

    fourArr = []

    for i in range(len(arr)):
        if len(arr[i]) == 4:
            fourArr.append(arr[i])
    
    return fourArr

# print(four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']))

# 5.19
def inBoth(arr, arr1):
    '''
    ([], []) => Boolean
    
    Returns True if any element in arr is in arr1, or vice versa.
    Otherwise returns False
    '''

    for i in range(len(arr)):
        for j in range(len(arr1)):
            if arr[i] == arr1[j]:
                return True
    
    return False

# print(inBoth([3, 2, 5, 4, 7], [9, 0, 1, 3]))

# 5.20
def intersect(arr, arr1):
    '''
    ([], []) => []
    
    Returns all elements that are in both input lists arr and arr1
    '''

    arr2 = []

    for i in range(len(arr)):
        for j in range(len(arr1)):
            if arr[i] == arr1[j]:
                arr2.append(arr[i])
    
    return arr2

# print(intersect([3, 5, 1, 7, 9], [4, 2, 6, 3, 9]))

# 5.21
def pair(arr, arr1, n):
    '''
    (int[], int[], int) => None
    
    Prints the pairs of integers that add up to n
    '''

    for i in range(len(arr)):
        for j in range(len(arr1)):
            if arr[i] + arr1[j] == n:
                print(str(arr[i]) + ' ' + str(arr1[j]))

# pair([2, 3, 4], [5, 7, 9, 12], 9)

# 5.22
def pairSum(lst, n):
    '''
    (int[], n) => None
    
    Prints the indeces of all pairs of values in lst that add up to n
    '''

    sum = 0

    for i in range(len(lst) // 2):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == n:
                print(str(i) + ' ' + str(j))
    
# pairSum([7, 8, 5, 3, 4, 6], 11)

# 5.29
def lastfirst(arr):
    '''
    (str[]) => [str[], str[]]
    
    Returns a list containing a list of first names and a list of last names taken from arr

    Precondition: each element in arr is of the format <Last name, First name>
    '''

    last = []
    first = []

    for i in range(len(arr)):
        ind = arr[i].index(',')

        last.append(arr[i][0:ind])
        first.append(arr[i][ind + 2:])
    
    return [first, last]

# print(lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob']))

# 5.31
def subsetSum(arr, target):
    '''
    (int[], int) => Boolean
    
    Returns True if there are 3 integers in arr that add up to target.
    Otherwise returns False
    '''

    for i in range(len(arr)):
        sum = arr[i]

        for j in range(len(arr)):
            if i != j:
                sum += arr[j]

                for k in range(len(arr)):
                    if i != k and j != k:
                        sum += arr[k]

                        if sum == target:
                            return True
    
    return False

# print(subsetSum([5, 4, 10, 20, 15, 19], 38))
# print(subsetSum([5, 4, 10, 20, 15, 19], 10))

# 5.33
def mystery(n):
    '''
    (int) => int
    
    Returns the number of times n can be halved using integer division before reaching 1
    '''

    counter = 0
    
    while n > 1:
        n = n // 2
        counter += 1
    
    return counter

# print(mystery(4))
# print(mystery(11))
# print(mystery(25))

# 5.46
def inversions(str):
    '''
    (str) => int
    
    Returns the number of inversions in str
    '''

    str = str.upper() # send to upper to simplify ord values
    inv = 0

    for i in range(len(str)):
        val = ord(str[i])

        j = i + 1

        while j < len(str):
            if val > ord(str[j]):
                inv += 1
            
            j += 1
    
    return inv

# print(inversions('ABBFHDL'))
# print(inversions('ABCD'))
# print(inversions('DCBA'))

# 5.48
def sublist(list1, list2):
    '''
    (int[], int[]) => Boolean
    
    Returns True if list1 is a sublist of list2.
    Otherwise returns False
    '''

    indeces = []

    for i in range(len(list1)):
        if list1[i] in list2:
            indeces.append(list2.index(list1[i]))
    
    for j in range(len(indeces) - 1):
        if indeces[j + 1] - indeces[j] < 1 or len(indeces) == 0:
            return False
    
    return True
        

# print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
# print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))

# 5.37 - MAX not MIN
def mssl(arr):
    '''
    (int[]) => int
    
    Returns the sum of the largest sublist of arr
    '''

    n = 0
    high = 0

    for i in range(len(arr)):
        n = max(n + arr[i], 0)
        high = max(high, n)
    
    return high

# print(mssl([3, 4, 5]))
# print(mssl([4, -2, -8, 5, -2, 7, 7, 2, -6, 5]))
# print(mssl([-2, -3, -5]))
# print(mssl([]))

