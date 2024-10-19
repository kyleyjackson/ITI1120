
#! NO SET DICTIONARIES, break, continue, OR GLOBAL VARIABLES
def read_raw(file):
    '''
    (str) => str[]

    Returns a list of strings that was stored in a file.
    '''
    raw = open(file).read().splitlines()

    for i in range(len(raw)):
        raw[i] = raw[i].strip()

    return raw


def clean_up(l):
    '''
    (str[]) => str[]

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed.
    Finally, l gets sorted

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''

    i = 0

    # remove asterisks
    while i < len(l): # using len(l) here as it changes throughout the loop
        if l[i] == '*': # remove all asterisks
            l.pop(i)
            i -= 1 # account for length lost
        
        i += 1
    
    j = 0

    # remove objects that appear an odd number of times
    while j < len(l): # grab the element to compare
        counter = 1 # count elements of same value
        k = 0

        while k < len(l): # begin comparing elements to l[j]
            if l[k] == l[j] and k != j: # when two elements match, increase the count, but make sure its not the same index
                counter += 1 
            
            k += 1

        if counter % 2 != 0: # if the element l[j] has appeared an odd number of times
            l.pop(j) # remove it
            j -= 1 # account for length lost
        
        j += 1
        
    # sort
    for m in range(len(l)):
        for n in range(len(l)): # compare l[m] with the entirety of l
            if ord(l[m]) < ord(l[n]): # compare unicode indecies using ord() to sort
                temp = l[n]
                l[n] = l[m]
                l[m] = temp

    return l


def is_rigorous(l):
    '''
    (str[]) => Boolean

    Returns True if every character in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is clean-up by clean_up function)

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    
    length = len(l)

    if length == 0:
        return True
    
    for i in range(length):
        temp = l[i]
        counter = 0
        
        for j in range(length):
            if temp == l[j]:
                counter += 1

                if counter > 2:
                    return False
    
    return True


#main
file = input("Enter the name of the file: ")
file = file.strip()

b = read_raw(file)
print("\nBefore clean-up:\n", b)

b = clean_up(b)
print("\nAfter clean-up:\n", b)

if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has " + str(len(b)) + " characters.")

else:
    print("\nThis list has no * but is not rigorous and it has " + str(len(b)) + " characters.")
     
