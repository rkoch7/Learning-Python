import os.path
import types
import sys

#lets load modules_test.py manually

module_name = 'module_1' #typically module name is filename
module_file = 'modules_test_source.py'
module_path = '.'

module_rel_filepath = os.path.join(module_path, module_file)
module_abs_filepath = os.path.abspath(module_rel_filepath)

#read source from file
with open(module_rel_filepath, 'r') as code_file:
    source_code = code_file.read()

#create a module
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_filepath

#set a reference in sys modules
sys.modules[module_name] = mod

#compile the source the code
code = compile(source_code, filename=module_abs_filepath, mode='exec')

#execute the compiled source
exec(code, mod.__dict__)

#call it
#mod.hello()

#or 
import module_1
module_1.hello()


