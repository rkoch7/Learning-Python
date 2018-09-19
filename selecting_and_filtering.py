def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i ** 3

is_odd = lambda x: x % 2 == 1
filtered = filter(is_odd, gen_cubes(10))
print(list(filtered))

from itertools import dropwhile, takewhile
from math import sin, pi
def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start) / (n -1)
    for _ in range(n):
        yield round(sin(start), 2)
        start += step
#print(list(sine_wave(20)))
result = takewhile(lambda x: 0 <= x <= 0.9, sine_wave(20))
print(list(result))
print(next(result))
