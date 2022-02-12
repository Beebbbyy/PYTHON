from itertools import count
import turtle, random

from markupsafe import re
from numpy import true_divide
# The word list is here: 
word_list = ['which', 'their', 'would', 'there', 'could', 'other', 'about', 'great', 'these', 'after', 'first', 'never', 'where', 'those', 'shall', 'being', 'might', 'every', 'think', 'under', 'found', 'still', 'while', 'again', 'place', 'young', 'years', 'three', 'right', 'house', 'whole', 'world', 'thing', 'night', 'going', 'heard', 'heart', 'among', 'asked', 'small', 'woman', 'whose', 'quite', 'words', 'given', 'taken', 'hands', 'until', 'since', 'light']
answer=random.choice(word_list)
y=250

def draw_square(x,y,col):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(col)
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

def input_guess(prompt):
    my_input=turtle.textinput("5 Letter Word", prompt)
    if my_input == None: return "     "
    elif len(my_input) !=5:  
        return my_input[0:5]
    else: 
        return my_input.lower()

def check_guess(my_input,answer,y):
    count=0
    x=-250
    for i in my_input:
        if i== answer[count]: draw_square(x,y,"green")
        elif i in answer:
            draw_square(x,y,"yellow")
        else: draw_square(x,y,"red")
        count+=1
        x+=75
    turtle.penup()
    turtle.goto(x,y,-25)
    turtle.write(my_input,font=("Verdana",15,"normal"))

for i in range(6):
    guess_prompt="What is guess " + str(i+1) + "?"
    my_input=input_guess(guess_prompt)
    check_guess(my_input,answer,y)
    y-=75
    if my_input==answer:
        turtle.penup()
        turtle.goto(-300,-200)
        turtle.write("Well DONE!!", font=("Verdana", 42,"normal"))
else:
    turtle.penup()
    turtle.goto(-300,-200)
    turtle.write(answer, font=("Verdana", 42,"normal"))

turtle.done()