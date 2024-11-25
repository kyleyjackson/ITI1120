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
    removeables = string.punctuation + '0123456789'
    dict0 = dict()

    for quote in raw:
        quote = quote.lower() # 1

        quote = quote.translate(str.maketrans('', '', removeables)) # 3, 4, partial 5
        words = quote.split() # 2

        for word in words:
            if len(word) >= 3 and word in dict0 and word.isalpha(): # 6
                dict0[word] = dict0[word] + 1
            
            elif len(word) >= 3 and word.isalpha():
                dict0[word] = 1
            
    return dict0

    

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    pass
    

##############################
# main
##############################
file = open_file()
d = read_file(file)
query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE

