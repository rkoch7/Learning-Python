#closures applications


class Averager:

    def __init__(self):
        self.numbers = []
    
    def add(self, n):
        self.numbers.append(n)
        return sum(self.numbers) / len(self.numbers)
    
a = Averager()
a.add(10)
a.add(15)
print(a.add(20))

#the same example above achieved with a closure 
# as shown below

def averager():
    numbers = []
    def inner(n):
        numbers.append(n)
        return sum(numbers) / len(numbers)
    return inner

fn = averager()

print(fn)
print(fn.__closure__)
print(type(fn))


############################
#why store the list just maintain total and count and return avg

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count 
        total += number
        count += 1
        return total / count
    return add


avg = averager()
print(avg)
print(avg.__closure__)
for n in range(1,7):
    print(avg(n))

###########################################





