#Named tuples - DocStrs and Default Values

from functools import namedtuple

Point2D = namedtuple('Point2D', 'x y')
pt1 = Point2D(6, 7)
print(Point2D.__doc__
    ,Point2D.x.__doc__
    ,Point2D.y.__doc__)


Point2D.__doc__ = 'Represent a 2D Cartesian coordinate'
Point2D.x.__doc__ = 'x coordinate'
Point2D.y.__doc__ = 'y coordinate'
print(help(Point2D))


Vector2D = namedtuple('Vector2D', 'x1, y1, x2, y2, origin_x, origin_y')
#prototype
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
#To create further vector2d instances you use vector_zero
v1 = vector_zero._replace(x1=10, y1=10, x2=10) #You hhave to use keyword args for replace

print(v1)

#You do the above using __defaults__ also

def func(a, b=10, c=20):
    pass

print(func.__defaults__)

Vector2D = namedtuple('Vector2D', 'x1, y1, x2, y2, origin_x, origin_y')
Vector2D.__new__.__defaults__ = (0, 0)
#x1 y1 x2 y2 origin_x origin_y
#               0       0       right aligned what you set to defaults

v1 = Vector2D(10, 20, 30, 40)
print(v1)

#defaults method is cleaner than using the prototype



