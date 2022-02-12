from cProfile import label
from email import message
from graphics import *

displayArea=GraphWin('Rainbow Circle', 300, 300)
# def main():
#     win = GraphWin('Face', 200, 150)
#     win.yUp()

#     head=Circle(Point(40,200), 25)
#     head.setFill("yellow")
#     head.draw(win)

#     eye1=Circle(Point(30, 105),5)
#     eye1.setFill('blue')
#     eye1.draw(win)

#     eye2=Line(Point(45,105), Point(55,105))
#     eye2.setWidth(3)
#     eye2.draw(win)

#     mouth=Oval(Point(100,120),'A face')
#     mouth.setFill("red")
#     mouth.draw(win)

#     label=Text(Point(100,120), 'A face')
#     label.draw(win)

#     message=Text(Point(win.getWidth()/2,20),'Click anywhere to quit.')
#     message.draw(win)
#     win.getMouse()
#     win.close()

# main()