def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        
        args_ = [str(a) for a in args]
        kwargs_ = ["{} = {}".format(k,v) for (k,v) \
        in kwargs.items()]
        all_args = args_ + kwargs_
        all_args = ",".join(all_args)
        print("{} with args ({}) took {:6f}".format(fn.__name__,
                                                    all_args,
                                                    elapsed))
        return result
    return inner


@timed
def fibo_reduce(n):
    from functools import reduce
    initial = 1,0
    dummy = range(n)
    fib_n = reduce(lambda prev, i:(prev[0] + prev[1], prev[0]), dummy, initial)
    return fib_n


print(fibo_reduce(5))


@timed
def fibo_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2 , fib_1 + fib_2
    return fib_2

print(fibo_loop(87))

def nth_fibo_recur(n):
    if n <= 2:
        return 1
    else:
        return nth_fibo_recur(n-1) + nth_fibo_recur(n-2)

@timed
def nth_fibo_recur_wrapper(n):
    nth_fibo_recur(n)

