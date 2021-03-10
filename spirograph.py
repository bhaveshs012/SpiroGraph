

# Drawing a SpiroGraph 

import random
import turtle as t

t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


my_turtle = t.Turtle()
screen = t.Screen()
my_turtle.color("blue")
my_turtle.speed("fastest")

def draw_spirograph(offset):
    for _ in range(int(360/offset)):   # Once it reaches where it started loop will stop rather than overlapping the circles again 
        my_turtle.pencolor(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + offset)

draw_spirograph(3)  # Degree by which the turtle needs to rotate each time

# So the loop should go until 360/ offset to stop where it started


screen.exitonclick()