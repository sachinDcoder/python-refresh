from collections import namedtuple

def exploreNamedtuple():
    Point = namedtuple('Point', 'x,y')
    pt = Point(1, -4)
    print(pt)
    print(type(pt))
    print(pt.x, pt.y)


exploreNamedtuple()

# Point(x=1, y=-4)
# <class '__main__.Point'>
# 1 -4
