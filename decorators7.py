 #memoization


def fib(n):
     print("Calculating fib ({})".format(n))
     return 1 if n < 3 else fib(n-1) + fib(n-2)
    

class Fib:
    def __init__(self):
        self.cache = {1: 1,2: 1}
    
    def fib(self, n):
        if n not in self.cache:
            print("Calculating fib({})".format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-1)
        return self.cache[n]

f = Fib()
f.fib(7)


###########################################

def fib1():
    cache = {1: 1, 2: 1}
    def calc_fib(n):
        if n not in cache:
            print("Calculating fib ({})".format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

###########################################


def memoize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            print("Cache miss for {}...Calculating".\
                                        format(n))
            cache[n] = fn(n)
        return cache[n]
    return inner

@memoize
def fib_recur(n):
    return 1 if n < 3 else fib_recur(n-1) \
                                    + fib_recur(n - 2)

print(fib_recur(8))
##################################################
#you can use same memoize to cache agai for cache
def memoize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            print("Cache miss for {}...Calculating".\
                                        format(n))
            cache[n] = fn(n)
        return cache[n]
    return inner


@memoize
def factorial(n):
    from functools import reduce
    return reduce(lambda x,y: x * y, range(1, n+1))



print(factorial(5))
print(factorial(6))

##########################################################
#how do I limit the size of the cache

from functools import lru_cache

@lru_cache(maxsize=8)
def factorial(n):
    print("Calculating fact of {}".format(n))
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(8))
print(factorial(9))
print(factorial(1))