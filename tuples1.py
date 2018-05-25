tup = 1, 2, 3
print(type(tup))

a = 1, 2, "a", "wkehd"
x, *_, y = a  #_ is convention when you dnt intend to use the 
#variable, though _ is perfectly valid variable name
print(x,y)


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,\
                                                    self.x, self.y)


pt = Point2D(2, 3)
print(pt)
print(hex(id(pt)))
pt.x = 100
print(pt)
print(hex(id(pt)))


a = Point2D(2, 4) , Point2D(89, 9)
print(a)

london  = 'London', 'UK', 90813848
new_york = 'New York', 'USA', 48256384656
beijing = 'Beijing', 'China', 3845283499
cities = [london, new_york, beijing]

total = sum(city[2] for city in cities)
print(total)

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072
symbol, *_, close  = record
print(symbol, close)


for city,country,population in cities:
    print(city, country, population)


###################################

from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <=  radius:
        is_in_circle = True
    else:
        is_in_circle = False
    
    return random_x, random_y, is_in_circle

num_attempts = 100
count_inside = 0

for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print("Pi approx is {} ". \
                    format((4*count_inside)/ num_attempts ))


                    