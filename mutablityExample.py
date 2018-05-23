my_var = "hello"
def process(s):
    s = s + ' world'
    return s

process(my_var)
print(my_var)
# this shows mutable objects provide some level 
# of protection from unintended modification
# specially during function calls


a = 10
print(type(a))

b = int(10)
print(type(b))

help(str)




#int sizes 

import sys
print(sys.getsizeof(0))
num = 0
print(sys.getsizeof(num))
print(sys.getsizeof(1))
print(sys.getwindowsversion())
print(sys.getsizeof(2 ** 1000))

print(155 / 4)
print(155 // 4)
print(155 % 4)

a = int(True)
print(a)

import decimal
#a = int("10.9")
a = int(Decimal("10.9"))
print(a)

a = int("123.2")
print(a)

a = int("a12f", base=16)
print(a)






