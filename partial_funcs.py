# reducing function arguments

from functools import partial 
def my_func(a, b, c):
    print(a, b, c)

f = partial(my_func, 10)
print(f(20,30))
print(type(f))

help(partial)

def pow(base, exponent):
    return base ** exponent
square = partial(pow, exponent=2)
print(square)
print(square(5))

cube = partial(pow, 3)
print(cube(3))

#issues - similar to args default



from functools import partial

def my_func(a,b,c):
    return (a, b, c)

f = partial(my_func,10)
result = f(20,30)
print(result)


from functools import partial

def my_func(a,b,*args,k1,k2, **kwargs):
    return(a,b,args,k1,k2,kwargs)

f = partial(my_func,10, 20, 30,40,50,k1=5,test="hello")
result = f(k2="python")
print(result)

from functools import partial

def pow(base,exponent):
    return base ** exponent

sq = partial(pow,2)
print(sq(10))
# i want to provide exponent in partial
# use named param

sq = partial(pow, exponent=2)
print(sq(16))

cube = partial(pow, exponent=3)
print(cube(9))

#variable refrence gets baked into the partial definition
from functools import partial
a = 2
def pow(base, exponent):
    return base ** exponent
sq = partial(pow, exponent=a)
print(sq(5))
a=3
#now you can expect 125 when you use sq(5)
# no sq is baked in to use a=2 reference
print(sq(5))

#but if its immutable datatype above scenario will work right

help(sorted)
from functools import partial
origin = (0,0)
l =[(1,1), (0,2),(-3,2), (-9,-5)]
dist2 = lambda x,y: (x[0]-y[0])**2 + (x[1]-y[1])**2
print(dist2((1,1),origin))
f = partial(dist2, origin)
result = sorted(l,key=f)
print(result)




