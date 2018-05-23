from functools import wraps

def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function with name {} at {}\
        was called {} times".format(fn.__name__,hex(id(fn)),count))
        return fn(*args, **kwargs)
    return inner

@counter
def my_func(s:str, i:int=1)->str:
    """return string multiply"""
    return s * i


help(my_func)

print(my_func("hhh",i=8))

