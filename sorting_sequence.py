import this

d = {'a':10, 'b':-9, 'c':2}
print(d, sorted(d))
print(sorted(d, key=lambda k: d[k]))


t = 'this', 'parrot', 'is', 'a', 'late', 'bird'
result = sorted(t, key=lambda s: len(s))
print(result)