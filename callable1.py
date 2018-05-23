print(callable(str))
print(callable(lambda))

result = print("hello")
print(result)

l = [1, 2, 3]
print(callable(l.append))

s = "xyx"
print(s.upper())
print(s)
result = callable(s.upper())
print(result)

from decimal import Decimal
result = callable(Decimal)
print(result)

a = Decimal('10.5')
print(a)
#is decimal class callable
print(callable(Decimal))
print(type(a))

#is a -> Decimal object callable

print(callable(a))

class MyClass:
    def __init__(self, x=10):
        print("initializing...")
        self.counter = x
    def __call__(self, x=1):
        print("updating counter...")
        self.counter += x

print(callable(MyClass))

a = MyClass(100)
print(a.counter)

print(callable(a))
a(5)
print(a.counter)



