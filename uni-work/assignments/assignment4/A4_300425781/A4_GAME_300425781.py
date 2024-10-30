# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

#! NO SET DICTIONARIES, break, continue, OR GLOBAL VARIABLES

import random

def wait_for_player():
    '''
    () => None

    Pauses the program until the user presses enter
    '''

    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''
    () => str[]

    Returns a list of strings representing the playing deck, with one queen missing.
    '''

    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)

    deck.remove('Q\u2663') # remove a queen as the game requires

    return deck


def shuffle_deck(deck):
    '''
    (str[]) => None

    Shuffles the given list of strings representing the playing deck    
    '''
    
    random.shuffle(deck)


#* COMPLETE ALL FUNCTIONS BELOW
def deal_cards(deck):
    '''
    (str[]) => (str[], str[])

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''

    dealer = []
    other = []
    h = len(deck) // 2
    rand = random.randint(1, 2)

    # randomize who gets the extra card
    if rand == 1: # player gets 26
        for i in range(h):
            other.append(deck[i])
            deck.pop(i)
        
        dealer = deck

    else: # npc gets 26
        for i in range(h):
            dealer.append(deck[i])
            deck.pop(i)
        
        other = deck


    return (dealer, other)


def remove_pairs(l):
    '''
    (str[]) => str[]

    Returns a copy of list l where all the pairs from l are removed AND
    the elements of the new list shuffled

    Precondition: elements of l are cards represented as strings described above

    Testing:
    Note that for the individual calls below, the function should
    return the displayed list but not necessarily in the order given in the examples.

    >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
    ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
    >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
    ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    arr = []
    symbols = []
    vals = []

    # separate symbols and values
    for i in l:
        vals.append(i[0:len(i) - 1])
        symbols.append(i[len(i) - 1])
    
    # deal with values only
    for i in vals:
        if i not in arr:
            arr.append(i)
        
        elif i in arr:
            arr.remove(i)
    
    # add symbols
    for i in range(len(arr)):
        arr[i] += symbols[vals.index(arr[i])]

    random.shuffle(arr)

    return arr


def print_deck(deck):
    '''
    ([]) => None

    Prints elements of a given list deck separated by a space
    '''

    str = ''

    for i in deck:
        str += i + ' '
    
    print(str.strip())

    
def get_valid_input(n):
    '''
    (int) => int
    
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
    
    Precondition: n >= 1
    '''

    i = input('Please enter an integer between 1 and ' + str(n) + ': ')
    isInvalid = False

    if not(i.isdigit()) or int(i) < 1 or int(i) > n:
        isInvalid = True

        while isInvalid:
            i = input('Invalid input. Please enter an integer between 1 and ' + str(n) + ': ')

            if i.isdigit() and int(i) <= n and int(i) > 0:
                isInvalid = False
            
    return int(i)

    

def play_game():
    '''
    () => None

    This function plays the game
    '''

    # initialize game
    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)
    dealer = tmp[0]
    human = tmp[1]
    gameOver = False

    # intro dialogue
    print('============================================')
    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:\n")
    print_deck(human)
    print()
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    
    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    while not(gameOver):
        # player turn start
        print('***********************************************************')
        print('Your turn.\n')
        print('Your current hand is:\n')
        print_deck(human)
        print()
        print('I have ' + str(len(dealer)) + ' cards.')
        print('1 will be my first card, and ' + str(len(dealer)) + ' will be my last.')
        print('Which card would you like?')
        
        # grab dealer card
        picked = get_valid_input(len(dealer))
        print()
        
        # suffix creator
        if picked == 1:
            print('You took my 1st card.')
        
        elif picked == 2:
            print('You took my 2nd card.')
        
        elif picked == 3:
            print('You took my 3rd card.')
        
        else:
            print('You took my ' + str(picked) + 'th card.')
        
        # remove card
        print('It is a ' + dealer[picked - 1] + '\n')

        human.append(dealer[picked - 1])
        dealer.pop(picked - 1)

        print('With the ' + human[len(human) - 1] + ' added, your hand is now: \n')
        print_deck(human)
        print()
        
        # shuffle and remove pairs
        human = remove_pairs(human)

        print('After shuffling and removing pairs, your hand is now: \n')
        print_deck(human)

        wait_for_player()
        
        # check if someone won
        if len(dealer) == 0:
            print('***********************************************************')
            print('Oh! I\'m out of cards!')
            print('I win! Better luck next time!')

            return
        
        elif len(human) == 0:
            print('***********************************************************')
            print('Oh... you\'re out of cards!')
            print('You win! Congratulations!')

            return

        # robot turn start
        print('***********************************************************')
        print('My turn.\n')
        
        # remove card
        randInt = random.randint(1, len(human))
        dealer.append(human[randInt - 1])
        human.pop(randInt - 1)

        # suffix creator
        if randInt == 1:
            print('I took your 1st card.')
        
        elif randInt == 2:
            print('I took your 2nd card.')
        
        elif randInt == 3:
            print('I took your 3rd card.')
        
        else:
            print('I took your ' + str(randInt) + 'th card.')
        
        # shuffle and remove pairs
        dealer = remove_pairs(dealer)
        wait_for_player()
        
        # check if someone won
        if len(dealer) == 0:
            print('***********************************************************')
            print('Oh! I\'m out of cards!')
            print('I win! Better luck next time!')

            gameOver = True
        
        elif len(human) == 0:
            print('***********************************************************')
            print('Oh... you\'re out of cards!')
            print('You win! Congratulations!')

            gameOver = True

# main
play_game()