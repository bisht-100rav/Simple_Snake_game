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
head.direction = "stop"       # object movement

######### Functions ##############

#  movement of the snake_head
def move():
    if head.direction == "up":     # making head move in up direction by
        y = head.ycor()            # by changing its y coordinate
        head.sety(y + 20)

    if head.direction == "down":     # making head move in down direction by
        y = head.ycor()            # by changing its y coordinate
        head.sety(y - 20)

    if head.direction == "right":     # making head move in right direction by
        x = head.xcor()            # by changing its x coordinate
        head.setx(x + 20)

    if head.direction == "left":     # making head move in left direction by
        x = head.xcor()            # by changing its x coordinate
        head.setx(x - 20)

# Function for changing direction of the head

def go_up():                       # function to go up
    head.direction = "up"

def go_down():                       # function to go down
    head.direction = "down"

def go_right():                       # function to go right
    head.direction = "right"

def go_left():                       # funcion to go left
    head.direction = "left"


# Setting up keyboard bindings

wn.listen()                       # calling keyboard input
wn.onkeypress(go_up, "w")         # BY pressing 'w' head moves up
wn.onkeypress(go_down, "s")       # BY pressing 's' head moves down
wn.onkeypress(go_right, "d")      # BY pressing 'd' head moves right
wn.onkeypress(go_left, "a")       # BY pressing 'a' head moves left


#Main game loop
while True:
    wn.update()  #  updating screen every refresh

    move()   #  calling movement funciton

    time.sleep(delay)  # calling of the delay variable




wn.mainloop()
