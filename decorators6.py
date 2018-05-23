def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("{}: called {}".format(run_dt, fn.__name__))
        return result
    return inner


def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print("{} ran for {:6f} seconds".format(fn.__name__,\
        end - start))
        return result
    return inner

@logged
@timed
def factorial(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1), 1)


print(factorial(9)) 


@logged
def func1():
    pass

@logged
def func2():
    pass

print(func1())

print(func2())


###################################


def dec_1(fn):
    from functools import wraps

    @wraps(fn)
    def inner():
        print("Running dec 1")
        return fn()
    return inner

def dec_2(fn):
    from functools import wraps

    @wraps(fn)
    def inner():
        print("Runnning dec 2")
        return fn()
    return inner

@dec_1
@dec_2
def my_func():
    print("Running my func")

print(my_func())