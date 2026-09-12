import math
import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.goto(0, -40)

for _ in range(16):
    for j in range(18):
        turtle.color("#FFA216")
        turtle.rt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.lt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.rt(180)
    turtle.circle(40, 24)

turtle.color("black")
turtle.shape("circle")
turtle.shapesize(0.5)
turtle.fillcolor("#8B4513")

GOLDEN_ANG = 137.508
PHI = GOLDEN_ANG * math.pi / 180
for i in range(140):
    r = 4 * math.sqrt(i)
    theta = i * PHI
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * GOLDEN_ANG)
    turtle.pendown()
    turtle.stamp()

turtle.hideturtle()
turtle.done()


