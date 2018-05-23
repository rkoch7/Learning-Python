def my_func(a:"mandatory positional",
            b:"optional positional" = 1,
            c=2,
            *args:" add some positional args",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "provide extra keyword args") -> "does nothin":
            """this function is being 
            used to demonstrate function introspection"""

            i = 20
            j = "hello"


print(my_func.__code__.co_name)

print(my_func.__code__.co_varnames)

print(my_func.__code__)
print(my_func.__doc__)
print(my_func.__annotations__)

#adding some attributes
my_func.short_descript = "short description"
print(dir(my_func))
print(my_func.__defaults__)
print(my_func.__kwdefaults__)


from inspect import isfunction, ismethod, isroutine
import inspect
class MyClass:
    def func(self):
        pass

print(isfunction(MyClass.func))

my_obj = MyClass()

print(isfunction(my_obj.func))

print(ismethod(my_obj.func))

print(inspect.getsource(my_func))




