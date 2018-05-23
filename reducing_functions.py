from functools import reduce

l = [5,8,6,10,9]
max_val = reduce(lambda a,b: a if a>b else b, l)
print(max_val)


min_val = reduce(lambda x,y: x if x<y else y, l)
print(min_val)

sum_list = reduce(lambda x,y: x+y,l)
print(sum_list)


l = [0, '', None, 100]

_any = reduce(lambda x,y: bool(x or y), l)
print(_any)


_all = reduce(lambda x,y: bool(x and y), l)
print(_all)

#calculate factorial 
#you can use reduce

n = 5
from functools import reduce
fact = reduce(lambda x,y: x*y, range(1, n+1))
print(fact)


l = []
from functools import reduce
#sum_list = reduce(lambda x,y: x+y, l)
sum_list = reduce(lambda x, y: x+y, l,0) #reduce initializer
print(sum_list)



