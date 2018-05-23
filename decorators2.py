

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return inner

def mult(a, b, c=5):
    """testing decorators :)"""
    return a * b * c

mult = counter(mult)
print(mult.__name__)
print(mult.__closure__)
print(help(mult))

# so essentially you have lost all details
#signature and name etc of mult

from functools import wraps

def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return inner

@counter
def mult(a, b, c=5):
    """testing decorators :)"""
    return a * b * c

print(mult)
print(mult.__name__)
print(mult.__closure__)
help(mult)