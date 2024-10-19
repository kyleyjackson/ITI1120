
#! NO SET DICTIONARIES, break, continue, OR GLOBAL VARIABLES
def two_length_run(arr):
    '''
    (numbers[]) => Boolean
    
    Takes a list of numbers arr, and returns True if it has a run (consecutive repeated values) of at least length 2. Returns False otherwise
    '''

    print(arr)
    length = len(arr)

    # length 1
    if length == 1: # run must be at least length 2
        return False

    # length >= 2
    else:
        for i in range(length - 1):
            if int(arr[i]) == int(arr[i + 1]):
                return True
        
    return False

# main

# collect array numbers (modified from Q1)
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

print(two_length_run(arr)) # call function