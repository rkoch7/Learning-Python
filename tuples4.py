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

Vector2D = namedtuple('Vector2D', 'x1, x2')

