# Introduction to variables and types
# Here, we assign different types of values to variables

#1. Quickly introduce Python and how it processes data (everything is an object with a type).
#2. Cover **integers**, **floats**, **strings**, and **lists**. ---- variable assignment and reassignment.
#3. Introduce basic arithmetic operators (`+`, `-`, `*`, `/`, `//`, `**`, `%`). -- operator precedence (BEDMAS).
#4. Comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`) and Boolean operators** (`and`, `or`, `not`).

a = 3           # integer (int)
b = 3.0         # float (floating-point number)
c = 'three'     # string (text)
d = [1, 2, 3]   # list (collection of values)

# Displaying the types of these variables
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>
print(type(d))  # Output: <class 'list'>

# Arithmetic operations and operator precedence (BEDMAS)
x = 2 + 3 * 5   # Multiplication happens first, then addition
print(x)        # Output: 17

y = (2 + 3) * 5 # Parentheses force addition to happen first
print(y)        # Output: 25

# Integer division (//) and modulus (%) operators
print(14 // 3)  # Output: 4 (quotient of 14 divided by 3)
print(14 % 3)   # Output: 2 (remainder of 14 divided by 3)

# Boolean expressions and comparison operators
# These evaluate to True or False
print(5 > 3)    # True, because 5 is greater than 3
print(5 == 5)   # True, because 5 is equal to 5
print(5 != 3)   # True, because 5 is not equal to 3

# Boolean operators (and, or, not)
print(5 > 3 and 2 < 4)  # True, because both conditions are true
print(5 > 3 or 2 > 4)   # True, because at least one condition is true
print(not (5 > 3))      # False, because not negates the result

# Lists and basic operations
# Lists can store multiple values of different types
my_list = [10, 20, 30]
print(my_list)            # Output: [10, 20, 30]

my_list.append(40)        # Adding an item to the list
print(my_list)            # Output: [10, 20, 30, 40]

my_list.remove(20)        # Removing an item from the list
print(my_list)            # Output: [10, 30, 40]

# Indexing lists (remember, index starts at 0)
print(my_list[0])         # Output: 10 (first element)
print(my_list[-1])        # Output: 40 (last element)

# Strings as sequences
s = "Hello"
print(s[0])    # Output: 'H' (first character)
print(s[-1])   # Output: 'o' (last character)

# Simple if-else statement
num = 10
if num > 5:
    print("Number is greater than 5")
else:
    print("Number is 5 or less")
# Output: Number is greater than 5

#1. Variables and Data Types**: Explain that variables can hold different types of data, and Python is dynamically typed (you don’t need to declare the type).
#2. Boolean Logic**: Show how Python uses `True` and `False` to make decisions.
#3. Lists**: Demonstrate how lists can store multiple items and are mutable (you can change them).
