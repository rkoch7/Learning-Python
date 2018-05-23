print(type(lambda x: x**2))

def apply_func(x, fn):
    return fn(x)


print(apply_func(3, lambda x: x**2))

print(apply_func(2, lambda x: x + 5))

print(apply_func("abc", lambda x: x[1:] * 3))

help(sorted)


l = ['B','a','C','d']
print(sorted(l))

print(sorted(l, key=lambda s: s.upper()))

l = [3+3j,0,1-1j,3+0j,6j]
print(sorted(l,key=lambda x: x.real**2+x.imag**2))


import random
l = [1,2,3,4,5,6,7,8,9,10]
out = sorted(l, key=lambda x: random.random())
print(out)

print(dir(print))

args = print.__code__
print(args)

#TODO:Implement 


