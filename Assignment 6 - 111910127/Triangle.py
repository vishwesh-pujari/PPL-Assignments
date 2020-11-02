from Shape import Shape # from Shape.py import the shape class
from math import sqrt, sin, cos, tan, pi
import turtle # for drawing shapes
turtleObject = turtle.Turtle() # creating the Turtle Object

class Triangle(Shape):
    def __init__(self, side1 = 100, side2 = 100, side3 = 100, angle1 = 60, angle2 = 60, angle3 = 60): # Constructor 
        self.setAngleValues(angle1, angle2, angle3)
        self.setSideLengths(side1, side2, side3)
        self._numberOfSides = 3
        return

    def getNumberOfSides(self):
        return self._numberOfSides

    def draw(self):
        sides = [self._side1, self._side2, self._side3]
        angles = [self._angle1, self._angle2, self._angle3]
        
        for i in range(self._numberOfSides):
            turtleObject.forward(sides[i])
            turtleObject.left(180 - angles[i])
            
        return

    def getPerimeter(self): 
        return self._side1 + self._side2 + self._side3

    def getArea(self): 
        s = self.getPerimeter() / 2 # finding the semi perimeter
        return sqrt(s * (s - self._side1) * (s - self._side2) * (s - self._side3)) # heron's formula

    def getSideLengths(self): 
        return (self._side1, self._side2, self._side3)

    def setSideLengths(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        a, b, c = self._side1, self._side2, self._side3
        sina, sinb, sinc = sin(self._angle2 * (pi / 180)), sin(self._angle3 * (pi / 180)), sin(self._angle1 * (pi / 180))
        if (round(a / sina) == round(b / sinb) == round(c / sinc)): # Sine rule
            return
        print("Invalid side lengths")
        exit()

    def getAngleValues(self):
        return (self._angle1, self._angle2, self._angle3)

    def setAngleValues(self, angle1, angle2, angle3):
        self._angle1 = angle1
        self._angle2 = angle2
        self._angle3 = angle3
        if (self._angle1 + self._angle2 + self._angle3 != 180): 
            print("Invalid Angle Values")
            exit()
        return

class EquilateralTriangle(Triangle): # Child class of Triangle
    def __init__(self, side = 100):
        super().__init__(side, side, side, 60, 60, 60)
        return

    def setSideLength(self, side):
        self._side1 = self._side2 = self._side3 = side
        return

    def getSideLength(self):
        return self._side1

    def getAngleValue(self):
        return self._angle1

class IsoscelesTriangle(Triangle):
    def __init__(self, side = 100, equalAngle = 30):
        angle1 = angle3 = equalAngle
        angle2 = 180 - (angle1 + angle3)
        side2 = side3 = side
        side1 = (sin(angle2 * (pi / 180)) * side3) / sin(angle1 * (pi / 180))
        super().__init__(side1, side2, side3, angle1, angle2, angle3)
        return

    def setEqualSide(self, side):
        self._side2 = self._side3 = side
        self._side1 = (sin(self._angle2 * (pi / 180)) * self._side3) / sin(self._angle1 * (pi / 180))
        return

    # Use getSideLengths() method of parent class

    def setEqualAngle(self, equalAngle):
        self._angle1 = self._angle3 = equalAngle
        self._angle2 = 180 - (self._angle1 + self._angle3)
        return

    # Use getAngleValues() method of parent class

class RightTriangle(Triangle):
    def __init__(self, base = 100, angle1 = 45):
        side3 = tan(angle1 * (pi / 180)) * base
        side2 = sqrt((base ** 2) + (side3 ** 2))
        angle2 = 90 - angle1
        if (angle1 == 90 or angle2 == 90):
            print("Invalid angle values")
            exit()
        super().__init__(base, side2, side3, angle1, angle2, 90)
        return

    def setBase(self, base):
        self._side1 = base
        self._side3 = tan(self._angle1 * (pi / 180)) * base
        self._side2 = sqrt((base ** 2) + (self._side3 ** 2))
        return

    def setAngle(self, angle1):
        self._angle2 = 90 - self._angle1
        if (angle1 == 90 or angle2 == 90):
            print("Invalid angle values")
            exit()
        return
    
t1 = EquilateralTriangle(100)
print("Area is", t1.getArea())
print("Perimeter is", t1.getPerimeter())
t1.draw()
turtle.done()
