# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner

# fn = outer()
# print(fn.__code__.co_freevars)
# print(fn.__closure__)


# def outer():
#     x = "python"
#     def inner():
#         print("hellow")
#     return inner

# fn = outer()
# print(fn.__code__.co_freevars)
# print(fn.__closure__)




# adders - shared extended scopes

adders = []
for n in range(1,4):
    print(n, hex(id(n)))
    def func(x):
        print(n, hex(id(n)))
        return x + n
    adders.append(func)

for add in adders:
    print(add(5))
