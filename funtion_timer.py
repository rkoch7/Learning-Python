import time

def time_it(fn, *args, rep=1,**kwargs):
    start_time = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end_time = time.perf_counter()
    return (end_time - start_time) / rep


print(time_it(print, 1,2,3, sep='|'))


def compute_power_1(n, *,start=1,end):
    result = []
    for i in range(start, end):
        result.append(n**i)
    return result

print(compute_power_1(2,end=5))

def compute_power_2(n, *, start=1,end):
    #using list comprehension
    return [n**i for i in range(start,end)]

print(compute_power_2(2,end=5))

def compute_power_3(n, *, start=1, end):
    #using generator expression
    return (n**i for i in range(start,end))

print(compute_power_3(2,end=9))
print(list(compute_power_3(2,end=9)))