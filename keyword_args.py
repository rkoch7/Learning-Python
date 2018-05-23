def func(a,b,c):
    print(a,b,c)


func(1,2,3)
func(1,c=10,b=2)
func(c=10,b=2,a=1)

def func1(a,b,*args,d):#d becomes a mandatory keyword arg
    print(a,b,args,d)

#func1(1,2,'c',3)
func1(1,2,'x','y',d=2)


#when you do not want to allow any positional arguments

def func(*,d):
    print(d)

#func(1,2,d=5) wrong cant do 

func(d=5)

def func(a,b,*,d):#I allow 2 postional arguments and no more
    pass
func(d=5)

#once you start using key word args 
#you cant revert back to using postional args

help(print)
print(1,2,3)

#issues with keyword args

from datetime import datetime

def log(msg, *, dt=None):
    if not dt:
        dt = datetime.utcnow()
    print("{}: {}".format(dt,msg))
log("aschdsif")
log("qkhdgqed",dt=2334)



help(int)
