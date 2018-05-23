l = [1,2,3,4,5]
a = l[0]
b = l[1:]
print(a)
print(b)

a, *b = l
print(a)
print(b)

#slicing will work for ordered structs 
#unpacking works for any iterable

s = "python"
a, *b = s
print(a)
print(b) #b will be a list irrespective of the iterable

a,b,*c = "python"
print(a)
print(b)
print(c)

a, b, *c, d = "on"
print(a)
print(b)
print(c)
print(d)

l1 = [1,2,3]
l2 = [3,5,6]
l = {*l1,*l2}
print(l)

s = {1,3,'c',7}
*c, = s #handy way of unpacking something to a list
print(c,type(c))


s1 = {1,2,'l'}
s2 = {4,5,'v'}
l = [*s1,*s2]
print(l)

help(set)





