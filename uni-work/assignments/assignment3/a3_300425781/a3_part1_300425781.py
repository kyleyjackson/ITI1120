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
    display = ''
    result = True

    # check if N only contains numbers
    if not(N.isdigit()):
        result = False

    # check if N can be split into groups of length d
    elif length % int(d) != 0:
        result = False
    
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
                    result = False
            
            else: # otherwise...
                sub += N[m]
            
            if len(sub) == int(d):
                display += sub + ', '

            m += 1

    print(display[0:len(display) - 2])
    if not(result):
        return False
    
    else:
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

def ansYes():
    '''
    () => None
    
    Prompts the user for a positive integer N and split d, then prints if N split into groups of d length is increasing
    '''

    N = input('Enter a positive integer: ').strip()

    # check if N is an integer in string form
    if not(N.isdigit()) or float(N) % 1 != 0 or float(N) < 1:
        no = True

        while no:
            N = input('The input must be a positive integer, try again: ')

            if N.isdigit() and float(N) % 1 == 0 and float(N) > 0:
                no = False
            
            else:
                no = True
    
    d = input('Input the split. The split has to divide the length of ' + N + ' (i.e. ' + str(len(N)) + '): ').strip()

    # check if N is divisible by d
    if not(d.isdigit()) or int(d) < 1 or int(N) % int(d) != 0:
        no = True

        while no:
            if d.isdigit() and int(d) > 0 and int(N) % int(d) == 0:
                no = False
            
            else:
                d = input('The split must divide the length of ' + N + ' (i.e. ' + str(len(N)) + '), try again: ')
                no = True
        
    bool = split_tester(N, d)

    if bool:
        print('The sequence is increasing')
    
    else:
        print('The sequence is not increasing')
            
# main
# Your code for the welcome message goes here, instead of name="Vida"
welcomeMessage('Welcome to my increasing-splits tester')
name = input('What is your name? ')

flag = True
welcomeMessage(name + ', welcome to my increasing-splits tester')

while flag:
    question = input(name + ", would you like to test if a number admits an increasing-split of given size? ")
    question = (question.strip()).lower()

    if question != 'yes' and question != 'no':
        no = True
        
        while no:
            if question == 'yes':
                no = False
                print('Good choice')
                ansYes()
            
            elif question == 'no':
                no = False
                flag = False
            
            else:
                question = input('Please input yes or no: ')
                no = True

    elif question == 'yes':
        print('Good choice!')
        ansYes()
       
    else:
        flag = False

welcomeMessage('Goodbye ' + name)