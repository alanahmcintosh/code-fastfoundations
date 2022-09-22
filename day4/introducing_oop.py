import sys
import math
import os
import turtle


class Rectangle:
    def __init__(self, width, height, position=(0, 0), fill="Red", stroke="Black", angle=(0.0)):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke
        self.angle = angle

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


    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(15, 28)
        pen.down()
        pen.begin_fill()
        pen.pencolor("Black")
        pen.fillcolor("White")
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        pen.end_fill()
        pen.up()



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
    def draw(self, circle):
        pen = turtle.Turtle()
        if pen.isdown():
            pen.up()
        pen.goto(*self.position)
        pen.down()
        pen.begin_fill()
        pen.pencolor("Black")
        pen.fillcolor("White")
        pen.circle(self.radius)
        pen.end_fill()
        pen.up()


class Triangle:

    def __init__(self, length, angle):
        self.length = length
        self.angle = angle


    def draw(self, triangle):
        pen = turtle.Turtle()
        if pen.isdown():
            pen.up()
        pen.goto(15, 28)
        pen.down()
        pen.begin_fill()
        pen.pencolor("black")
        pen.fillcolor("purple")
        pen.forward(self.length)
        pen.left(self.angle)
        pen.forward(self.length)
        pen.left(self.angle)
        pen.forward(self.length)
        pen.end_fill()
        pen.up()

class Canvas(turtle.TurtleScreen):

    def __init__(self, width, length, bg = "white"):
        canvas = turtle.getcanvas()
        super().__init__(canvas)
        self.screensize(width, length, bg)
        self.width = width
        self.length = length
        self.pen = turtle.RawTurtle(canvas)

    def grid(self):
        self.pen.up()
        self.pen.goto(0, self.length / 2)
        self.pen.down()
        self.pen.goto(0, -self.length / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()

   # def draw_circle(self, circle):
        #pen = turtle.Turtle()
        #if pen.isdown():
         #   pen.up()
        #pen.goto(15, 28)
        #pen.down()
        #pen.begin_fill()
        #pen.pencolor("black")
        #pen.fillcolor("purple")
        #pen.circle(60)
        #pen.end_fill()
        #pen.up()
        #self.pen.circle(circle.radius)

    def draw(self,shape):
        shape.draw(self.pen)

    def write(self, phrase):
        phrase.write(self.pen)

    def __str__(self):
        return f"length = {self.length}, height = {self.length}"

class Text:

    def __init__(self, text, colour=("Black"), position=(3,3)):
        self.text = text
        self.position = position
        self.colour = colour

    def __str__(self):
        return f"My signature is {self.text}"

    def write(self, phrase):
        pen = turtle.Turtle()
        if pen.isdown():
            pen.up()
        pen.goto(15, 28)
        pen.down()
        # pen.begin_fill()
        pen.pencolor("black")
        # pen.fillcolor("purple")
        pen.write('Alanah', align='left', font=('Arial', 48, 'bold'))
        # pen.end_fill()
        pen.up()


class Square(Rectangle):
    def __init__(self, width, *args, **kwargs):
        super().__init__(width, width, *args, **kwargs)

    def __str__(self):  # Python special methods
        return f"I am a square of length {self.width}. I have area {self.area()}. I have diagonal {self.diagonal()}. My coordinates are {self.bounding_box()}. My perimeter equals {self.perimeter()}."



def main():

    rectangle = Rectangle(100, 150)
    signature = Text("Alanah")
    canvas = Canvas(1200,750)
    square = Square(400)
    circle = Circle(50)
    triangle = Triangle(100, 120)


    #print(square)
    #print(rectangle)
    #print(signature)
    #print(canvas)
    #print(rectangle.position)
    #print(rectangle.bounding_box())
    #print(rectangle.area())
    #print(rectangle.diagonal())
    #print(rectangle.perimeter())
    #print(square.position
    #print(square.bounding_box())
    #print(square.area())
    #print(square.diagonal())
    #print(square.perimeter())
    #canvas.grid()
    #canvas.draw_circle(circle)
    #canvas.draw(circle)
    #canvas.draw(square)
    #canvas.draw(triangle)
    canvas.write(signature)
    turtle.done()


    return 0

if __name__ == '__main__':
    sys.exit(main())