# Pong Script

## Draw the screen

```python
import turtle

# setup screen
window = turtle.Screen()
window.setup(1000,600)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)             # turns off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,300)
ui.pendown()
ui.goto(0,-300)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto(-470,0)

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto(465,0)

# create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()

# ----- MAIN LOOP -----
while True:
    window.update()
```

## Make paddles move

Make left paddle go up

```python
import turtle
import time

def left_pad_up():
    current_x = left_pad.xcor()
    current_y = left_pad.ycor()
    new_y = current_y+10
    left_pad.goto(current_x, new_y)

# setup screen
window = turtle.Screen()
window.setup(1000,600)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)             # turns off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,300)
ui.pendown()
ui.goto(0,-300)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto(-470,0)

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto(465,0)

# create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()

# ----- MAIN LOOP -----
while True:
    window.update()
    left_pad_up()
    time.sleep(.05)
```

Make left paddle go down

```python
import turtle
import time

def left_pad_up():
    current_x = left_pad.xcor()
    current_y = left_pad.ycor()
    new_y = current_y+10
    left_pad.goto(current_x, new_y)

def left_pad_down():
    current_x = left_pad.xcor()
    current_y = left_pad.ycor()
    new_y = current_y-10
    left_pad.goto(current_x, new_y)

# setup screen
window = turtle.Screen()
window.setup(1000,600)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)             # turns off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,300)
ui.pendown()
ui.goto(0,-300)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto(-470,0)

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto(465,0)

# create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()

# ----- MAIN LOOP -----
while True:
    window.update()
    left_pad_down()
    time.sleep(.05)
```

Have paddle react to keys

```python
import turtle
import time

def left_pad_up():
    global left_pad_dir
    left_pad_dir = "up"

def left_pad_down():
    global left_pad_dir
    left_pad_dir = "down"
    
def movement():
    # left pad
    if left_pad_dir == "up":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y+10
        if new_y > 270:
            new_y = 270
        left_pad.goto(current_x, new_y)
    elif left_pad_dir == "down":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y-10
        if new_y < -270:
            new_y = -270
        left_pad.goto(current_x, new_y)   
        

# setup screen
window = turtle.Screen()
window.setup(1000,600)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)             # turns off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,300)
ui.pendown()
ui.goto(0,-300)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto(-470,0)
left_pad_dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto(465,0)
right_pad_dir = "stop"

# create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()

# key bindings
window.listen()
window.onkey(left_pad_up,"w")
window.onkey(left_pad_down,"s")

# ----- MAIN LOOP -----
while True:
    window.update()
    time.sleep(.05)
    movement()
```

Now setup right padel

```python
import turtle
import time

def left_pad_up():
    global left_pad_dir
    left_pad_dir = "up"

def left_pad_down():
    global left_pad_dir
    left_pad_dir = "down"
    
def right_pad_up():
    global right_pad_dir
    right_pad_dir = "up"

def right_pad_down():
    global right_pad_dir
    right_pad_dir = "down"
    
def movement():
    # left pad
    if left_pad_dir == "up":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y+10
        if new_y > 270:
            new_y = 270
        left_pad.goto(current_x, new_y)
    elif left_pad_dir == "down":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y-10
        if new_y < -270:
            new_y = -270
        left_pad.goto(current_x, new_y)
    
    # right pad
    if right_pad_dir == "up":
        current_x = right_pad.xcor()
        current_y = right_pad.ycor()
        new_y = current_y+10
        if new_y > 270:
            new_y = 270
        right_pad.goto(current_x, new_y)
    elif right_pad_dir == "down":
        current_x = right_pad.xcor()
        current_y = right_pad.ycor()
        new_y = current_y-10
        if new_y < -270:
            new_y = -270
        right_pad.goto(current_x, new_y)
    
        

# setup screen
window = turtle.Screen()
window.setup(1000,600)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)             # turns off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,300)
ui.pendown()
ui.goto(0,-300)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto(-470,0)
left_pad_dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto(465,0)
right_pad_dir = "stop"

# create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()

# key bindings
window.listen()
window.onkey(left_pad_up,"w")
window.onkey(left_pad_down,"s")
window.onkey(right_pad_up,"p")
window.onkey(right_pad_down,";")

# ----- MAIN LOOP -----
while True:
    window.update()
    time.sleep(.05)
    movement()
```

## Make ball move

```python
ssa
```

