def dec(fn):
    print("Runnning decorator")

    def inner(*args, **kwargs):
        print("Running inner")
        return fn(*args, **kwargs)
    return inner

@dec
def my_func():
    print("Running my_func")

my_func()

###############################################

def dec_factory():
    print("Running dec factory")

    def decorator(fn):
        print("Running decorator")
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            print("Running inner")
            return fn(*args, **kwargs)
        return inner
    return decorator

@dec_factory()
def my_func1():
    print("Running my_func")

my_func1()
################################################


def dec_factory(a, b):
    print("Running dec factory")

    def decorator(fn):
        print("Running decorator")
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            print("Running inner")
            print("a = {}, b = {}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return decorator


def my_func1():
    print("Running my_func")

# dec = dec_factory(1, 2)
# print(dec)
# my_func1 = dec(my_func1)
# my_func1()

my_func1 = dec_factory(1,2)(my_func1)
print(my_func1)

#############################################################

def timed(reps): #timed is a factory 

    def decorator(fn):
        from functools import wraps
        from time import perf_counter
        
        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed_time = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed_time += (perf_counter() - \
                                                    start)

            print("total time elaspsed {.6f}".\
                            format(total_elapsed_time))
            return result
        return inner
    return decorator

#################################################################