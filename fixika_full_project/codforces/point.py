class Point:
    def __init__(self, x, y):
        self.x= x
        self.y = y

    def distance(self, point):
        return((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

    def __str__(self):
        str_repr = 'Point.({0:.5f}, {1:.5f})'.format(self.x, self.y)
        return str_repr


    def hello(self):
        return "Hello! My cords are: ({0:.5f}, {1:.5f}, {2:.5f}) Nice To Mite you!"

class Point3d(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def distance_3d(self, point):
        return((self.x - point.x)**2 + (self.y - point.y)**2 + (self.z - point.z)**2)**0.5

    def __str__(self):
        str_repr = 'Point.({0:.5f}, {1:.5f}, {2:.5f})'.format(self.x, self.y, self.z)
        return str_repr



