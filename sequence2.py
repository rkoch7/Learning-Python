
l = [1,2,3]
cp = [e for e in l]
print(cp, id(l), id(cp))

l = [1,2,(1,2)]
l2 = l.copy()

t1 = (1, 2, 3)
t3 = t1[:]
t2 = t1[0:1]
print(id(t1), id(t2), id(t3))

v1 = [0 ,0]
v2 = [0, 0]
line1 = [v1, v2]
line2 = [v for v in line1]
print(id(line1[0]), id(line2[0]))
line2[0][1] = 5
print(line1, line2)

import dis 
def foo():
    l1 = [[1,2, [1,2,3]],[1,2]]
    l2 = [x.copy() for x in l1]
    print(id(l1[1]), id(l2[1]))
    l1[0][2][1] = "s"
    print(l1, l2)

foo()

dis.dis(foo)

v1 = [1,1]
v2 = [2,2]
v3 = [3,3]
v4 = [4,4]
l1 = [v1, v2]
l2 = [v3, v4]

plane1 = [l1, l2]
plane2 = [x.copy() for x in plane1]

print(id(plane1[0]),id(plane2[0]))

import copy 
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f"Line({self.p1.__repr__()}, {self.p2.__repr__()})"
    
p1 = Point(1, 2)
p2 = Point(10 , 12)

line1 = Line(p1, p2)
line2 = copy.deepcopy(line1)

print(line1.p1, id(line1.p1))
print(line1.p2, id(line1.p2))