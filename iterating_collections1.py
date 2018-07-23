class Squares:

    def __init__(self, length):
        self.i = 0
        self.length = length
    
    def __next__(self):
        print("__next__ was called")
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result
    
    def __iter__(self):
        print("__iter__ was called")
        return self

sq = Squares(10)
for item in sq:
    print(item)

sq = Squares(10)
sq_iterator = iter(sq)
print(id(sq), id(sq_iterator))

while True:
    try:
        item = next(sq_iterator)
        print(item)
    except StopIteration:
        break