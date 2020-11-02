from Shape import Shape # From the Shape.py file import the Shape class
from math import pi, sin

import turtle
turtleObject = turtle.Turtle()

class Quadrilateral(Shape): # Child class of Shape
    def __init__(self, side1 = None, side2 = None, side3 = None, side4 = None, angle1 = None, angle2 = None, angle3 = None, angle4 = None):
        self._numberOfSides = 4
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._side4 = side4
        self._angle1 = angle1
        self._angle2 = angle2
        self._angle3 = angle3
        self._angle4 = angle4
        return

    def draw(self):
        sides = [self._side1, self._side2, self._side3, self._side4]
        angles = [self._angle1, self._angle2, self._angle3, self._angle4]

        for i in range(self._numberOfSides):
            turtleObject.forward(sides[i])
            turtleObject.left(angles[i])
        return

    def getPerimeter(self):
        return self._side1 + self._side2 + self._side3 + self._side4

    def getArea(self):
        return self._side1 * self._side2 * sin(self._angle1 * (pi / 180))

    def getAngleValues(self):
        return (self._angle1, self._angle2, self._angle3, self._angle4)

    def getSideLengths(self):
        return (self._side1, self._side2, self._side3, self._side4)

    def setSideLengths(self, side1 = None, side2 = None, side3 = None, side4 = None):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._side4 = side4
        return

    def setAngleValues(self, angle1 = None, angle2 = None, angle3 = None, angle4 = None):
        self._angle1 = angle1
        self._angle2 = angle2
        self._angle3 = angle3
        self._angle4 = angle4
        return

    def getNumberOfSides(self):
        return self._numberOfSides


class Square(Quadrilateral): # Child Class of Quadrilateral
    def __init__(self, sideLength = 50):
        super().__init__(side1 = sideLength, angle1 = 90)
        self._side2 = self._side3 = self._side4 = self._side1 # since all sides of square are equal
        self._angle2 = self._angle3 = self._angle4 = self._angle1 # since all angles of square are equal
        return

    def getSideLength(self):
        return self._side1

    def setSideLength(self, sideLength):
        self._side1 = self._side2 = self._side3 = self._side4 = sideLength
        return

    def getAngleValue(self):
        return self._angle1

class Rectangle(Quadrilateral): # Child Class of Quadrilateral
    def __init__(self, length = 50, breadth = 40):
        super().__init__(side1 = length, side2 = breadth, angle1 = 90)
        self._side3 = self._side1
        self._side4 = self._side2
        self._angle2 = self._angle3 = self._angle4 = self._angle1
        return

    def getLength(self):
        return self._side1

    def setLength(self, length):
        self._side1 = self._side3 = length
        return

    def getBreadth(self):
        return self._side2

    def setBreadth(self, breadth):
        self._side2 = self._side4 = breadth
        return

    def getAngleValue(self):
        return self._angle1

class Rhombus(Quadrilateral): # Child Class of Quadrilateral
    def __init__(self, sideLength = 100, angle1 = 60):
        super().__init__(side1 = sideLength, angle1 = angle1)
        self._side2 = self._side3 = self._side4 = self._side1
        self._angle3 = self._angle1 # Opposite angles of rhombus are equal
        self._angle2 = 180 - self._angle1 # Adjacent angles of rhombus are supplementary
        self._angle4 = self._angle2
        return

    def setSideLength(self, sideLength):
        self._side1 = self._side2 = self._side3 = self._side4 = sideLength
        return

    def getSideLength(self):
        return self._side1

    # Use getAngleValues() of the Quadrilateral Class for getting angles

    def setAngleValues(self, angle1):
        super().setAngleValues(angle1 = angle1)
        self._angle3 = self._angle1
        self._angle2 = 180 - self._angle1
        self._angle4 = self._angle2
        return

class Parallelogram(Quadrilateral): # Child Class of Quadrilateral
    def __init__(self, side1 = 200, side2 = 100, angle1 = 60):
       super().__init__(side1 = side1, side2 = side2, angle1 = angle1)
       self._side3 = self._side1
       self._side4 = self._side2
       self._angle3 = self._angle1 # Opposite angles of Parallelogram are equal
       self._angle2 = 180 - self._angle1 # Adjacent angles of Parallelogram are supplementary
       self._angle4 = self._angle2
       return

    def setSideLengths(self, side1, side2):
        super().setSideLengths(side1 = side1, side2 = side2)
        self._side3 = self._side1
        self._side4 = self._side2
        return

    # Use function getSideLengths() to get the lengths of sides

    def setAngleValues(self, angle1):
        super().setAngleValues(angle1 = angle1)
        self._angle3 = self._angle1
        self._angle2 = 180 - self._angle1
        self._angle4 = self._angle2
        return

    # Use function getAngleValues() to get the angles

r1 = Rectangle(100, 50)
print("Area is", r1.getArea())
print("Perimeter is", r1.getPerimeter())
r1.draw()
turtle.done()
