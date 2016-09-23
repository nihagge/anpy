#Methods
class Circle(object):
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    @property
    def area(self):
        # radius ** 2 * pi
        return (self.radius ** 2) * Circle.pi
        self.result = (self.radius ** 2) * Circle.pi
       #  print self.result
c = Circle(radius=100)

print c.radius
print c.area