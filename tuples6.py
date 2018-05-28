from collections import namedtuple

data_list = [
    {'key2': 1, 'key1': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys = {key for dict_ in data_list for key in dict_}
print(keys)

Struct = namedtuple('Struct', sorted(keys))
print(Struct._fields)

Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
print(Struct._fields)

s1 = Struct()
print(s1)

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))
print(tuple_list)
