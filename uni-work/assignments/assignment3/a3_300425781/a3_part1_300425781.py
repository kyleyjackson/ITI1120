#! NO ARRAYS, TUPLES, OR SET DICTIONARIES
def split_tester(N, d):
    # Your code for split_tester function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''
    (string, string) => Boolean
    
    Takes a sequence of numbers N which are to be split into groups of length d. If N cannot be split into groups of length d, this functions returns False
    Else, if the groups are increasing in numerical value, this function returns True, otherwise this function returns False
    '''

    # length for iteration
    length = len(N)
    m = 0

    # new stuff
    i = 0
    sub = ''

    # check if N only contains numbers
    if not(N.isdigit()):
        return False

    # check if N can be split into groups of length d
    if length % int(d) != 0:
        return False
    
    else:
        while m <= length:
            if len(sub) == int(d): # when split reaches desired length
                if int(sub) > i: # check if increasing
                    i = int(sub)

                    if m < length:
                        sub = N[m]
                    
                    else:
                        sub = ''

                else:
                    return False
            
            else: # otherwise...
                sub += N[m]
            
            print(m, length, sub, i)
            m += 1
    
    return True

# you can add more function definitions here if you like       

def welcomeMessage(str):
    '''
    (string) => None

    Prints a welcome message board based with the specified string
    '''

    strLen = len(str) #length of inputted string
    b = '*' # border
    s = ' ' # empty spaces

    #printing the board
    print()
    print(b * (strLen + 10))
    print(b + s * (strLen + 8) + b)
    print(b + '  __' + str + '__  ' + b)
    print(b + s * (strLen + 8) + b)
    print(b * (strLen + 10))
    print()
            
# main
# Your code for the welcome message goes here, instead of name="Vida"
welcomeMessage('Welcome to my increasing-splits tester')
name = input('What is your name? ')

flag = True
welcomeMessage(name + ' welcome to my increasing-splits tester')

while flag:
    question = input(name + ", would you like to test if a number admits an increasing-split of given size? ")
    question = (question.strip()).lower()
    
    if question == 'no':
        flag = False
        welcomeMessage('Goodbye ' + name)

    elif question == 'yes':
        pass

    else:
        ''
