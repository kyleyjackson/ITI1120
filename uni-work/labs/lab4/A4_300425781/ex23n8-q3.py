#=== Exercise Three ===#
def is_divisible(n, m):
     '''
     (int, int) => Boolean

     Returns True if n is divisible by n, and False otherwise.
     '''
     return n % m == 0

def is_divisible23n8(n):
     '''
     (int) => Boolean

     Returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.
     '''

     if (is_divisible(n, 2) or is_divisible(n, 3)) and not(is_divisible(n, 8)):
          return True
     else:
          return False

def print_all_23n8(num):
     '''
     (int) => None
     
     Prints all the non-negative numbers smaller than num that are divisible by 2 or 3, but not 8
     
     Precondition: num is non-negative
     '''

     # array of nums 
     arr = []

     for i in range(num):
          if is_divisible23n8(i):
               arr.append(i)
     
     print(arr)

n = int(input('Enter a number: '))
print_all_23n8(n)
