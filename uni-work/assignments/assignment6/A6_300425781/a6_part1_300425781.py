import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    
    fn = input('Enter the name of the file: ')
    fn = fn.strip()
    invalid = True
    file0 = None

    while invalid:
        try:
            file0 = open(fn)

        except FileNotFoundError:
            print('The specified file does not exist.')
            fn = input('Enter the name of the file: ')
        
        else:
            invalid = False

    return file0


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    
    raw = fp.read().splitlines()
    dict0 = dict()
    line = 1

    for quote in raw:
        quote = cleanUp(quote) # 1, 3, 4, 5
        words = quote.split() # 2

        for word in words:
            if len(word) >= 2:
                if word in dict0 and word.isalpha() and line not in dict0[word]: # 6
                    dict0[word].add(line)
                
                elif word.isalpha():
                    dict0[word] = {line}
            
        line = line + 1

    return dict0


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    
    queries = query.split() # list of each query
    arr = []

    for item in queries:
        arr.append(D.get(item))
    
    if None in arr: # if the string does not exist
        return [-1]
    
    arr0 = []

    for set0 in arr:
        for i in set0:
            arr0.append(i)
    
    if len(arr0) == len(removeDuplicates(arr0)) and len(arr) > 1: # if the queries don't coexist on the same line
        return [-2]
    
    elif len(arr) == 1:
        return isort(list(D[query]))
    
    else:
        arr0 = formatList(arr0)
        return isort(arr0)


#*HELPERS
def isort(arr): # this was taken from my A5
    '''
    (int[]) => int[]
    
    Returns a sorted version of the unsorted arr

    Precondition: arr is a list of integer values
    '''

    if len(arr) <= 1: # if length of 0 or 1, array is sorted by default
        return arr

    for i in range(1, len(arr)):
        c = arr[i]
        j = i - 1

        while j >= 0 and c < arr[j]: # keep moving elements greater than c up in indecies
            arr[j + 1] = arr[j]
            j = j - 1
        
        arr[j + 1] = c # insert
    
    return arr


def cleanUp(s):
    '''
    (str) => str
    
    Cleans up the string by converting everything to lowercase and removing all non-letter characters
    Returns the cleaned up string
    '''
    s = s.lower().strip()
    removeables = string.punctuation + '0123456789'
    
    return s.translate(str.maketrans('', '', removeables))
    

def formatList(arr):
    '''
    (int[]) => int[]
    
    Formats a list following the steps below
        > All non duplicates are removed
        > Then the duplicate elements are removed until one copy of each is left
    '''
    
    arr1 = list(arr)

    for line in arr:
        if arr.count(line) <= 1:
            arr1.remove(line)
    
    return removeDuplicates(arr1)


def invalidWord(s, dict0):
    '''
    (str) => str
    
    Returns the word in s that is not in dict0
    '''

    arr = s.split()

    for i in range(len(arr)):
        if arr[i] not in dict0:
            return arr[i]


def removeDuplicates(arr):
    return list(dict.fromkeys(arr))


##############################
# main
##############################
file = open_file()
d = read_file(file)
query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
continued = True

while continued:
    if cleanUp(query) == 'q':
        print('\nGoodbye.')
        continued = False
    
    else:
        indecies = find_coexistance(d, cleanUp(query))

        if indecies == [-1] or cleanUp(query) == '':
            print('The word \'' + invalidWord(query, d) + '\' is not in the file.')
        
        elif indecies == [-2]:
            print('The words you have specified do not coexist on the same line.')
        
        else:
            print('The word(s) you entered coexist in the following line(s) of the file:')
            str0 = ''

            for i in indecies:
                str0 = str0 + str(i) + ' '
            
            print(str0)

        query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()