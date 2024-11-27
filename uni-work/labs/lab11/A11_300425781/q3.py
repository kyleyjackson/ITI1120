def is_palindrome(s):
    '''
    (string) => Boolean
    
    Returns True if s is a palindrome, False otherwise
    '''

    s = s.lower()

    if len(s) == 1 or len(s) == 0:
        return True
    
    if s[0] != s[len(s) - 1]:
        return False
    
    else:
        return is_palindrome(s[1 : len(s) - 1])

print(is_palindrome('taco cat')) # False
print(is_palindrome('tacocat')) # True