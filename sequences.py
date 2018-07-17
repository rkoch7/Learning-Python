s = "gnu's not unix"
enum = enumerate(s)
print(type(enum))
print(list(enum))

s.index('z')
s = "python"
l = [1,2,3,4,5,6,7,8,9,10]
print(s[1:4])
print(list(enumerate(s)))
print(s[::-1])


#slicing always return a new object
l = [1,2,3]
l1 = l[:]
print(l is l1)

##caveats
test = [[1,1],[1,2]]
new = test * 2
print(new, hex(id(test[0])), hex(id(new[0])))

from decimal import Decimal

a = Decimal('10.5')
b = Decimal('10.5')
print(a is b)

l = [Decimal('10.5')]
print(id(l[0]))

l1 = l * 2
print(l1)
print(hex(id(l[0])))
print(hex(id(l1[0])))

s = [1,2,3]
s.reverse()
print(s)

l = [1, 2, 3, 4, 5]
print(id(l), id(l[0:2]))
print(type(l[0:2]))

l[0:2] = 'a', 'b'
print(l)
l.extend("python")
print(l)


l = [[1,2], 'a', 'b']
l1 = l.copy() #use deep copy
l1[0].append(6)
print(l, l1)


