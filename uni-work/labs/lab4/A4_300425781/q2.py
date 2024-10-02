#=== Exercise Two ===#
def mess(str):
    '''
    (str) => str

    Takes a string as an input and the returns a copy of the string where each character 
    that is one of the last 8 consonants of the English alphabet is capitalized, and where each blank space is replaced with '-'
    '''

    # init stuff
    eightConsonants = ['z', 'y', 'x', 'w', 'v', 'r', 't', 's']
    str1 = ''

    # start changing string
    for i in range(len(str)):
        if str[i] in eightConsonants: # capitalize last 8 consonants 
            str1 += str[i].upper()

        elif str[i] == ' ': # replace space w/ dash
            str1 += '-'
        
        else: # nothing to be changed
            str1 += str[i]
        
    # print(str1)
    return str1

mess('Random access memory  ')
mess('central processing   unit.')