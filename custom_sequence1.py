#### mutable sequence #####

class MyClass:

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'MyClass(name={self.name})'
    
    def __add__(self, other):
        return MyClass(self.name + other.name)
    
    #inplace add - mutate self
    def __iadd__(self, other):
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other
        
        return self
    
    def __mul__(self, n):
        return MyClass(self.name * n)
    
    def __imul__(self, n):
        self.name *= n
        return self
    
    def __rmul__(self, n):
        self.name *= n
        return self
    
    def __contains__(self, value):
        return value in self.name


c1 = MyClass("acda")
c2 = MyClass("acsadcdds")

print(id(c1), id(c2))
result = c1 + c2
print(id(result), result)

c1 = MyClass("acda")
c2 = MyClass("acsadcdds")
result = c1 * 3
print(id(result), result)