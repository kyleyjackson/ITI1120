def m(i):
    '''
    (int) => float
    
    Returns the result of the series: 1/3, 2/5, ..., i/(2i + 1)
    '''
    if i == 1:
        return (1/3)

    return (i / ((2 * i) + 1)) + m(i - 1)

# == MAIN == #
for i in range(1, 11):
    print(m(i))