import sys
import math
import os

class Rectangle:
    def __init__(self, width, height, position=(0, 0), fill=("Red"), stroke="Black"):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def __str__(self):  # Python special methods
        return f"I am a rectangle of length {self.width} and height {self.height}. I have area {self.area()}. I have diagonal {self.diagonal()}. My coordinates are {self.bounding_box()}. My perimeter equals {self.perimeter()}."


    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def bounding_box(self):
        xmin = self.position[0] - self.width/2
        xmax = self.position[0] + self.width/2
        ymin = self.position[1] - self.height/2
        ymax = self.position[1] + self.height/2
        return xmin, xmax, ymin, ymax

class Circle:
    units = 'cm'  # all circles will have the same units


    def __init__(self, radius, position=(0, 0)):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.diameter = 2 * radius
        #self.area = math.pi * radius ** 2

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}, with a diameter of {self.diameter}."


    def area_of_circle(self):
        return math.pi * self.radius ** 2

    def perimeter_of_circle(self):
        return 2 * math.pi * self.radius


    def arc_length(self, angle, degrees=False):
        """Function to compute the arc length l for the angle provided"""
        if degrees:
            angle = math.radians(angle)
        return self.radius * angle



    def bounding_box(self):
        """Function to compute the four values of the bounding box for a circle"""
        # xmin, xmax, ymin, ymax
        xmin = self.position[0] - self.radius
        xmax = self.position[0] + self.radius
        ymin = self.position[1] - self.radius
        ymax = self.position[1] + self.radius
        return xmin, xmax, ymin, ymax


class Canvas:
    def __init__(self, length, height, position=(0,0), fill=("White")):
        self.length = length
        self.height = height
        self.position = position
        self.fill = fill

class Text:

    def __init__(self, text, colour=("Black"), position=(3,3)):
        self.text = text
        self.position = position
        self.colour = colour

    def __str__(self):
        return f"My signature is {self.text}"






def main():
    rectangle = Rectangle(10, 15)

    print(rectangle)
    #print(rectangle.position)
    #print(rectangle.bounding_box())
    #print(rectangle.area())
    #print(rectangle.diagonal())
    #print(rectangle.perimeter())

    return os.EX_OK

if __name__ == '__main__':
    sys.exit(main())