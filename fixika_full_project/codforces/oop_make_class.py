from point import Point
from point import Point3d

point1 = Point(1, 33)
point2 = Point(4, -9)

# print(point1.x, point1.y)
# print(point2.x, point2.y)
#
#
# print(point1.distance(point2))
# print(point2.distance(point1))
#
# print(point1)
# print(type(point1))
# print(type(point2))
#

point3d_1 = Point3d(2, 4, 9)
point3d_2 = Point3d(5, 8, 90)

print(point3d_1.distance(point3d_2))
print(point3d_1.distance_3d(point3d_2))
print(point3d_1)

print(point3d_1.hello())