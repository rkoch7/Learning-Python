maps = map(lambda x: x**2 , range(5))
print(maps)
print(iter(maps) is maps)
print(list(maps))

def add(t):
    return t[0] + t[1]

print(list(map(add, [(0, 0), [1, 1], range(2,4)])))

def add_(x, y):
    return x + y

g = (add_(*t) for t in [(0, 0), [1, 1], range(2,4)])
print(list(g))

from itertools import starmap
maps = starmap(add_,[(0, 0), [1, 1], range(2,4)])
print(list(maps))

from functools import reduce

print(reduce(lambda x,y: x*y, [1, 2, 3, 4]))

def sum_(iterable):
    it = iter(iterable)
    acc = next(it)
    yield acc
    for item in it:
        acc += item
        yield acc

for item in sum_([10, 20, 30]):
    print(item)

def running_reduce(fn, iterable, start=None):
    it = iter(iterable)
    if start is None:
        acc = next(it)
    else:
        acc = start
    yield acc
    for item in it:
        acc = fn(acc, item)
        yield acc

print(list(running_reduce(lambda x,y: x+y, [10, 20, 30, 40])))