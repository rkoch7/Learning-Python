from itertools import count, cycle, repeat, islice

#count
g = count(10)
l = list(islice(g, 5))
print(l)
#range can only take integers
g = count(1, 0.5)
print(list(islice(g, 10)))

g = count((1+2j), (1+1j))
print(list(islice(g, 10)))

#cycle will work with both iterables and iterators
g = cycle(('red', 'green', 'blue'))
print(list(islice(g, 10)))

#lets try a iterator
def colors():
    yield 'red'
    yield 'green'
    yield 'blue'
c = colors()
g = cycle(c)
print(list(islice(g, 15)))

from collections import namedtuple

Card = namedtuple('Card', 'rank suit')
def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)

hands = [list() for _ in range(4)]
h_cycle = cycle(hands)
for card in card_deck():
    next(h_cycle).append(card)
print(hands)

#repeat
g = repeat('Python', 4) #return the same memory location
for x in g:
    print(x, hex(id(x)))
