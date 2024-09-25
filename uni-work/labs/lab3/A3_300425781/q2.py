#== Exercise 2 ==#
def rps(p1, p2):
    '''
    (string, string) => number

    Takes inputs for a game of rock paper scissors, and returns a value based on the victor
        > -1 if p1 wins
        > 1 if p2 wins
        > 0 if a tie occurs
    
    Precondition: inputs must be 'R', 'P', or 'S'
    '''

    if p1 == p2:
        return 0
    
    elif (p1 == 'R' and p2 == 'S') or (p1 == 'P' and p2 == 'R') or (p1 == 'S' and p2 == 'P'):
        return -1
    
    else:
        return 1
    
print(rps('R', 'P'))
print(rps('R', 'S'))
print(rps('R', 'R'))