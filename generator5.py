files = 'car-brands-1.txt','car-brands-2.txt','car-brands-3.txt'

def brands(*files):
    for f_name in files:
        with open(f_name) as f:
            for line in f:
                yield line.strip('\n')

# for brand in brands(*files):
#     print(brand)

def brand1(*files):
    for f_name in files:
        yield from gen_cleaned_data(f_name)


def gen_cleaned_data(file):
    with open(file) as f:
        for row in f:
            yield row.strip('\n')

print(list(brand1(*files)))