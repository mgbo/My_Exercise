
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

col=['red','blue','green','magenta','wheat']
for i in range(4):
	t.color(col[i%4])
	t.fd(100)
	t.lt(90)

turtle.done()
