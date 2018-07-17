import importlib
import sys

mod_name = 'math'
importlib.import_module(mod_name)
print(mod_name)
print(mod_name in sys.modules)

#print(math.sqrt(2))   importlib compiled-exec and put modules 
#sys.modules but you do not yet have an handle to it 
#check using globals

print('math' in globals())

#get a handle to math 
# math_1 = sys.modules['math'] or 

math_1 = importlib.import_module(mod_name)
print(math_1)
print(hex(id(math_1)))
print(hex(id(sys.modules['math'])))
print(math_1.sqrt(2))

#finders, loaders,
#finders + loader = importer
import fractions
print(fractions.__spec__) 

import sys
print(sys.meta_path) #what importers are available


