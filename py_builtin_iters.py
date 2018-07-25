r = range(10) #range is an iterable
print(type(r))

print('__iter__' in dir(r))
print('__next__' in dir(r))

z = zip([1, 2, 3], 'abc') #zip is iterator
print(z)
print('__iter__' in dir(z))
print('__next__' in dir(z))
print(list(z))
print(list(z)) #iterator exhausted

#iter() on iterator will return itself
with open('cars.csv') as f:
    print(iter(f) is f)

e = enumerate("python rocks")
print(iter(e) is e)
print(list(e))
print(list(e))
