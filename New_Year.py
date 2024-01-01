from turtle import *
import random
import time
from turtle import TurtleGraphicsError
# Text to speech
from gtts import gTTS
from playsound import playsound


# Create the turtle
t = Turtle()
t.speed(20)

# Set the background color
Screen().bgpic("newyear.gif")

# Function to draw the fireworks
def draw_fireworks():
    for i in range(30):
        t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        t.forward(50)
        t.speed(5)
        t.right(80)

# Draw the fireworks
draw_fireworks()
a = 1
def shapes(a, num_sides):
    # loop for drawing shapes
    for i in range(num_sides):
        t.forward(100)
        t.pensize(a)
        a += 0.5
        t.right(360/num_sides)
        Screen().bgcolor(random.choice(["red", "blue", "green", "yellow", "purple", "orange", "white","pink","brown","gray","cyan","magenta","lightgreen","lightblue","lightpink","lightyellow","lightgray","darkgreen","darkblue","darkred","darkgray"]))
        t.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange", "white","pink","brown","gray","cyan","magenta","lightgreen","lightblue","lightpink","lightyellow","lightgray","darkgreen","darkblue","darkred","darkgray"]))
    Screen().bgcolor("black")

# Go to the top left corner
# t.penup()
# t.goto(-200, 200)
# t.pendown()

# # Draw the text
# t.color("white")
# t.write("Happy New Year!", font=("Arial", 36, "bold"))


# New Year 2024
mytext = "Happy New Year To All"
audio = gTTS(text=mytext, lang="en", slow=False)
try:
    audio.save("shapes.mp3")
    playsound("shapes.mp3")
except:
    print("Sorry, I can't play the audio")
t.penup()
t.goto(100,0)
t.pendown()

for i in range(3,5):
    shapes(a, i)

# Draw the text
t.color("white")
t.write("2024", font=("Arial", 36, "bold"))
t.forward(100)
# Go to the bottom right corner
t.penup()
t.goto(200, -100)
t.pendown()


t.color("yellow")
for i in range(5):
    t.forward(50)
    t.right(144)

t.penup()
t.goto(200, -200)
t.pendown()
t.color("red")
for i in range(5):
    t.forward(10)
    t.right(180)
    t.forward(10)
    t.right(180.6)
    t.forward(5)
    t.left(90)

t.color("gold")
t.begin_fill()
t.forward(20)
t.left(90)
t.forward(50)
t.left(90)
t.forward(40)
t.left(90)
t.forward(50)
t.end_fill()

t.color("white")
t.begin_fill()
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.end_fill()

t.color("gold")
t.begin_fill()
t.forward(10)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.right(90)
t.forward(20)
t.end_fill()

t.color("white")
t.begin_fill()
t.forward(10)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.right(90)
t.forward(20)
t.end_fill()

t.goto(200, -200)
t.color("gold")
t.begin_fill()
t.forward(10)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.right(90)
t.forward(20)
t.end_fill()

time.sleep(3)
Screen().clear()
from Turtle_Graphics import *
TurtleGraphicsError()


# Keep the window open
Screen().mainloop()
