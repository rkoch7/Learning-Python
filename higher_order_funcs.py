print(help(map))

"""class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

"""

#map(func, *iterables) -> iterator object

#*iterables -> a varaiable number of iterable objects
#func -> some function that takes as many arguments as there
# are iterable objects passed to iterable

#map(func, *iterables) -> will return a iterator that calculates
#the function passed applied to each element of iterable

s = "hello"
iter = map(lambda k: k.upper(),s)
print(iter)
# for i in iter:
#     print(i)

s1 = "".join(iter)
print(s1)

l1 = [1,2,3]
l2 = [4,5,6]
var = zip(l1, l2)
print(var)
for v in var:
    print(v, type(v))

l1 = [1,2,3]
l2 = [10,20,30,40]
l3 = "python"

result = zip(l1, l2, l3)
result_list =list(result)
print(result_list)

#list of chars in string with its index
l1 = "abcdef"
l2 = range(100) #take greater than or equal to length of str
print(list(zip(l1, l2)))

#list comprehensions

l = range(10)
#return list of squares of elements of l less than 25

result = [x**2 for x in l if x**2 < 25]
print(result)


def fact(n):
    return 1 if n<2 else n * fact(n-1)

result = map(fact, range(5))
print("Memory address of result before using it {}".format(id(result)))
print(list(result))
print("Memory address of result after using it {}".format(id(result)))

print(list(result))




l1 = [1,2,3,4,5]
l2 = [10,20,30]
result_list = [x+y for x,y in zip(l1,l2)]
print(result_list)

l1 = [1,2,3,3,4]
l2 = [1,2,3]
l3 = "hello"

#map expects function which takes 
#same number of variables as numbes of 
#iterables passed, but this will 
#execute as it return a mapobject/generator
#will throw only when you execute against 
#the iterator returned
results = map(lambda x,y:x+y,l1,l2,l3)
#now it will throw
print(list(results))


l1 = [1, 2, 3, 3, 4]
l2 = [1, 2, 3]
l3 = "hello"


result = zip(l1,l2,l3)
print(hex(id(result)))
print(result is None)
print(list(result))
print(result is None)
print(list(result))

print(hex(id(result)))

#once a generator is exhausted its done baby

var = list(zip(range(10000), 'python'))
print(var)

#list comprehension
def fact(n):
    return 1 if n<2 else n * fact(n-1)

results = [fact(n) for n in range(5)]
print(results)

#generator expression
result_gen = (fact(n) for n in range(5))
print(result_gen)
for i in result_gen:
    print(i)
print(list(result_gen))
























