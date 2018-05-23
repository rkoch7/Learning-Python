def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function {} was called {} times".\
        format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

print(add, type(add))
print(mult, type(mult))

add = counter(add)
mult = counter(mult)

print(add, type(add))
print(mult, type(mult))
###################################



def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        try:
            result = fn(*args, **kwargs)
            count += 1
            print("function {} called {} times ".format(fn.__name__, count))
            return result
        except e:
            print(e)
    return inner


@counter
def mult(a, b, c=1):
    return a * b * c

# mult = counter(mult)
print(mult(2, 7))

@counter
def add(a, b):
    return a + b

print(add(1, 3))
print(add(2, 3))
print(add(6, 3))
print(add(9, 3))
