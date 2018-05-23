#scopes and namespaces
"""
variable name and its binding to memory 
reference only exist in specific parts 
of the code - scopes
Where are these bindings stored??
namespaces
Each scope has its own namespace

Global Scope -> Module scope
It spans a single file 
Python does not have a scope across all modules
like a truly global scope

The only exception is that are some of the built in 
globally available objects such as 
True None False dict print

Global scopes are nested within the built in scope
Local scopes when we create functions we can create
variable names 

The global keyword - tells py to use variable 
in global namespace

when py encounters a function at compile time
    it will scan for labels(variables) that have values 
    assigned to them(anywhere in the function)
    if the label has not been specified as global then it 
    will be local

    Variables that are referenced but not assigned a value 
    anywhere in the function will not be local and python 
    at run time look for them in enclosing scopes

"""

a = 10
def func():
    global a
    print(a)
    a = 100

func()
print(a)

a = 10
def my_func():
    print("global a:", a)
    a = "hello"
    print(a)

my_func()