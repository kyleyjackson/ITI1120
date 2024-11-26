import sys
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord = 0, ycoord = 0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+', '+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+', '+str(self.y)+')'

class Rectangle():

    # overloads
    def __init__(self, bl, tr, col):
        '''
        (Point, Point, str) => None
        
        Initializes a rectangle with bottom left point bl and top right point tr
        Precondition: The x and y coordinates of Point bl will always be <= those of tr
        '''

        self.botLeft = bl
        self.topRight = tr
        self.colour = col.lower().strip()
    
    def __str__(self):
        '''
        (Rectangle) => str
        Overloads print() for Rectangles to:

        "I am a self.colour rectangle with a bottom left corner at self.botLeft and a top right corner at self.topRight"
        '''

        return 'I am a ' + self.colour + ' rectangle with a bottom left corner at ' + str(self.botLeft.get()) + ' and a top right corner at ' + str(self.topRight.get())

    def __eq__(self, other):
        '''
        (Rectangle, Rectangle) => Boolean

        Returns True if self is the exact same Rectangle as other
        Returns False otherwise
        '''

        return self.botLeft == other.botLeft and self.topRight == other.topRight and self.colour == other.colour
    
    def __repr__(self):
        '''
        Canonical string representation: Rectangle(self.botLeft, self.topRight, self.colour)
        '''

        return 'Rectangle(' + str(self.botLeft) + ', ' + str(self.topRight) + ', ' + self.colour + ')'

    # methods
    def get_bottom_left(self):
        '''
        (Rectangle) => Point
        
        Returns the bottom left corner of the invoking Rectangle
        '''

        return self.botLeft

    def get_top_right(self):
        '''
        (Rectangle) => Point
        
        Returns the top right corner of the invoking Rectangle
        '''

        return self.topRight

    def get_colour(self):
        '''
        (Rectangle) => str
        
        Returns the colour of the invoking Rectangle
        '''

        return self.colour
    
    def reset_colour(self, col):
        '''
        (Rectangle, str) => None
        
        Changes the string representing the invoking Rectangle to col
        '''

        self.colour = col.lower().strip()
    
    def get_perimeter(self):
        '''
        (Rectangle) => int/float
        
        Returns the perimeter of the invoking Rectangle
        '''

        s1 = self.topRight.x - self.botLeft.x
        s2 = self.topRight.y - self.botLeft.y

        return (2 * s1) + (2 * s2)

    def get_area(self):
        '''
        (Rectangle) => int/float
        
        Returns the area of the invoking Rectangle
        '''

        s1 = self.topRight.x - self.botLeft.x
        s2 = self.topRight.y - self.botLeft.y

        return s1 * s2

    def move(self, x, y):
        '''
        (Rectangle, int/float, int/float) => None
        
        Moves the invoking Rectangle by x units right and y units up
        '''

        self.botLeft = Point(self.botLeft.x + x, self.botLeft.y + y)
        self.topRight = Point(self.topRight.x + x, self.topRight.y + y)
    
    def intersects(self, other):
        '''
        (Rectangle, Rectangle) => Boolean
        
        Returns True if the two Rectangles intersect
        Returns False otherwise
        '''

        return not(self.topRight.x < other.botLeft.x or self.botLeft.x > other.topRight.x or self.topRight.y < other.botLeft.y or self.botLeft.y > other.topRight.y)
        
    def contains(self, x, y):
        '''
        (Rectangle, Point) => Boolean
        
        Returns True if point is within the confines of the invoking Rectangle
        Returns False otherwise
        '''

        return (x <= self.topRight.x and self.botLeft.x <= x) and (y <= self.topRight.y and self.botLeft.y <= y)
    

class Canvas:

    # overloads
    def __init__(self):
        '''
        () => None

        Initializes empty Canvas object
        '''

        self.rects = []

    def __repr__(self):
        '''
        Canonical string representation: Canvas(self.rects)
        '''

        return 'Canvas(' + str(self.rects) + ')'

    def __len__(self):
        '''
        Overloads len() to return the length of self.rects
        '''
        
        return len(self.rects)

    # methods
    def add_one_rectangle(self, rect):
        '''
        (Canvas, Rectangle) => None
        
        Adds a Rectangle to the invoking Canvas
        '''

        self.rects.append(rect)
    
    def count_same_colour(self, col):
        '''
        (Canvas, str) => int
        
        Returns the number of Rectangles in the invoking Canvas that have the colour col
        '''

        col = col.lower().strip()
        count = 0

        for rect in self.rects:
            if rect.colour == col:
                count += 1
        
        return count

    def total_perimeter(self):
        '''
        (Canvas) => int/float
        
        Returns the sum of each Rectangle's perimeter for the invoking Canvas
        '''

        p = 0

        for rect in self.rects:
            p += rect.get_perimeter()
        
        return p

    def min_enclosing_rectangle(self):
        '''
        (Canvas) => Rectangle
        
        Returns the smallest Rectangle needed to envelop all Rectangles in the invoking Canvas
        '''

        # smallest/largest possible numbers
        maxX = -1 * sys.maxsize
        maxY = -1 * sys.maxsize
        minX = sys.maxsize
        minY = sys.maxsize

        for rect in self.rects:
            minX = min(minX, rect.botLeft.x)
            minY = min(minY, rect.botLeft.y)
            maxX = max(maxX, rect.topRight.x)
            maxY = max(maxY, rect.topRight.y)

        return Rectangle(Point(minX, minY), Point(maxX, maxY), 'red')

    def common_point(self):
        '''
        (Canvas) => Boolean
        
        Returns True if there exists a point that is contained by each Rectangle in the invoking Canvas
        Returns False otherwise
        '''

        for rect in self.rects:
            for other in self.rects:
                if not(rect.intersects(other)):
                    return False

        return True