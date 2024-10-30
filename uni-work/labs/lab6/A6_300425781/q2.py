terminated = False

while not(terminated):
    n = input('Enter the first integer: ')
    m = input('Enter the second integer: ')
    
    print('The sum of your two integers is ' + str(int(n) + int(m)))
    
    affirm = input('Do you wish to continue? ')

    if affirm.lower().strip() != 'yes':
        terminated = True