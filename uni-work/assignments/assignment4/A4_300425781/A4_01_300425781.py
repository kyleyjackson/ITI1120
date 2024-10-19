
#! NO SET DICTIONARIES, break, continue, OR GLOBAL VARIABLES
def number_divisible(arr, n):
    '''
    (int[], int) => int
    
    Takes a list of integers arr, and returns the number of elements in arr that are divisible by n
    '''

    counter = 0

    for i in range(len(arr)):
        if arr[i] % n == 0:
            counter += 1
    
    return counter

# main

# collect array numbers
nums = input('Please input a list of integers separated by spaces: ')
arr = []
i = 0

# turn string into list
while i < len(nums):
    temp = ''

    if nums[i].isdigit() or nums[i] == '-':
        j = i
        k = 0

        while j < len(nums) and (nums[j].isdigit() or nums[j] == '-'):
            temp += nums[j]
            j += 1
            k += 1
        
        i += k
        arr.append(int(temp))

    i += 1

# ask for divisor
n = input('Please input an integer: ')
m = number_divisible(arr, int(n))

print('The number of elements divisible by ' + n + ' is ' + str(m))