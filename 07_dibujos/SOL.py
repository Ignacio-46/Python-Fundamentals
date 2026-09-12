import  turtle

count = 1
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

while count < 300:
    t.forward(count)
    t.color("yellow")
    t.lt(143)
    t.lt(1)
    count += 1
    t.forward(count)
    t.rt(350)
    t.radians()
    t.color("orange")
    t.rt(30)
t.hideturtle()
turtle.done()