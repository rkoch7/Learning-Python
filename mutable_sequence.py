#assigning value through slice 
l = [1, 2, 3, 4, 5]
print(id(l))

l[0:3] = "python"
print(l, id(l))

l[2:5] = []
print(l, id(l))

#insertion
l[2:2] = "rosha"
print(l, id(l))