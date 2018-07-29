def squares(n):
    for i in range(n):
        yield i ** 2

sq = squares(5)
print(sq)
print(list(sq))
print(list(sq))

class Squares:

    def __init__(self, n):
        self._n = n
    
    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2
    
    def __iter__(self):
        return Squares.squares_gen(self._n)


sq = Squares(5)
print(sq)
print(list(sq))
print(list(sq))

def squares1(n):
    for i in range(n):
        yield i ** 2

sq = squares1(5)
print(sq)
next(sq)
next(sq)
#now run enum 
print(list(enumerate(sq)))