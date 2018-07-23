
squares = [i**2 for i in range(1, 101) if i%2]
print(squares)

import dis

compiled_code = compile('[i**2 for i in range(6)]', 
                        filename='string', mode='eval')

dis.dis(compiled_code)

table2 = [[i+j for i in range(1, 11)] for j in range(1, 11)]
print(table2)


#pascals
from math import factorial
def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))
size = 10
pascal = [[combo(row, col) for col in range(row+1)]for row in range(size+1)]
print(pascal)

#Nested Loops

l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

result = [s1 + s2 for s1 in l1 for s2 in l2]
print(result)

#dot product of 2 vector spaces

v1 = [1, 2, 3, 4, 5]
v2 = [10, 20, 30, 40, 50]
list(zip(v1, v2))

result = sum(i*j for i, j in zip(v1, v2)) #qctually gen expr
print(result)

#Caveats
funcs = [lambda x: x**i for i in range(5)]
print(funcs[0](10)) #i captured

funcs = [lambda x, p=i:x**p for i in range(5)] 
#default variables are evaluated at compile time
print(funcs[0](10))
print(funcs[1](10))