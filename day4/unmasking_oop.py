import math
import os
import sys


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





def main():
    small_circle = Circle(10)
    big_circle = Circle(50)

    print(small_circle)
    print(big_circle)

    # now we change units for all instances on the class
    Circle.units = 'pm'

    print(small_circle)
    print(big_circle)

    # but
    big_circle.units = 'hm'  # only change for the big_circle instance

    print(small_circle)
    print(big_circle)

    #canvas = Canvas(1200, 780)
    #canvas.mystery_method()
    #turtle.done()

   # print(area_of_circle(small_circle))
    #print(perimeter_of_circle(small_circle))
    #print(arc_length(small_circle, 75))
    #print(bounding_box(small_circle))
    print(small_circle.area_of_circle())
    print(small_circle.perimeter_of_circle())
    print(small_circle.bounding_box())
    print(small_circle.arc_length(50))


    return os.EX_OK



if __name__ == '__main__':
    sys.exit(main())
