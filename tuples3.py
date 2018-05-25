#Modifying and extending - named tuples

from functools import namedtuple

Point2D = namedtuple('Point2D', 'x y')
pt1  = Point2D(2, 3)
print(hex(id(pt1)))

pt1 = Point2D(100, pt1.y)
print(hex(id(pt1)))

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_256, 26_393)
print(djia)

*values, close = djia
print(values, close)
values.append(close)

djia_1 = Stock(*values)
print(djia_1)

values = djia[:7]
djia = Stock(*values, 10000)
print(djia)

#use replace method
print(djia, hex(id(djia)))
djia = djia._replace(year=1983)
print(djia, hex(id(djia)))

print(Point2D, Point2D._fields, type(Point2D._fields))

Point3D = namedtuple('Point3D', Point2D._fields + ('z', ))
print(Point3D, Point3D._fields)