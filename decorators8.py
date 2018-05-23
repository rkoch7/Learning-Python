
def timed1(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print(avg_elapsed)
        return result
    return inner

# see number of times you the run the function is hard
#coded never a good idea


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
            print("total time elaspsed {}".format(total_elapsed_time))
            return result
        return inner
    return decorator

@timed(10)
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(10))




