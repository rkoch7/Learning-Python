def my_func():
    yield 1
    yield 2
    yield 3

gen = my_func()
print(iter(gen) is gen)

print(type(gen), gen)
for i in gen:
    print(i)

import math
class FactIter:

    def __init__(self, n):
        self._n = n
        self._i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._i >= self._n:
            raise StopIteration
        result = math.factorial(self._i)
        self._i += 1
        return result 

fact_iter = FactIter(5)
print(list(fact_iter))
print(list(fact_iter))

def fact():
    i = 0 
    def inner():
        nonlocal i
        result = math.factorial(i)
        i += 1
        return result
    return inner

fact_iter = iter(fact(), math.factorial(13))
print(fact_iter)
print(list(fact_iter))
print(list(fact_iter))

#using yield statement
def my_func1():
    print('line 1')
    yield 'flying'
    print('line 2')
    yield 'Circus'

my_func = my_func1()
print(iter(my_func) is my_func)

my_func.__next__()
test = my_func.__next__()

print(my_func)
print(list(my_func))


import math
def fact1(n):
    for i in range(n):
        yield math.factorial(i)

print(fact1)
f = fact1(5)
print(list(f))
print(next(f))
