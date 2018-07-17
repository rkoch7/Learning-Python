import sys

for key in sorted(sys.modules.keys()):
    print(key)

print('cmath' in sys.modules)
from cmath import exp
print('cmath' in globals()) #using from cmath import exp say , 
#you will have only a reference to exp in global namespace
print('exp' in globals()) 