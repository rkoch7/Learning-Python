l = [1, 2, 3]
print(iter(l) is l)

class Squares:

    def __init__(self, n):
        self._n = n
    
    def __len__(self):
        return self._n
    
    def __getitem__(self,i):
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2

sq = Squares(10)
l =[sq[i] for i in range(10)]
print(l)
print(iter(sq))

class SequenceIterator:

    def __init__(self, sequence):
        self._sequence = sequence
        self._i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._i >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._i] ** 2
        self._i += 1
        return result

sq = Squares(15)
sq_iter =SequenceIterator(sq)
print(list(sq_iter))

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

a = "qsqwd"
print(is_iterable(a))
a = 100
print(is_iterable(a))
#second form
#iter(callable, sentinel)