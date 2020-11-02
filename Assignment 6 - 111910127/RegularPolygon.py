from Shape import Shape # From the Shape.py file import the Shape Class
from math import tan, pi

import turtle
turtleObject = turtle.Turtle()

class RegularPolygon(Shape): # Child class of Shape
    def __init__(self, numberOfSides = 6, sideLength = 100):
        self._numberOfSides = numberOfSides
        self._angleValue = 360 / self._numberOfSides
        self._sideLength = sideLength
        return

    def getNumberOfSides(self):
        return self._numberOfSides

    def setNumberOfSides(self, numberOfSides):
        self._numberOfSides = numberOfSides
        self._angleValue = 360 / self._numberOfSides
        return

    def getAngleValue(self):
        return self._angleValue

    def getSideLength(self):
        return self._sideLength

    def setSideLength(self, sideLength):
        self._sideLength = sideLength
        return

    def getPerimeter(self):
        return self._numberOfSides * self._sideLength

    def getArea(self):
        apothem = self._sideLength / (2 * tan((180 / self._numberOfSides) * (pi / 180)))

        return (self.getPerimeter() * apothem) / 2

    def draw(self):
        for i in range(self._numberOfSides):
            turtleObject.forward(self._sideLength)
            turtleObject.left(self._angleValue)
        return

class Pentagon(RegularPolygon):
    def __init__(self, sideLength = 100):
        super().__init__(5, sideLength)
        return

class Hexagon(RegularPolygon):
    def __init__(self, sideLength = 100):
        super().__init__(6, sideLength)
        return

class Heptagon(RegularPolygon):
    def __init__(self, sideLength = 100):
        super().__init__(7, sideLength)
        return

class Octagon(RegularPolygon):
    def __init__(self, sideLength = 100):
        super().__init__(8, sideLength)
        return

o1 = Octagon(100)
print("Area is", o1.getArea())
print("Perimeter is", o1.getPerimeter())
o1.draw()
turtle.done()
