#=== Exercise Five ===#

# part one
def partOne(): # made function so i can test other part easily
    '''
    () => int

    Asks the user for a positive integer input then prints all of its divisors
    Returns the inputted integer
    '''

    # init stuff
    n = int(input('Enter a positive integer: '))
    m = 1
    str1 = ', '

    while m <= n:
        if n % m == 0:
            str1 += str(m) + ', '

        m += 1
    
    print(str1[2:len(str1) - 2])
    return n

# part two
def prime(n):
    '''
    (int) => Boolean
    
    Takes a positive integer and returns whether its a prime number

    Precondtion: n is and integer > -1
    '''

    # counter/moldulus num
    m = 2

    if n < 2:
        return False

    else:
        while m < n:
            if n % m == 0:
                return False

            m += 1
    
    return True

# referencing part one
print('This number is prime, this is ' + str(prime(partOne())))

# bonus part 4
def lesserPrimes():
    '''
    () => None

    Asks the user input for a positive integer. then prints all primes smaller than the number
    '''

    # init stuff
    n = int(input('Enter a positive integer: '))
    arr = []
    m = 0

    while m < n:
        if prime(m):
            arr.append(m)
        
        m += 1
    
    print(arr)

lesserPrimes()