def counter(fn):
    count  = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function with name {}  at address {} was called {} times "\
        .format(fn.__name__, hex(id(fn)), count))
        return fn(*args, **kwargs)
    return inner


def add(a:int, b:int=0):
    """
    adds two ints
    """
    return a + b

def mult(a:int, b:int, c:int=7):
    """mult 3 with one default """
    return a * b * c

@counter
def my_func(s:str, i:int) -> str:
    return s * i

print(hex(id(mult)))

mult = counter(mult)
print(mult.__closure__)
print(hex(id(mult)))

mult(1, 2)
mult(7, 2)
mult(9, 2)

# print(hex(id(mult)))

# out = counter(mult)
# print(out.__closure__)
# print(hex(id(out)))

# out(1,2)
# out(7, 2)
# out(9, 2)







