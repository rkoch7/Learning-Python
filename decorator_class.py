#class instances are callable if you implement the 
#__call__

#using the class as the decorator factory

class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, fn):
        from functools import wraps
        print("Class initiated")
        @wraps(fn)
        def inner(*args, **kwargs):
            print("Running inner")
            return fn(*args, **kwargs)
        return inner

obj = MyClass(1,2)
print(obj)
r = obj(lambda x : x + 1)
print(r)
print(r(5))

