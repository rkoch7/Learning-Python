import math

#lazy evaluation

class Circle:

    def __init__(self, r):
        self._radius = r
        self._area = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None
    
    @property
    def area(self):
        if self._area is None:
            print("Calculating area")
            self._area = math.pi * (self._radius ** 2)
        return self._area

c1 = Circle(3)
print(c1.area)
print(c1.area)
c1.radius = 5
print(c1.area)


class Factorial:

    def __iter__(self):
        return FactIter()
    

class FactIter:

    def __init__(self):
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.i += 1
        return math.factorial(self.i)

fact = Factorial()
print(fact, type(fact))
fact_iter = iter(fact)

for _ in range(16):
    print(next(fact_iter))