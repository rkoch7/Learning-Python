def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

count1 = counter()
print(count1)
print(count1())


##################################

# some way to keep track of how many times a 
#function has been called

func_counters =dict()
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count 
        count += 1
        func_counters[fn.__name__] = count #you dnt need to 
        #use "global func_counter" its not an assignment
        #just assingning a value to an element of func_counter
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a + b

def mult(a, b):
    return a * b

add_count = counter(add)
mult_count = counter(mult)

add_count(4,6)
add_count(7,8)
mult_count(99,99)
print(func_counters)







