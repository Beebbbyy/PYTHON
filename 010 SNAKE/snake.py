from inspect import trace
from math import ceil
from tkinter import CENTER
import turtle
import time
import random

delay=0.1

score=0
high_score=0

wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width=600,height=600)
wn.tracer(0)


head =  turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction='stop'

food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

sc=turtle.Turtle()
sc.speed(0)
sc.shape('square')
sc.color('black')
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0 High Score:0" , align='center', font=('ds-digital', 24, 'normal'))

def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction !='up':
        head.direction = 'down'
def go_left():
    if head.direction!='right':
        head.direction ='left'
def go_right():
    if head.direction!='left':
        head.direction ='right'
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.sety(x-20)
    if head.direction=='right':
        x=head.xcor()
        head.sety(x+20)
    
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_left,'a')
wn.onkeypress(go_right,'d')

while True:
    wn.update()

    #check collision with border area
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'

        for segment in segments:
            segment.goto(1000, 1000)
        segment.clear()

        score=0

        delay =








