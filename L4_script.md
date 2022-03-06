## Lesson 4 Script

## Tutorial 1 Functions

Functions

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

# draw rectangle
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

plus triangle

```python
import turtle

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 4
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 3
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)
```

Problem: **DRY**

Unnecssary reassignment of `length`

```python
import turtle

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 4

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 3

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)
```

Repeition of the `for` loop

Create functions

```python
import turtle

def draw_shape(sides,length):
    # draw a shape with given sides and given length
    for i in range(sides):
        my_ttl.forward(length)
        my_ttl.left(360/sides)

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

draw_shape(6,100)
my_ttl.penup

draw_shape(4,100)
draw_shape(3,100)
```

Problem: **DRY**

Unnecssary reassignment of `length`

```python
import turtle

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 4

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 3

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)
```

Repeition of the `for` loop

Create functions

```python
import turtle

def draw_shape(sides,length):
    # draw a shape with given sides and given length
    for i in range(sides):
        my_ttl.forward(length)
        my_ttl.left(360/sides)

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

draw_shape(6,100)
my_ttl.penup

draw_shape(4,100)
draw_shape(3,100)
```

## Tutorial 2 User input

Now that we have labels, we can ask the user for their value

```python
import turtle

screen = 500
sides = input("Number of sides> ")
length = input("Length of sides> ")

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)
```

> TypeError: 'str' object cannot be interpreted as an integer

Why the error. `input` accepts values as strings, but we need numbers.

Functions

Do a bit of tidying up

```python
import turtle

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)
```

Draw more than one shape?

Hexagon plus square

```python
import turtle

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 4
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)
```

plus triangle

```python
import turtle

# screen settings
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 4
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)

# shape parameters
sides = 3
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360/sides)
```
