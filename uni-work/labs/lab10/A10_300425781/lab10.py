import random
import math
import sys

class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'
    
    def distance(self, other):
        '''
        (Point, Point) => float 
        
        Returns the distance from the invoking Point to the other Point
        '''

        dx = other.x - self.x
        dy = other.y - self.y

        return math.sqrt((dx ** 2) + (dy ** 2))
    
    def up(self):
        self.sety(self.y + 1)
    
    def down(self):
        self.sety(self.y - 1)

    def left(self):
        self.setx(self.x - 1)

    def right(self):
        self.setx(self.x + 1)


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age = 0):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)

    def getAge(self):
        '''Returns the Animal's age value'''
        return self.age
    


class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit
    
    def __gt__(self, other):
        '''Returns result of self.rank > other.rank'''
        return self.rank > other.rank

    def __ge__(self, other):
        '''Returns result of self.rank >= other.rank'''
        return self.rank >= other.rank

    def __lt__(self, other):
        '''Returns result of self.rank < other.rank'''
        return self.rank < other.rank

    def __le__(self, other):
        '''Returns result of self.rank <= other.rank'''
        return self.rank <= other.rank


class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)

    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck
    

class BankAccount:

    # overloads
    def __init__(self, balance = 0):
        '''Initialize the bank account with a value of balance'''
        self.bal = balance

    def __repr__(self):
        '''Canonical string representation BankAccount(bal)'''
        return 'BankAccount(' + str(self.bal) + ')'

    # methods
    def withdraw(self, val):
        '''
        (BankAccount, int) => None

        Withdraws val from the invoking BankAccount's balance
        Prints a message if val > self
        '''
        if val > self.bal:
            print('You don\'t have enough money to withdraw this amount')
        
        else:
            self.bal = self.bal - val
    
    def deposit(self, val):
        '''
        (BankAccount, int) => None

        Adds money to the BankAccount's balance
        '''
        self.bal = self.bal + val

    def balance(self):
        '''Returns the balance of the invoking BankAccount'''
        return self.bal


class PingPong:

    def __init__(self):
        '''Initialize PingPong with int representing if Ping or Ping was last printed'''
        self.int = 0

    def next(self):
        '''Prints PING or PONG depending on which was printed last'''
        if self.int == 0:
            print('PING')
            self.int = 1
        
        else:
            print('PONG')
            self.int = 0


class Queue:

    # overloads
    def __init__(self):
        '''Initializes an empty Queue'''
        self.queue = []

    def __repr__(self):
        '''Canonical string representation Queue(queue)'''
        return 'Queue(' + str(self.queue) + ')'
    
    def __eq__(self, other):
        '''Returns True if both Queues are equal in length, False otherwise'''
        return len(self.queue) == len(other.queue)
    
    def __len__(self):
        '''Returns the length of the invoking Queue'''
        return len(self.queue)

    # methods
    def enqueue(self, item):
        '''
        (Queue, object) => None
        
        Adds an item to the Queue
        '''
        self.queue.append(item)

    def dequeue(self):
        '''Removes the item from the front of the Queue'''
        temp = self.queue[0]
        self.queue.pop(0)

        return temp
    
    def isEmpty(self):
        '''Returns True if the Queue is empty, False otherwise'''
        return len(self.queue) == 0


class Vector(Point):

    # overloads
    def __repr__(self):
        '''Canonical string representation Vector(x, y)'''
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def __add__(self, other):
        '''Allows for addition of Vector objects'''
        return 'Vector(' + str(self.x + other.x) + ', ' + str(self.y + other.y) + ')'
    
    def __mul__(self, other):
        '''Returns the dot product of the self and other Vectors'''
        return (self.x * other.x) + (self.y * other.y)
    

class Marsupial:

    # overloads
    def __init__(self, col = 'white'):
        '''Initializes a Marsupial object with default colour white and empty pouch'''
        self.colour = col
        self.pouch = []

    def __repr__(self):
        '''Canonical string representation "I am a self.colour Marsupial."'''
        return 'I am a ' + self.colour + ' Marsupial.'
    
    # methods
    def put_in_pouch(self, item):
        '''
        (Marsupial, str) => None
        
        Puts in item in the Marsupial
        '''
        self.pouch.append(item)
    
    def pouch_contents(self):
        '''Prints self.pouch'''
        print(self.pouch)


class Kangaroo(Marsupial):

    # overloads
    def __init__(self, col, xc = 0, yc = 0):
        '''Initializes Kangroo with colour, coordinates and empty pouch'''
        self.colour = col
        self.x = xc
        self.y = yc
        self.pouch = []
    
    def __repr__(self):
        '''
        Canonical string representation 
        "I am a self.colour Kangaroo located at coordinates (self.x, self.y)"
        '''
        return 'I am a ' + self.colour + ' Kangaroo, located at coordinates (' + str(self.x) + ', ' + str(self.y) + ')'
    
    # methods
    def jump(self, dx, dy):
        '''
        (Kangaroo, int, int) => None

        Moves the Kangroo by dx x distance and dy y distance
        '''

        self.x = self.x + dx
        self.y = self.y + dy


class Points(Point):

    # overloads
    def __init__(self, arr = []):
        self.points = arr
    
    def __len__(self):
        '''Allows for usage of len() with Points objects'''
        return len(self.points)
    
    def __repr__(self):
        '''Canonical string representation Points(points)'''
        return 'Points(' + str(self.points) + ')'
    
    # methods
    def add(self, xc, yc):
        '''Adds a Point to the Points array with coordinates (xc, yc)'''
        self.points.append(Point(xc, yc))

    def left_most_point(self):
        '''Returns the left most Point, if there are two, it returns the bottom left most point'''

        minPoint = Point(sys.maxsize, sys.maxsize)

        for point in self.points:
            if minPoint.x == point.x:
                if point.y < minPoint.y:
                    minPoint = point
            
            elif minPoint.x > point.x:
                minPoint = point
        
        return minPoint
    

# class-testing functions
def testPoint():
    print('--- TESTING POINT ---')
    c = Point(0, 1)
    c.sety(0) # (0, 0)
    print(c.get())

    d = Point(4, 3)
    print(d.get())

    print(c.distance(d)) # 5.0

    c.up() # (0, 1)
    c.left() # (-1, 1)
    print(c.get())

    d.right() # (5, 3)
    d.down() # (5, 2)
    print(d.get())

# testPoint()


def testAnimal():
    print()
    print('--- TESTING ANIMAL ---')
    dog = Animal('dog', 'woof', 3)
    print(dog.getAge())

    # testing card
    print()
    print('--- TESTING CARD ---')

    c1 = Card('3', '\u2660')
    c2 = Card('5', '\u2662')

    print(c1)
    print(c2)

    print(c1 < c2)
    print(c1 > c2)
    print(c1 <= c2)

# testAnimal


def testBankAccount():
    print()
    print('--- TESTING BANKACCOUNT ---')

    acc = BankAccount(700)
    print(acc)

    acc.withdraw(70)
    print(acc.balance())

    acc.withdraw(1000)
    print(acc.balance())

    acc.deposit(7)
    print(acc.balance())

    print(acc)

# testBankAccount()


def testPingPong():
    print()
    print('--- TESTING PINGPONG ---')

    ball = PingPong()
    ball.next()
    ball.next()
    ball.next()
    ball.next()
    ball.next()

# testPingPong()


def testQueue():
    print()
    print('--- TESTING QUEUE ---')

    q = Queue()
    print(q)

    q.enqueue('John')
    q.enqueue('Annie')
    q.enqueue('Sandy')
    print(q)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.isEmpty())

    q1 = Queue()
    q1.enqueue('kiwi')
    q1.enqueue('apple')
    print(q1)
    print(len(q1))

    q2 = Queue()
    q2.enqueue('kiwi')
    print(q2)

    print(q1 == q2)

    print(q1.dequeue())
    print(q1 == q2)

# testQueue()


def testVector():
    v1 = Vector(1, 3)
    v2 = Vector(-2, 4)

    print(v1)
    print(v2)

    print(v1 + v2)
    print(v1 * v2)

# testVector()


def testMarsupial():
    m = Marsupial('red')
    print(m)

    m.put_in_pouch('doll')
    m.put_in_pouch('firetruck')
    m.put_in_pouch('kitten')
    m.pouch_contents()

# testMarsupial()


def testKangaroo():
    k = Kangaroo('Blue', 0, 0)
    print(k)

    k.put_in_pouch('doll')
    k.put_in_pouch('firetruck')
    k.put_in_pouch('kitten')
    k.pouch_contents()

    k.jump(1, 0)
    k.jump(1, 0)
    k.jump(1, 0)
    print(k)

# testKangaroo()


def testPoints():
    a = [Point(1, 1), Point(1, 2), Point(2, 20), Point(1.5, -20)]
    mp = Points(a)
    mp.add(1, -1)
    print(mp)

    print(mp.left_most_point())
    print(len(mp))


testPoints()