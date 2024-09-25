#2.1
def min_enclosing_rectangle(radius, x, y):
    '''
    (number, number, number) => tuple
    
    Returns the coordinates of the bottom left corner of the smallest axis-aligned rectangle that fits the circle with radius 'radius' with a center at (x, y)
    min_enclosing_rectangle() will return None if radius is a negative number

    Precondition: radius > 0
    '''

    if radius < 0: # return None if radius is negative
        return

    y -= radius
    x -= radius

    return (x, y)

#print(min_enclosing_rectangle(1, 1, 1))
#print(min_enclosing_rectangle(-1, 10, 2))
#print(min_enclosing_rectangle(500, 1000, 2000))
#print(min_enclosing_rectangle(4.5, 10, 2))

#2.2
def vote_percentage(results):
    '''
    (string) => float
    
    Takes a string containing the substrings 'yes', 'no', or 'abstained' and returns the percentage of 'yes' among all 'yes' and 'no'

    Preconditions: 
        > results contains at least one 'yes' and one 'no'
        > The only substrings are 'yes', 'no', and 'abstained'
    '''

    # occurance of 'yes' and 'no'
    numY = results.count('yes')
    numN = results.count('no')

    return numY / (numN + numY)

#print(vote_percentage('yes yes yes no abstained yesyesyes noyesno'))
#print(vote_percentage('abstainedyesyesyesnoyes'))

#2.3
def vote():
    '''
    () =>
    
    Takes the user input for a string containing the substrings 'yes', 'no', and 'abstained' and prints the outcome based on the amount of votes
        > all yes => passing unanimously
        > 2/3 yes => passing with super majority
        > 1/2 yes => passing with simple majority
        > else => vote fails
    '''

    str = input('Enter the yes, no, and abstained votes one by one then press enter when done\n')

    # make call to vote_percentage(str)
    n = vote_percentage(str)

    # check status of vote
    if n == 1.0:
        print('Vote passes unanimously.')

    elif n >= 2/3:
        print('Vote passes with super majority.')

    elif n >= 0.5:
        print('Vote passes with simple majority')

    else:
        print('Vote failed.')

#vote()

#2.4
def l2lo(w):
    '''
    (number) => tuple
    
    Takes a number w and returns a pair of numbers (l, o) such that w = 1 + o/16 and l is an integer and o is a non negative number smaller than 16.
    l and o will always be unique.

    Precondition: w is non-negative
    '''

    # take decimal point of w, get o
    # plug in o and w to get l

    wInt = int(w)
    o = (w - wInt) * 16
    l = int(w - o/16)

    return (l, o)

#print(l2lo(7.5))
#print(l2lo(9.25))
