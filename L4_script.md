# Lesson 4 Script

## Tutorial 1 Functions

My solution for L3_Ex4

```python
import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

# move pen
my_ttl.penup()
my_ttl.goto(-100,0)
my_ttl.pendown()

# draw square
for i in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for i in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
# move pen
my_ttl.penup()
my_ttl.goto(-25,-200)
my_ttl.pendown()

# draw rectangle
for i in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(-80,-100)
my_ttl.pendown()

# draw square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(45,-100)
my_ttl.pendown()

# draw square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(15,-150)
my_ttl.pendown()

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

Can we identify the repetition:

- move pen
- draw shapes

Take all the move pen code and consolidate that in one spot.

```python
import turtle

def move_pen():
    my_ttl.penup()
    my_ttl.goto(-100,0)
    my_ttl.pendown()

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

move_pen()

# draw square
for i in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for i in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
# move pen
my_ttl.penup()
my_ttl.goto(-25,-200)
my_ttl.pendown()

# draw rectangle
for i in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(-80,-100)
my_ttl.pendown()

# draw square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(45,-100)
my_ttl.pendown()

# draw square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(15,-150)
my_ttl.pendown()

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

Ok for one movement. How can we adjust this to use of every pen movement?

```python
import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

move_pen(-100,0)

# draw square
for i in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for i in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
move_pen(-25,-200)

# draw rectangle
for i in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
move_pen(-80,-100)

# draw square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

move_pen(45,-100)

# draw square
for i in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
move_pen(15,-150)

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

- From 71 lines to 61 lines
- No errors in t=move pen, so I know the code is correct

Is there more repetition?

Squares

```python
import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()
    
def draw_square(length):
    for i in range(4):
        my_ttl.forward(length)
        my_ttl.right(90)

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

move_pen(-100,0)
draw_square(200)

# draw triangle
for i in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
move_pen(-25,-200)

# draw rectangle
for i in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
move_pen(-80,-100)
draw_square(35)
move_pen(45,-100)
draw_square(35)
move_pen(15,-150)

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

Down to 52 lines

Now the code is more readable. So let's extend that.

```python
import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()
    
def draw_square(length):
    for i in range(4):
        my_ttl.forward(length)
        my_ttl.right(90)
        
def draw_triangle(length):
    for i in range(3):
        my_ttl.forward(length)
        my_ttl.left(120)

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

move_pen(-100,0)
draw_square(200)
draw_triangle(200)
move_pen(-25,-200)

# draw rectangle
for i in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
move_pen(-80,-100)
draw_square(35)
move_pen(45,-100)
draw_square(35)
move_pen(15,-150)

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

Still 52 lines

Lets finish this.

```python
import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()
    
def draw_square(length):
    for i in range(4):
        my_ttl.forward(length)
        my_ttl.right(90)
        
def draw_triangle(length):
    for i in range(3):
        my_ttl.forward(length)
        my_ttl.left(120)

def draw_rectangle(long, short):
    for i in range(2):
        my_ttl.forward(short)
        my_ttl.left(90)
        my_ttl.forward(long)
        my_ttl.left(90)
        
def draw_circle(rad):
    my_ttl.circle(rad)

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

move_pen(-100,0)
draw_square(200)
draw_triangle(200)
move_pen(-25,-200)
draw_rectangle(100,50)
move_pen(-80,-100)
draw_square(35)
move_pen(45,-100)
draw_square(35)
move_pen(15,-150)
draw_circle(5)
my_ttl.hideturtle()
```

Now 53 lines, but much easier to read.

### Exercises

- L4_Ex1.py
- L4_Ex2.py

## Tutorial 2: User Input

