# Name: Kyle Yang Jackson
# Student Number: 300425781
# Course: ITI1120
# Assignment One
# Year: 2024

# imports
import turtle
import math

####################
# Question One
####################
def mh2kh(s):
    '''
    (number) => number
    
    Returns the input speed in km/h
    '''

    # print(1.609344 * s)  # for vscode testing
    return 1.60934 * s

# mh2kh(10)

####################
# Question Two
####################
def pythagorean_pair(a, b):
    '''
    (number, number) => Boolean

    Returns True if numbers a and b form a pythagorean pair, returns false otherwise
    '''

    c = math.sqrt((a ** 2 + b ** 2)) # pythagorean theorem

    # print(round(c, 0) == c) # vscode testing
    return round(c, 0) == c # compare & return

# pythagorean_pair(-300, 400)
# pythagorean_pair(2, 2)

####################
# Question Three
####################
def in_out(xs, ys, side):
    '''
    (number, number, number) => Boolean

    Returns True if the query point is inside of the boundaries of the specified square
    Precondition: side must be non-negative
    '''
    
    xInput = input("Enter the x coordinate of the query point: ")
    xc = float(xInput) # str => float

    yInput = input("Enter the y coordinate of the query point: ")
    yc = float(yInput) # str => float

    # print((xc >= xs and xc <= xs + side) and (yc >= ys and yc <= ys + side))  # for vscode testing
    return ((xc >= xs and xc <= xs + side) and (yc >= ys and yc <= ys + side)) # compare and return

# in_out(0, 0, 2.5)

####################
# Question Four
####################
def safe(n):
    '''
    (number) => Boolean

    Returns False if the number n does not contain 9 and cannot be divided by 9, otherwise returns True
    Precondition: n must be non-negative
    '''

    nStr = str(n) # convert to str for substring check

    # print(not('9' in nStr or n % 9 == 0)) # for vscode testing
    return ('9' in nStr or n % 9 == 0) # substring check

# safe(81)
# safe(97)
# safe(1000)

####################
# Question Five
####################
def quote_maker(quote, name, year):
    '''
    (string, string, number) => string

    Returns a formatted quote after given the quote, author, and year
    '''

    year = str(year) # int => str

    # print('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"')
    return ('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"') # create quote

# quote_maker('hello', 'someone', 2000)

####################
# Question Six
####################
def quote_displayer():
    '''
    () => string

    Returns a formatted quote after the user inputs the quote, author, and year
    '''

    # inputs
    quote = input('Enter the quote: ')
    name = input('Enter the name of the author of your quote: ')
    year = input('Enter the year the quote was created: ')

    # print('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"')
    return ('In ' + year + ', a person called ' + name + ' said: \"' + quote + '\"') # form quote

# quote_displayer()

####################
# Question Seven
####################
def rps_winner():
    '''
    () => None

    Prints the result of p1 in a rock paper scissors game between p1 and p2 after given inputs
    '''

    # inputs
    p1 = input('Player 1\'s move (rock, paper, scissors): ')
    p2 = input('Player 2\'s move (rock, paper, scissors): ')

    # print p1 victory and tie statements
    print('Player 1 wins, this is ' + str(((p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'))))
    print('Player 1 and Player 2 tied, this is ' + str(p1 == p2))
    
# rps_winner()
        
####################
# Question Eight
####################
def fun(x):
    '''
    (number) => number

    Returns the answer y for the expression 10^(4y) = x + 3 
    '''

    y = (math.log(x + 3)) / (4 * math.log(10)) # math.log() acts as ln unless base is specified

    # print(y) # vscode testing
    return y

# fun(20)

####################
# Question Nine
####################
def ascii_name_plaque(name):
    '''
    (string) => none

    Prints an ascii plaque with the inputted name in the middle
    '''

    nLen = len(name) #length of inputted name
    b = '*' # border
    s = ' ' # empty spaces

    #printing the plaque
    print(b * (nLen + 10))
    print(b + s * (nLen + 8) + b)
    print(b + '  __' + name + '__  ' + b)
    print(b + s * (nLen + 8) + b)
    print(b * (nLen + 10))

# ascii_name_plaque('kyle j')

####################
# Question Ten
####################
def draw_court():
    '''
    () => none

    Draws a basketball court using turtle graphics
    '''
    # screen and cursor
    t = turtle.Turtle()
    s = turtle.Screen()

    # setting colors
    s.bgcolor('#F4D48D')
    t.pencolor('white')
    t.pensize(3)
    t.hideturtle()
    t.speed(10)

    # center circle
    t.penup()
    t.fillcolor('#E48B50')
    t.goto(0, -50)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.penup()
    t.end_fill()

    # half court line
    t.goto(0, -175)
    t.left(90)
    t.pendown()
    t.forward(350)
    t.penup()

    # left key
    t.goto(-350, 45)
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.forward(125)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(125)
    t.end_fill()
    t.penup()

    # right outer key
    t.goto(350, -55)
    t.pendown()
    t.forward(125)
    t.right(90)
    t.forward(110)
    t.right(90)
    t.forward(125)
    t.penup()

    # right key
    t.goto(350, -45)
    t.right(180)
    t.pendown()
    t.begin_fill() 
    t.forward(125)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(125)
    t.end_fill()
    t.penup()
    
    # left outer-key
    t.goto(-350, 55)
    t.pendown()
    t.forward(125)
    t.right(90)
    t.forward(110)
    t.right(90)
    t.forward(125)
    t.penup()

    # out of bounds lines
    t.goto(-350, 175)
    t.right(180)
    t.pendown()
    t.forward(700)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(700)
    t.right(90)
    t.forward(350)
    t.penup()

    # left 3-point line
    t.goto(-350, -135)
    t.right(90)
    t.pendown()
    t.forward(45)
    t.circle(135, 180)
    t.forward(45)
    t.penup()

    # right 3-point line
    t.goto(350, 135)
    t.pendown()
    t.forward(45)
    t.circle(135, 180)
    t.forward(45)
    t.penup()

    # left key circle solid half
    t.goto(-225, -55)
    t.pendown()
    t.circle(55, 180)

    # left key circle dotted half
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)

    # right key circle dotted half
    t.goto(220, -55)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)
    t.pendown()
    t.circle(55, 12.5)
    t.penup()
    t.circle(55, 12.5)

    # right key circle solid half
    t.pendown()
    t.circle(55, 190)
    t.penup()

    # left back board
    t.goto(-330, -25)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.penup()

    # left rim
    t.goto(-330, 0)
    t.right(90)
    t.pendown()
    t.forward(10)
    t.right(90)
    t.color('#FFFFFF')
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()

    # right back board
    t.goto(330, 25)
    t.pendown()
    t.forward(50)
    t.penup()

    # right rim
    t.goto(330, 0)
    t.right(90)
    t.pendown()
    t.forward(10)
    t.right(90)
    t.color('#FFFFFF')
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()

    # exit on click
    s.exitonclick()

# draw_court()

####################
# Question Eleven
####################
def alogical(n):
    '''
    (number) => number

    Returns the number of times n / 2 must happen until n <= 1 is True
    Precondition: n >= 1
    '''
    
    # round up since we can have decimal
    # print(math.ceil(math.log(n, 2)))
    return math.ceil(math.log(n, 2)) # math.ceil rounds up

# alogical(4200231)

####################
# Question Twelve
####################
def cad_cashier(price, payment):
    '''
    (number, number) => number

    Returns the exact change in CAD when given price and payment
    Preconditions: price and payment are non-negative, payment >= price, last decimal in price is either 0 or 5, both numbers are inputted with 2 decimal places
    '''

    # print(round((payment - price) / 0.05) * 0.05)
    return round((payment - price) / 0.05) * 0.05 # convert to nearest nickel

# cad_cashier(19.99, 100.00)

####################
# Question Thirteen
####################
def min_CAD_coins(price, payment):
    '''
    (number, number) => tuple

    Returns a tuple of the minimum amount of coins needed to provide accurate change in the format: (toonies, loonies, quarters, dimes, nickels)
    Preconditions: same as cad_cashier(price, payment)
        => price and payment are non-negative, payment >= price, last decimal in price is either 0 or 5, both numbers are inputted with 2 decimal places
    '''

    change = cad_cashier(price, payment) * 100 # convert change into cents, already rounded to nearest nickel

    # coin cent values
    toonieVal = 200
    loonieVal = 100
    quarterVal = 25
    dimeVal = 10
    nickelVal = 5

    # calculate number of coins needed in order, then subtract
    numToonies = math.floor((change / toonieVal)) # math.floor() used to round down 
    change = change - (toonieVal * numToonies)
    
    numLoonies = math.floor((change / loonieVal))
    change = change - (loonieVal * numLoonies)
    
    numQuarters = math.floor((change / quarterVal))
    change = change - (quarterVal * numQuarters)
    
    numDimes = math.floor((change / dimeVal))
    change = change - (dimeVal * numDimes)
    
    numNickels = math.floor((change / nickelVal))

    # print((numToonies, numLoonies, numQuarters, numDimes, numNickels))
    return (numToonies, numLoonies, numQuarters, numDimes, numNickels)
# min_CAD_coins(3, 20)
