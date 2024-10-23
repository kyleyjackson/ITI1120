import random as rand

n = int(input("Enter a positive even integer for the size of the list? "))

# make list of zeros
a = []

for i in range(n):
    a.append(0)

# make list of random ints from 1 - 100
b = []

for i in range(n):
    b.append(rand.randint(1, 100))

# make list c alias of b
c = b

#make first 2 zero and print
for i in range(len(c) // 2):
    c[i] = 0

print('List b: ' + str(b))
print('List c: ' + str(c))

# copy b to d
d = []

for i in range(len(b)):
    d.append(b[i])

# list e has every other element of b
j = 1
e = []

while j < len(b):
    e.append(b[j])
    j += 2