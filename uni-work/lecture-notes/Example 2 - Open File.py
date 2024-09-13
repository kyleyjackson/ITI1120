# Part 1: Boolean expressions, Function Design, Return, Program Execution
#IMPORTANT:We can use the IDLE console to do easy tasks in python.

# Example of Boolean expressions
x = 10
y = 20

# Boolean expressions compare values and result in True or False
# Show how comparisons work (<, >, ==, !=) and introduce Boolean logic (True/False).

print(x < y)   # Output: True
print(x == y)  # Output: False
print(x != y)  # Output: True

# Designing a simple function that returns a boolean result
# What is Docstring and how to write in different ways? --- Include the funtions header's (arguments types) in the docstring
def is_even(number):
    """
    This function checks if a number is even.
    If even, it returns True; otherwise, False.
    """
    return number % 2 == 0  # Return True if number is even
    #The difference between return function vs. void function.

# Calling the function with different arguments .. What's the difference?
# Explain how Python executes a function when it is called, jumping to its definition and then returning to the call.
print(is_even(10))  # Output: True
print(is_even(3))   # Output: False

# Function design: return and program execution
def add(a, b):
    """
    This function takes two numbers and returns their sum.
    """
    return a + b

# Program execution: When a function is called, the program jumps to its definition.
result = add(5, 7)
print(result)  # Output: 12

########################################################################

# Part 2: Functions that return value vs. functions that don't, Strings, Input Function, Print Function, Type Conversion, More Boolean Expressions

# Function that returns a value (as we saw earlier with `add`)
def multiply(a, b):
    """
    This function returns the product of two numbers.
    """
    return a * b

# Function that does NOT return a value but prints something instead
def greet(name):
    """
    This function prints a greeting message.
    """
    print("Hello, " + name + "!")

# Function calls
product = multiply(6, 7)  # This will store the return value
print(product)            # Output: 42

greet("Alice")            # This just prints, no return value is stored
# Output: Hello, Alice!

# Input function: Getting user input as a string
user_input = input("Enter a number: ")
print("You entered:", user_input)

# Type conversion: Converting a string to an integer
user_number = int(user_input)  # Convert string input to integer
print("Twice your number is:", user_number * 2)

# More Boolean expressions
# Combining multiple boolean expressions using "and", "or", "not"
age = 25
income = 50000

# Boolean expressions with logical operators
print(age > 18 and income > 30000)  # True, because both conditions are true
print(age < 18 or income > 30000)   # True, because one condition is true
print(not(age < 30))                # False, because age is less than 30

# String manipulation
name = "Python"
print(len(name))        # Output: 6 (length of the string)
print(name.upper())     # Output: "PYTHON" (uppercase conversion)
print(name.lower())     # Output: "python" (lowercase conversion)
print(name[0])          # Output: 'P' (access first character)

# Checking if a character or substring is in a string
print('y' in name)      # Output: True (checks if 'y' is in "Python")
print('z' in name)      # Output: False

# String concatenation
greeting = "Hello, " + name + "!" # I can print them in different ways!
print(greeting)         # Output: "Hello, Python!"

# Combining input and output with string formatting
user_name = input("What is your name? ")
print(f"Nice to meet you, {user_name}!")  # Using f-string for formatted output
