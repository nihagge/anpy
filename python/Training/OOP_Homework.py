#Methods
# from __future__ import print_function

class Cylinder(object):
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height + self.radius

    def surface_area(self):
        return self.height * self.radius

Cy = Cylinder()
print Cy.volume()
print Cy.surface_area()



class Lines(object):
    def __init__(self,coor1, coor2):
        # type: (object, object) -> object
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return x1 * y2

coordinate1 = (2,3)
coordinate2 = (3,6)

Li = Lines(coordinate1,coordinate2)

print Li.distance()




#Methods
#class Circle(object):
#    pi = 3.14
#    def __init__(self,radius):
#        self.radius = radius
#    @property
#    def area(self):
#        # radius ** 2 * pi
#        return (self.radius ** 2) * Circle.pi
#        self.result = (self.radius ** 2) * Circle.pi
#        print self.result
#c = Circle(radius=100)##
