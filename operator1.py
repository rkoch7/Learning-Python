import operator

result = operator.concat("hello ", "world")
print(result)

#itemgetter function returns a callable
# operator.getitem() same as a[b]

# s = "roshan"
# f = operator.itemgetter(6)
# print("f for u",f)
# result = f(s)
# print(result)


l = [1,2,3,4,5,6]
f = operator.itemgetter(1,3,5)
result = f(l)
print(result, type(result))


#attribute getter - similar to itemgetter 
#but return the objects attributes

class MyClass:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def test(self):
        self.a += 1
        self.b += 1
        self.c += 1
    
my_obj = MyClass(1,2,3)
import operator

f = operator.attrgetter("test")
print(f)
print(f(my_obj)())

print(my_obj.a, my_obj.b, my_obj.c)


#calling another callable

import operator
s = "python"
f = operator.attrgetter("upper")
print(f, type(f))
print(f(s),type(f(s)))
print(f(s)())



################################333

import operator
from functools import reduce
result = reduce(lambda x,y: x*y, [1,2,3,4,5],1)
print(result)

result = reduce(operator.mul, [1,2,3,4,5])
print(result)

a = 1
b = 1
print(a is b)


class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def test(self, key):
        self.a += 1
        self.b += 1
        self.c += 1
        print("test instance method", key)
    

import operator
myobj = MyClass(10,20,30)
test_attr = operator.attrgetter("test")
print(test_attr)
print(test_attr(myobj))
print(test_attr(myobj)(15))



    









