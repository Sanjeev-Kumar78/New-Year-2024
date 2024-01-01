from turtle import *
import colorsys
import random

t = Turtle()
# Canvas size
setup(1000, 600)
# Screen().bgpic("New Year 2023\\newyear.gif")
bgcolor(random.choice(["red", "blue", "green", "yellow", "purple", "orange", "white","pink","brown","gray","cyan","magenta","lightgreen","lightblue","lightpink","lightyellow","lightgray","darkgreen","darkblue","darkred","darkgray"]))
tracer(50)
pensize(5)

for i in range(300):
    c = colorsys.hsv_to_rgb(i/300.0, 1.0, 1.0)
    h = c[0]*205
    c1 = colorsys.hsv_to_rgb(i/350.0, 0.5, 0.9)
    pencolor(c)
    fillcolor("black")
    # Go to the center of the screen
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Draw the text
    t.color("white")
    t.write("Happy New Year!", align="center", font=("Arial", 36, "bold"))
    t.penup()
    t.goto(0, -40)
    t.pendown()
    t.write("2023", align="center", font=("Arial", 36, "bold"))
    for i in range(2):
        # Go to the center of the screen
        t.penup()
        t.goto(0, -2)
        t.pendown()

        # Draw the text
        t.speed(20)
        t.color(c1)
        # t.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange", "white","pink","brown","gray","cyan","magenta","lightgreen","lightblue","lightpink","lightyellow","lightgray","darkgreen","darkblue","darkred","darkgray"]))
        t.write("Happy New Year!", align="center", font=("Arial", 36, "bold"))
        t.penup()
        t.goto(0, -42)
        t.pendown()
        t.write("2024", align="center", font=("Arial", 36, "bold"))
    begin_fill()
    for j in range(2):
        fd(i*1.2)
        rt(60)
        fd(300)
        rt(120)
    rt(121)
    end_fill()
Screen().bgcolor("black")
done()
