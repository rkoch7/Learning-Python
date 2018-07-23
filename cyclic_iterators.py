class CyclicIterator:
    
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result

iter_cycl = CyclicIterator("NSWE")
for _ in range(15):
    print(next(iter_cycl))

iter_cycl = CyclicIterator([10, 20, 36])
for _ in range(15):
    print(next(iter_cycl))

iter_cycl = CyclicIterator("NSWE")
n = 10
items = [str(i) + next(iter_cycl) for i in range(1, n+1)]
print(items)

#using zip
iter_cycl = CyclicIterator("NSWE")
items = [str(num) + direction 
        for num, direction in zip(range(1, n+1), iter_cycl)]
print(items)

#above code CycleIter implement for any iterable in general
class CyclicIterator1:

    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        finally:
            return item

iter_cycl = CyclicIterator1("NSWE")
for _ in range(15):
    print(next(iter_cycl))



