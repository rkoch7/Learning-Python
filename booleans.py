help(bool)
print(issubclass(bool,int))
print(type(True),hex(id(True)),int(True))

print(type(False), hex(id(False)), int(False))

print(hex(id(3 > 4)))

print(None is False)


a = [1,2,3]
a = None
b = [4]
print(a and b)

a = (1,2)
b = (1,2)
var = a is b
print(var)

tup = ()
tup = [1, 2, 3]
print(type(tup))
