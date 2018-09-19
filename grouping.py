import itertools

with open('cars_2014.csv') as f:
    for row in itertools.islice(f, 0, 20):
        print(row, end='')

from collections import defaultdict
makes = defaultdict(int)
with open('cars_2014.csv') as f:
    next(f)
    for row in f:
        make, _ = row.strip('\n').split(',')
        makes[make] += 1
for key, value in makes.items():
    print(f'{key}: {value}')

from itertools import groupby
data = [1, 2, 2, 2, 3]
it = groupby(data)
for group_key, sub_iter in it:
    print(group_key, list(sub_iter))

from itertools import groupby
def gen_groups():
    for key in range(1, 4):
        for i in range(3):
            yield (key, i)
    yield 1,7

g = gen_groups()
groups = groupby(g, lambda x: x[0])

for group_key, sub_iter in groups:
    print(group_key, list(sub_iter))

"""
You must be careful to sort the data by the criteria before you call groupby or it won't work.
groupby method actually just iterates through a list and whenever the key changes it creates a new group.
"""
# group1 = next(groups)
# print(group1[0], list(group1[1]))
# print(list(g))
# group2 = next(groups)
# print(group2[0], list(group2[1]))
# group3 = next(groups)
# print(group3[0], list(group3[1]))
# print(list(g))
# print(list(g))

#lets use car data with group by model

from itertools import groupby, islice

with open('cars_2014.csv') as f:
    next(f)
    make_groups = groupby(f, key=lambda x: x.split(',')[0])
    make_counts = ((key, sum(1 for model in models))
                   for key, models in make_groups )
    print(list(make_counts))