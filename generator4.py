g = (i ** 2 for i in range(11))
print(g)
for i in g:
    print(i)
print(list(g)) #iterator exhausted

import dis
exp = compile('[i ** 2 for i in range(6)]',
             filename='<string>', mode='eval')
dis.dis(exp)

import dis
exp = compile('(i ** 2 for i in range(6))',
             filename='<string>', mode='eval')
dis.dis(exp)

#pascals tri

from math import factorial

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10 #global
pascal = [[combo(row, col) for col in range(row+1)] 
            for row in range(size+1)]
print(pascal)

size = 10 #global
pascal = [[combo(row, col) for col in range(row+1)] 
            for row in range(size+1)]

size = 10
pascal = ((combo(row, col)for col in range(row+1))for row in range(size+1))
print([list(row) for row in pascal])