#slicing general iterables including iterators
#most tools in itertools module return a lazy iterator

from itertools import islice

l = [1,2,3,4,5,6,7]
result = islice(l, 0,len(l), 2)
print(list(result))
print(list(result))

import math

def factorial(n):
    for i in range(n):
        yield math.factorial(i)

def slice_(iterable, start, stop):
    for _ in range(0, start):
        next(iterable)
    for _ in range(start, stop):
        yield next(iterable)

f = factorial(25)

result = list(slice_(f, 5, 20))
print(result, len(result))

result2 = list(islice(factorial(10),2, 7))
print(result2)

import math
from itertools import islice
#islice is lazy iterator
def factorial1():
    index = 0
    while True:
        print(f'yielding factorial({index})...')
        yield math.factorial(index)
        index += 1

facts  = factorial1()
for _ in range(5):
    print(next(facts))

slice_iter = islice(factorial1(), 3, 19)
print(slice_iter)
l = list(slice_iter)#only when list was called slice_iter was evaluated
print(l)