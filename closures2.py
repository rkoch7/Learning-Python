#strings and ints get interned 

def outer():
    x = "python"
    print(hex(id(x)))
    def inner():
        print(x)
        print(hex(id(x)))
    return inner


fn = outer()
print(fn.__closure__)
fn()

############################################
def outer():
    x =[1,2,3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    return inner

fn = outer()
tup = fn.__closure__
for t in tup:
    print(t, type(t))
fn()

###################################3


def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

fn = outer()
print(fn.__closure__)
print(hex(id(0))) #0 is singleton object

print(fn())
print(fn.__closure__)
###########################################


def outer():
    #closures within same scope
    count = 0
    
    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2


fn1, fn2 = outer()
print(fn1.__closure__)
print(fn2.__closure__)
print(fn1())
print(fn1())
print(fn2())

################################################


def pow(n):
    def inner(x):
        return x ** n
    return inner


square = pow(2)
print(square)
print(hex(id(2)))
print(square.__closure__)
print("*"*5)
print(square(5))
cube = pow(3)
print(cube)
print(cube.__closure__)

#square and cube are different closures 
#each function call different scope generated

###############################################################3


#labels that get shared without you realizing

def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1.__closure__, add_2.__closure__,add_3.__closure__)

#as you can see different cell objects 
#different closures 

#but when you see lines 107 to 109 into a loop

adders =[]
for n in range(1, 4):
    adders.append(lambda x: x + n)

#n is shared between scopes you have created a closures
#not exactly since n is in global funcs
#lets wrap it into a func

def create_adder():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adder()

print(adders)

print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)

"""(<cell at 0x04F8A7D0: int object at 0x6964D750>,)
(<cell at 0x04F8A7D0: int object at 0x6964D750>,)
(<cell at 0x04F8A7D0: int object at 0x6964D750>,)"""

#all n point to same n

print(adders[0](10))
print(adders[1](10))
print(adders[2](10))


#Now how do you solve this
#same example as above, 

def create_adder():
    adders = []
    for n in range(1, 4):
        #no free variable no closure created
        #y default is evaluted when function is created
        adders.append(lambda x, y=n: x + y)
    return adders



adders = create_adder()
print(adders)
print(adders[0].__closure__)
print(adders[0].__code__.co_freevars)
###########################################################










    
