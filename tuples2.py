#named tuples

from collections import namedtuple

class Point3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "Class Name: {} (x = {}, y = {}, z = {}) "\
                                    .format(self.__class__.__name__
                                    ,self.x
                                    ,self.y
                                    ,self.z)

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.z == other.z and \
                    self.y == other.y and \
                    self.x == other.x
        else:
            return False

pt1 = Point3D(10, 20, 30)
pt2 = Point3D(40, 50, 60)

print(pt1, pt2)
print(pt1 == pt2)
#########################################################

from collections import namedtuple
Point2D = namedtuple('Point2D', 'x, y')
print(Point2D)

pt1 = Point2D(x=5, y=8)
print(isinstance(pt1, tuple))
print(pt1, type(pt1),pt1.x)

#get maximum among cordinates of a Point,
# because this is a tuple we can do this
print(max(pt1))
#########################################
#dot product 

from collections import namedtuple

Point2D = namedtuple('Point2D', 'x, y')
pt1 = Point2D(x=5, y=8)
pt2 = Point2D(x=6, y=9)

Vector3D = namedtuple('Vector3D', 'x y z')
vect1 = Vector3D(10, 20, 30)
vect2 = Vector3D(1, 2, 3)


def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))

print(dot_product(pt1, pt2))
print(dot_product(vect1, vect2))

#You can use the same dot product function 
#irrespective of the number of coordinates
#they are all performing tuple operations
#for the class implementations you might have to end 
#writing class specific func

#########################################
from functools import namedtuple
Circle = namedtuple('Circle', 'centre_x, centre_y radius')
print(Circle._fields)
print(Circle._source)
c1 = Circle(1, 2, 5)
print(c1._asdict())   #returns a ordered dict



