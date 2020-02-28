# Method overriding is an ability of a class to change the implementation of a method of its paraent class.
# Means the subclass uses the same class name of its parent's with different implementation

class Shapes:
    def __init__(self, area = 0):
        self.area = area

    def calc_area(self):
        return self.area


class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calc_area(self):
        return self.length * self.breadth

class Circle:
    def __init__(self, radious):
        self.radious = radious

    def calc_area(self):
        return format((22/7) * (self.radious ** 2), '.2f')

class Square:
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side ** 2



shape = Shapes()
area = shape.calc_area()
print(area)


rect = Rectangle(10,20)
rect_area = rect.calc_area()
print(rect_area)

circle = Circle(radious=2)
rect_area = circle.calc_area()
print(rect_area)

sqr = Square(4)
sqr_area = sqr.calc_area()
print(sqr_area)