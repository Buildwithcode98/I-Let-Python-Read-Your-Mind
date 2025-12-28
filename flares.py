import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

points = []
for i in range(200):
    a = i * 0.1
    points.append([a, random.uniform(0.8, 1.2)])

time = 0

while True:
    t.clear()
    time += 0.03

    for a, m in points:
        x = 220 * math.sin(a + time) * math.cos(time * m)
        y = 220 * math.cos(a - time) * math.sin(time * m)

        hue = (a * 10 + time * 20) % 360
        t.color((hue / 360, 1, 1))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(3)

    screen.update()

