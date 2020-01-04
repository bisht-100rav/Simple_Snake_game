#Importing the turtle module
import turtle

#turtle is an inbuilt module in python
import time  # time module to create delays

delay = 0.1  # setting up delay variable
#Setting up the screen
wn = turtle.Screen()                     #  Iinitialising main window
wn.title("Snake game by Dipali")         #  Main Window Title
wn.bgcolor( "lightgreen")                      #  Setting up background color
wn.setup(width = 600,height = 600)       #  Main window's size(resolution)
wn.tracer(0)                         #  this function is used to remove animations in the main window


#Snake Head

head = turtle.Turtle()    # crating a turtle object
head.speed(0)             # setting animation speed of object
head.shape("square")      # shape of the object
head.color("black")       # color of the object
head.penup()              # functionso that turtle does'nt draw any line
head.goto(0,0)            # placement of object in the middle of screen
head.direction = "up"       # object movement

######### Functions ##############

#movement of the snake_head
def move():
    if head.direction == "up":     # making head move in updirection by
        y = head.ycor()            # by changing its y coordinate
        head.sety(y + 20)



#Main game loop
while True:
    wn.update()  #  updating screen every refresh

    move()   #  calling movement funciton

    time.sleep(delay)  # calling of delay varible




wn.mainloop()
