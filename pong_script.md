# Pong Script

### Objectives

- Event-driven programming
- Key bindings

### Draw Screen

The first thing we need to do is create the screen and draw a line down the middle.

```python
import turtle

# vairable
screen_width = 1000
screen_height = 600

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)


# ---- MAIN LOOP ---- #
while True:
    window.update()
```

### Add paddles

#### Left Paddle

``` python
import turtle

# vairable
screen_width = 1000
screen_height = 600

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"


# ---- MAIN LOOP ---- #
while True:
    window.update()
```

### Right Paddle

```python
import turtle

# vairable
screen_width = 1000
screen_height = 600

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# ---- MAIN LOOP ---- #
while True:
    window.update()
```

### Make left paddle move up

``` python
import turtle

# vairable
screen_width = 1000
screen_height = 600

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# ---- MAIN LOOP ---- #
while True:
    window.update()
    current_x = left_pad.xcor()
    current_y = left_pad.ycor()
    new_y = current_y + 10
    left_pad.goto(current_x,new_y)
```

### Slow down left paddle

```python
import turtle
import time

# vairable
screen_width = 1000
screen_height = 600
paddle_speed = 10
game_speed = .05

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# ---- MAIN LOOP ---- #
while True:
    window.update()
    current_x = left_pad.xcor()
    current_y = left_pad.ycor()
    new_y = current_y + paddle_speed
    left_pad.goto(current_x,new_y)
    time.sleep(game_speed)
```

### Create movement function

```python
import turtle
import time

def movement():
    current_x = left_pad.xcor()
    current_y = left_pad.ycor()
    new_y = current_y + paddle_speed
    left_pad.goto(current_x,new_y)

# vairable
screen_width = 1000
screen_height = 600
paddle_speed = 10
game_speed = .05

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# ---- MAIN LOOP ---- #
while True:
    window.update()
    time.sleep(game_speed)
    movement()
```

### Move left paddle up or down

```python
import turtle
import time

def movement():
    if left_pad.dir == "up":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y + paddle_speed
        left_pad.goto(current_x,new_y)
    elif left_pad.dir == "down":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y - paddle_speed
        left_pad.goto(current_x,new_y)

# vairable
screen_width = 1000
screen_height = 600
paddle_speed = 10
game_speed = .05

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# ---- MAIN LOOP ---- #
while True:
    window.update()
    time.sleep(game_speed)
    left_pad.dir = "up"
    movement()
```

### Create Key bindings

Key bindings run a specific function when a key is:

- pressed
- on press
- on release

```python
import turtle
import time

def left_pad_up():
    left_pad.dir = "up"

def left_pad_down():
    left_pad.dir = "down"
    
def left_pad_stop():
    left_pad.dir = "stop"

def movement():
    if left_pad.dir == "up":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y + paddle_speed
        left_pad.goto(current_x,new_y)
    elif left_pad.dir == "down":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y - paddle_speed
        left_pad.goto(current_x,new_y)

# vairable
screen_width = 1000
screen_height = 600
paddle_speed = 10
game_speed = .05

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# key bindings
window.listen()
window.onkeypress(left_pad_up, "w")
window.onkeyrelease(left_pad_stop,"w")
window.onkeypress(left_pad_down, "s")
window.onkeyrelease(left_pad_stop,"s")

# ---- MAIN LOOP ---- #
while True:
    window.update()
    time.sleep(game_speed)
    movement()
```

### Repeat for Right Pad

```python
import turtle
import time

def left_pad_up():
    left_pad.dir = "up"

def left_pad_down():
    left_pad.dir = "down"
    
def left_pad_stop():
    left_pad.dir = "stop"
    
def right_pad_up():
    right_pad.dir = "up"

def right_pad_down():
    right_pad.dir = "down"
    
def right_pad_stop():
    right_pad.dir = "stop"


def movement():
    if left_pad.dir == "up":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y + paddle_speed
        left_pad.goto(current_x,new_y)
    elif left_pad.dir == "down":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y - paddle_speed
        left_pad.goto(current_x,new_y)
    
    if right_pad.dir == "up":
        current_x = right_pad.xcor()
        current_y = right_pad.ycor()
        new_y = current_y + paddle_speed
        right_pad.goto(current_x,new_y)
    elif right_pad.dir == "down":
        current_x = right_pad.xcor()
        current_y = right_pad.ycor()
        new_y = current_y - paddle_speed
        right_pad.goto(current_x,new_y)
        

# vairable
screen_width = 1000
screen_height = 600
paddle_speed = 10
game_speed = .05

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# key bindings
window.listen()
window.onkeypress(left_pad_up, "w")
window.onkeyrelease(left_pad_stop,"w")
window.onkeypress(left_pad_down, "s")
window.onkeyrelease(left_pad_stop,"s")
window.onkeypress(right_pad_up, "p")
window.onkeyrelease(right_pad_stop,"p")
window.onkeypress(right_pad_down, ";")
window.onkeyrelease(right_pad_stop,";")


# ---- MAIN LOOP ---- #
while True:
    window.update()
    time.sleep(game_speed)
    movement()
```

