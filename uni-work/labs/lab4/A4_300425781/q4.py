#=== Exercise Four ===#
n = int(input('Enter a positive integer: '))

for i in range(n + 1):
    print('$' * i)

#=== Bonus Exercise ===#
m = int(input('Enter a positive integer: '))
sym = input('Enter a symbol: ')
spc = ' '

for i in range(m):
    print(spc * (m - i)  + (sym * i)  + sym + (sym * i) + spc * (m - i))