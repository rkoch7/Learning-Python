def fib(n):
    fib_0 = 1
    fib_1 = 1
    for _ in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

class FibIter:

    def __init__(self, n):
        self._n = n
        self._i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._i >= self._n:
            raise StopIteration
        result = fib(self._i)
        self._i += 1
        return result

fib_iter = FibIter(8)
print(list(fib_iter))


def fib1(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for _ in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

gen = fib1(7)
print(list(gen))