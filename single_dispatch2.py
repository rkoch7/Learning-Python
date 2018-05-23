from html import escape

def single_dispatch(fn):
    registry= {}
    registry[object] = fn
    print(registry)

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    def dispatch_method(type_):
        registry.get(type_, registry[object])

    decorated.register = register
    decorated.dispatch_method = dispatch_method
    decorated.registry = registry
    
    return decorated


@single_dispatch
def htmlize(arg):
    return escape(str(arg))


print(htmlize("1 > 10"))
print(htmlize.dispatch_method)
print(htmlize.registry)
print(htmlize.register)

@htmlize.register(int)
def html_int(arg):
     return '{0}(<i>{1}</i)'.format(arg, str(hex(arg)))


@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')


print(htmlize(25))
print(htmlize.dispatch_method)
print(htmlize.registry)
print(htmlize.register)




print(htmlize("discusfducbashbd sdihbcasbd"))
print(htmlize.dispatch_method)
print(htmlize.registry)
print(htmlize.register)
