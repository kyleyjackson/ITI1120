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

    no_pairs = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    random.shuffle(no_pairs)

    return no_pairs


def print_deck(deck):
    '''
    ([]) => None

    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    
def get_valid_input(n):
    '''
    (int) => int
    
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
    
    Precondition: n >= 1
    '''

    

def play_game():
    '''
    () => None

    This function plays the game
    '''

    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print(dealer)
    print(human)

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    
    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE
	
	 

# main
play_game()