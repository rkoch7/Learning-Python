#immutable type sequence

from functools import lru_cache

class Fib:

    def __init__(self, n):
        self.n = n
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            return Fib._fib(s)
        else:
            rng = range(*s.indices(self.n))
            return [Fib._fib(i) for i in rng]


    
    @staticmethod
    @lru_cache(2**10)
    def _fib(n):
        if n < 2:
            return 1
        return Fib._fib(n-1) + Fib._fib(n-2)
    
fib = Fib(10)
print(fib[0:4])
print(fib(-1:-4:-1))
print(list(fib))