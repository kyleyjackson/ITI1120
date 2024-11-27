def is_palindrome_v2(s):
    '''
    (string) => Boolean
    
    Returns True if s is a palindrome, False otherwise
    '''

    s = s.lower().strip()
    s1 = ''

    for char in s:
        if char.isalpha():
            s1 = s1 + char

    if len(s1) == 1 or len(s1) == 0:
        return True
    
    if s1[0] != s1[len(s1) - 1]:
        return False
    
    else:
        return is_palindrome_v2(s1[1 : len(s1) - 1])

print(is_palindrome_v2('taco cat')) # True
print(is_palindrome_v2('tacocat')) # True
print(is_palindrome_v2('i\'m mi')) # True
print(is_palindrome_v2('Madam, I\'m Adam')) # True
