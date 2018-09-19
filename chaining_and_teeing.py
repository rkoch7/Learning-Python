l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

# for gen in l1, l2, l3:
#     for item in gen:
#         print(item)

def chain_iterables(*l):
    for iterable in l:
        yield from iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain_iterables(l1, l2, l3):
    print(item)

from itertools import chain

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

l = [l1, l2, l3]
for item in chain(*l):
    print(item)

def squares():
    print("yielding 1st item")
    yield (i**2 for i in range(4))
    print("yielding 2nd item")
    yield (i**2 for i in range(4, 8))
    print("yielding 3rd item")
    yield (i**2 for i in range(8, 12))

# for item in chain(*squares()):
#     print(item)

#unpacking is always eager, if there is heavy lifting done between yields
print("using chain.from_iterable")
for item in chain.from_iterable(squares()):
    print(item)

from itertools import tee

def squares_(n):
    for i in range(n):
        yield i**2

gen = squares_(5)
iters = tee(gen, 3)
print(iters)