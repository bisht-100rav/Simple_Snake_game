#Importing the turtle module
import turtle
#turtle is an inbuilt module in python

import time  # time module to create delays
import random  # randomizer



delay = 0.1     # setting up delay variable
score = 0       # variable for the score
high_score = 0  # variable for the high score

#Setting up the screen
wn = turtle.Screen()                     #  Iinitialising main window
wn.title("Snake game by Dipali")         #  Main Window Title
wn.bgcolor( "lightgreen")                      #  Setting up background color
wn.setup(width = 600,height = 600)       #  Main window's size(resolution)
wn.tracer(0)                         #  this function is used to remove animations in the main window


# Snake Head

head = turtle.Turtle()    # crating a turtle object
head.speed(0)             # setting animation speed of object
head.shape("square")      # shape of the object
head.color("black")       # color of the object
head.penup()              # functionso that turtle does'nt draw any line
head.goto(0,0)            # placement of object in the middle of screen
head.direction = "stop"       # object movement initially

# Snake food
food = turtle.Turtle()    # crating a turtle object
food.speed(0)             # setting animation speed of object
food.shape("circle")      # shape of the object
food.color("red")       # color of the object
food.penup()              # function so that turtle does'nt draw any line
food.goto(random.randint(-270,250),random.randint(-270,270))            # placement of object in the random posi of screen

#creating list for body segments
segments = []

# PEN   Scoring text for the snake game
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 00 High Score: 00", align= "center", font = ("Courier", 24,"normal"))

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

def go_up():     # function to go up
    if head.direction != 'down':
        head.direction = "up"

def go_down():                       # function to go down
    if head.direction != 'up':
        head.direction = "down"

def go_right():                       # function to go right
    if head.direction != 'left':
        head.direction = "right"

def go_left():                       # funcion to go left
    if head.direction != 'right':
        head.direction = "left"


# Setting up keyboard bindings

wn.listen()
wn.onkeypress(go_up, "w")         # BY pressing 'w' head moves up
wn.onkeypress(go_down, "s")       # BY pressing 's' head moves down
wn.onkeypress(go_right, "d")      # BY pressing 'd' head moves right
wn.onkeypress(go_left, "a")       # BY pressing 'a' head moves left

#Main game loop
while True:
    wn.update()  #  updating screen every refresh

    # check for collision with the border
    if head.xcor()>290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # pause screen for 1 sec
        head.goto(0,0)  # initialise posi of snake after death
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000,1000)   # remove turtle outside the screen

        # clear the segments list
        segments.clear()

        # reset score
        score = 0

        # reset the speed of the snake
        dealy = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font = ("Courier", 24, "normal"))



    # checking collision of food with head
    if head.distance(food) < 20:
        # move food to a random spot
        x = random.randint(-290, 290)    # posi is from center to left and right
        y = random.randint(-290, 290)    # posi is from center to up and down
        food.goto(x,y)

        # if food is eaten, add a segment to head
        new_segment = turtle.Turtle()    # crating a turtle object
        new_segment.speed(0)             # setting animation speed of object
        new_segment.shape("square")      # shape of the object
        new_segment.color("dimgrey")       # color of the object
        new_segment.penup()              # functionso that turtle does'nt dr
        segments.append(new_segment)     # joining new segment with each other

        # shorten the delay to increase speed of snake
        delay -= 0.005

        # Increase the score
        score += 10

        # change the high score
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font = ("Courier", 24, "normal"))

        # movement of end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()     # moves last head to second last head position in x posi
        y = segments[index-1].ycor()     # moves last head to second last head postion in y posi
        segments[index].goto(x,y)

        # move segment 0(first one after head) to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()   #  calling movement funciton

    # check for snake collision with itself( body)
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segments
            segments.clear()


    time.sleep(delay)  # calling of the delay variable




wn.mainloop()