def outer_func():
    x = "hello"
    def inner_func():
        nonlocal x
        x += " world!"
    inner_func()
    print(x)

outer_func()


def outer_func():
    x = 'hello'
    def inner1():
        print("in inner")
        x = "python"
    inner1()
    print(x)

outer_func()


def outer():
    x = "hello"
    def inner1():
        def inner2():
            nonlocal x
            x += " world!"
        inner2()
    inner1()
    print(x)

outer()












