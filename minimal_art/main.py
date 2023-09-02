import turtle
from turtle import Turtle, Screen
import random

# #############################################
timmy = Turtle()
timmy.shape("turtle")
# ##############################################
tommy = Turtle()
tommy.shape("circle")
# #############################################
tammy = Turtle()
tammy.shape("classic")
# #############################################
turtle.colormode(255)
angles = [0, 90, 180, 270]

def get_image():
    """Takes a png screenshot of the tkinter window, and saves it
     in cwd"""
    print("...converting GUI window ro PNG")
    # ImageGrab.grab().crop((x0, y0, x1, y1)).save("minimalistic_art.png")
#
def generate_color() -> tuple:
    """This function generates random numbers from 0-225 and adds numbers
    to variables r, g, b. These variables are latter added as a tuple """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def turtle_attr():
    """This function adds the needed attributes for the different objects. """
    timmy.hideturtle()
    tommy.hideturtle()
    tammy.hideturtle()
    # #######################################
    timmy.penup()
    tommy.penup()
    tammy.penup()
    # #######################################
    tommy.speed("fast")
    tammy.speed("fastest")
    #########################################
    timmy.setposition(100, 90)
    tommy.setposition(-100, -100)


def draw():
    """This function draws using turtle graphics"""
    timmy.pen(pendown=True, pensize=5)
    tommy.pen(pendown=True, pensize=8)
    tammy.pen(pendown=True, pensize=2)
    # ##################################
    timmy.fd(50)
    tommy.fd(40)
    tammy.circle(70)
    # timmy.penup()
    # timmy.fd(20)

for i in range(3, 20):
    turtle_attr()
    timmy.color(generate_color())
    for n in range(i):
        draw()
        timmy.lt(round(360 / i, 3))
        # ##########################
        tommy.color(generate_color())
        tommy.setheading(random.choice(angles))
        ###############################
        # tammy.color(generate_color())
        tammy.setheading(tammy.heading() + round(360 / i))



# get_image()


# screen display configuration
screen = Screen()
screen.exitonclick()

