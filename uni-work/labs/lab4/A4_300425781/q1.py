#=== Exercise One ===#
def is_eligible(age, citizenship, prison):
    '''
    (int, str, str) => None
    
    Takes an integer value for the user's age, along with strings stating whether they are a Canadian citizen and current living in prison
    Then prints a message stating if the user is eligible to vote
    '''
    # check if citizen
    if citizenship.upper().strip() == 'CANADIAN' or citizenship.upper().strip() == 'CANADA':
        citizenship = True
    
    else:
        citizenship = False

    # check if criminal record
    if prison.upper().strip() == 'NO':
        prison = False
    
    elif prison.upper().strip() == 'YES':
        prison = True

    print(age, citizenship, prison)

    if age > 17 and citizenship and not(prison):
        print('Congratulations, you are eligible to vote!')

    else:
        print('Unfortunately, you are not able to vote.')

# take inputs
age = int(input('What is your age? '))
citizenship = input('What country are you a citizen of? ')
prison = input('Do you currently live in prison due to a criminal offense? ')

# call function
is_eligible(age, citizenship, prison)