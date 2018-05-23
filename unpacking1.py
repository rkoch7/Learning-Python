l = (1,2,3,4,5)
a = l[0]
b = l[1:]
print(type(a))
print(type(b))

l = (1,2,3,4,5,6)
a, *b = l
print(a)
print(b)


l = [1, 2, 3, 4, 5, 6]
a, *b = l
print(a)
print(b)

l = [1]
a, *b = l
print(a)
print(b)

l = "xyzf"
a, *b = l
print(a,type(a))
print(b,type(b))
