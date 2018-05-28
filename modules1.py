import math
import fractions
from types import ModuleType

my_module = ModuleType('my_super_module', "this is an awesome module")
print(my_module)
print(my_module.__dict__)
my_module.hello = lambda:"hello"
my_module.pi = 3.142
print(my_module.__dict__)


print(type(fractions), type(ModuleType('math')))
print(math, math.__name__)
print(math.__dict__)

sqrt_func = math.__dict__['sqrt']
print(sqrt_func(2))

print(isinstance(fractions, ModuleType))




