from Shape import Shape # from Shape.py file import the class Shape
import turtle # for drawing shapes
from math import pi

turtleObject = turtle.Turtle() # creating the Turtle Object

class Circle(Shape): # Child class of Shape
    def __init__(self, radius = 50): # Constructor 
        self.__radius = radius
        return

    def draw(self):
        turtleObject.circle(self.__radius)
        return

    def getCircumference(self): # returns the circumference of the circle 
        return 2 * pi * self.__radius

    def getArea(self): # returns the area of the circle
        return pi * self.__radius * self.__radius

    def getRadius(self): # returns the radius of the cirlce
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius
        return

c1 = Circle(50)
rad = c1.getRadius()
circumference = c1.getCircumference()
area = c1.getArea()
print("Radius of circle is", rad)
print("Circumference of circle is", circumference)
print("Area of circle is", area)

c1.draw()
turtle.done()
