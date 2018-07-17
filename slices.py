s  = slice(0, 2)
print(type(s))
print(s.start, s.stop)

#getting data from a flatfile

data = []
range_firstname = slice(0, 51)
range_lastname = slice(51, 101)
for row in data:
    first_name = row[range_firstname]
    last_name = row[range_lastname]
#this approach is better than hardcodin the slice values

l ="python"
print(l[::-1])
print(l[-1])

#using indices function of slice obj

t = slice(0, 100, 2).indices(14)
print(t)
print(list(range(*t)))

from dis import dis

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

dis(fact)