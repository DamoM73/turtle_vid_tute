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

#### L4_Ex1.py

```python
import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

############################################
## Convert the code below using functions ##
############################################

# move pen
my_ttl.penup()
my_ttl.goto(0,-200)
my_ttl.pendown()

# draw head
my_ttl.color("black","yellow")
my_ttl.begin_fill()
my_ttl.circle(200)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(-75,0)
my_ttl.pendown()

# draw eye
my_ttl.color("black","black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(75,0)
my_ttl.pendown()

# draw eye
my_ttl.color("black","black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(-100,-75)
my_ttl.pendown()

# draw mouth
my_ttl.color("black","black")
my_ttl.begin_fill()
for i in range(2):
    my_ttl.forward(200)
    my_ttl.right(90)
    my_ttl.forward(25)
    my_ttl.right(90)
my_ttl.end_fill()

my_ttl.hideturtle()
```

#### L4_Ex2.py

```python
import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

############################################
## Use you knowledge of Python and Turtle ##
## to draw a car. Use functions to ensure ##
## that you Do not Repeat Yourself.       ##
############################################
```



## Tutorial 2: User Input

How can we make the computer respond to the user?

Consider this code. To make a different shape, the user needs to be a programmer and know which values to change.

``` python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = 9
length = 100

draw_poly(length,sides)
```

There is a way for the user to give a value for the number and length of the sides

``` python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = input("How many sides?> ")
length = input("How long are the sides?> ")

draw_poly(length,sides)
```

Error: `TypeError: 'str' object cannot be interpreted as an integer`

All input is received as a string

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = int(input("How many sides?> "))
length = int(input("How long are the sides?> "))

draw_poly(length,sides)
```

### Exercises

#### L4_Ex3.py

``` python
###############################################
## write a program that askes the user for a ##
## number and then counts up to that number. ##
###############################################

```

