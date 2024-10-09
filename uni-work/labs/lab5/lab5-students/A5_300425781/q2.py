def is_perfect(n):
    '''
    (int) => Boolean
    
    Takes a positive integer n and returns True if it's the sum of all its positive divisors excluding itself
    Returns False otherwise
    '''

    i = 1
    sum = 0

    while i < n:
        if n % i == 0:
            sum += i

        i += 1
    
    return sum == n


# main
arr = []

for i in range(10000):
    if is_perfect(i) and i != 0:
        arr.append(i)
    
print(arr)


# modified part for 5th num
arr = []

for i in range(35000000):
    if is_perfect(i) and i != 0:
        arr.append(i)
    
print(arr)

