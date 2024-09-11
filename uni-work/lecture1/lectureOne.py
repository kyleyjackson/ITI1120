y = 0
str = 'hello world'
str1 = 'h'
arr = [2, 3]
#*objects and classes
x = 3 #integer
#an integer object can have any numerical value

x = 3.0 #float
# a float is represented in memory using 64 bits
# only 2^64 real number values can be represented with a float, the rest are approximated

x = 'three' #string
#a string is a sequence of characters enclosed within quotations

x = [3, 3, 3] #list
#a list is a comma-separated sequence of ints, floats, strings, and more enclosed within square brackets

#*arithmetic operators
#python follows bedmas
#() - Parenthesis
#** exponentiation
#*, /, //, % multiplication, division, modulus
#+, - addition and subtraction


#*relational operators (notation, example, meaning)
#>, x > y, x is greater than y
#<, x < y, x is less than y
#>= x >= y, x is greater than or equal to y
#<=, x <= y, x is less than or equal to y


#*equality operators (notation, example, meaning)
#==, x == y, x is equal to y
#!=, x != y, x is not equal to y


#*boolean expressions
#booleans evaluate to either True or False
#boolean expressions often involve comparison operators (<, >, ==, !=, <=, >=)
#comparison operators are evaluated after arithmetic operators


#*logical operators
x and y #returns true if both expressions are true
x or y #returns true if either expression is true
not x #returns true if the expression is false


#*escape sequences
'\n' #new-line character
'\t' #tab character
'\'' #single quote character
'\"' #double quote character
'\\' #backslash character


#*string operators
x in y #returns true if x is a substring of y
x not in y #returns true if x is not a substring of y
x + y #concatenates x and y
x + y #concatenates y to itself x amount of times
str[y] #character at index y of str
len(str) #returns the length of str


#*string methods
str.capitalize() #returns a copy of str with the first letter capitalized
str.count(str1) #returns the number of occurances of str1 in str
str.find(str1) #returns the index of the first occurance of str1 in str
str.lower() #returns an all-lowercase copy of str
str.upper() #returns an all-uppercase copy of str
str.replace(str, str1) #returns copy of str with every str replaced with str1
str.split(y) #returns list of substrings of str, delimited by y
str.strip() #returns str without leading or trailing whitespace


#*indexing
#in strings and lists, each character/entry has a value starting from 0 and increasing by 1 per character/entry


#*negative indexing
#similar to indexing, but starts from the end of the string/last with a starting value of -1


#*list operators
y in x #returns true if y is an item in x
y not in x #returns true if y is not an item in x
x + arr #concatenates x and arr
y * x #concatenates x to itself y number of times
x[y] #item at index y of list x
len(x) #returns the number of items in x
min(x) #returns the minimum item in x
max(x) #returns the maximum item in x
sum(x) #returns the sum of all items in x


#*list methods