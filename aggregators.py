def squares(n):
    for i in range(n):
        yield i ** 2

l = list(squares(5))
print(l)
sq = squares(5)
print(min(sq))
#print(max(sq)) returns an iterator which was exhausted in the
#min call, need to recreate gen expr every time
sq = squares(5)
print(max(sq))

#all values are numbers, they inherit from Numbers class

from numbers import Number
from decimal import Decimal

print(isinstance(10, Number))
print(isinstance(10.5, Number))
print(isinstance(10+4j, Number))
print(isinstance(Decimal('10.5'), Number))
print(isinstance('10.5', Number))

from numbers import Number
from decimal import Decimal
l = [10, 20, 30, 40, 50,None]
print(all(isinstance(i, Number) for i in l))

with open('car-brands.txt') as f:
    for row in f:
        print(len(row), row, end='')

#find if all car brands are greater than 3 chars
with open('car-brands.txt') as f:
    result = all(map(lambda row: len(row) >= 4, f))
print(result)