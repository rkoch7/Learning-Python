from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from html import escape


@singledispatch
def htmlize(arg):
    return escape(str(arg))

print(htmlize.registry)

@htmlize.register(Integral)
def html_int(arg):
     return '{0}(<i>{1}</i)'.format(arg, str(hex(arg)))


print(htmlize.registry)

@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item)) 
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


# s = "python"
# htmlize(s)  this causes stackoverflow 
#when working with subclass types handle 
#most resolved type to avoid conflict   
#isinstance vs type -> isinstance can handle 
#subclasses