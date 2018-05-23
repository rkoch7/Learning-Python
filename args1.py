def my_func(a, b, *args):
    print(a,type(a))
    print(b,type(b))
    print(args,type(args))


my_func(1,2,'a',6,1,9,'r')

def my_func1(a,b,*args,d):
    pass

my_func1(1,2,3,4)


def my_func3(a,b,c):
    print(a,type(a))
    print(b, type(b))
    print(c, type(c))

l = [1,2,3,4]
my_func3(*l)



def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count

print(avg(1,2,3,3,3,3,3))
print(avg())




def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    #bool of a tuple returns its truth value
    avg = (hi + lo) / 2
    if log_to_console:
        print("high {} low {} avg = {}".format(hi, lo, avg))
    return avg

avg = calc_hi_lo_avg(1,2,3,4,5)
print(avg)

avg = calc_hi_lo_avg(1, 2, 3, 4, 5,log_to_console=True)
print(avg)







