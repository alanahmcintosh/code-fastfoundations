import sys
import turtle


def draw_rectangle():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)


def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()

def draw_triangle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("black")
    pen.fillcolor("purple")
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.end_fill()
    pen.up()



def find_angle_from_sides(n):
    return 360/n

def draw_pentagom():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("black")
    pen.fillcolor("purple")
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.left(72)
    pen.forward(100)
    pen.end_fill()
    pen.up()

def my_name():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    #pen.begin_fill()
    pen.pencolor("black")
    #pen.fillcolor("purple")
    pen.write('Alanah', align='left', font=('Arial', 48, 'bold'))
    #pen.end_fill()
    pen.up()

def main():
    #draw_rectangle()
    #draw_circle()
    #draw_triangle()
    #draw_pentagom()
    #print(find_angle_from_sides(5))
    my_name()
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
