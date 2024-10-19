
#! NO SET DICTIONARIES, break, continue, OR GLOBAL VARIABLES
def longest_run(arr):
    '''
    (numbers[]) => int
    
    Takes a list of numbers arr, and returns the length of the longest run in the list
    '''

    length = len(arr)
    counter = 1
    counter1 = 0

    if length == 0:
        return 0

    for i in range(length - 1):
        if arr[i] == arr[i + 1]:
            counter1 += 2
            j = i + 1

            while j < length - 1 and arr[j] == arr[j + 1]:
                counter1 += 1
                j += 1
        
        if counter1 > counter:
            counter = counter1
            counter1 = 0
                
    return counter

# main

# collect array numbers (Same as Q2)
nums = input('Please input a list of integers separated by spaces: ')
arr = []
i = 0

# turn string into list
while i < len(nums):
    temp = ''

    if nums[i].isdigit() or nums[i] == '-' or nums[i] == '.':
        j = i
        k = 0

        while j < len(nums) and (nums[j].isdigit() or nums[j] == '-' or nums[j] == '.'):
            temp += nums[j]
            j += 1
            k += 1
        
        i += k
        arr.append(float(temp))

    i += 1

longest_run(arr)