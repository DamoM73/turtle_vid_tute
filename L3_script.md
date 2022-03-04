# Leeson 3 script

## Learning objective

Understand how and when to use variables

## Replace magic numbers

Look at code for an interated square

```python
import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(4):
    my_ttl.forward(100)
    my_ttl.left(90)
```

What do we need to change to make this into a large triangle?

```python
import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
```

What values fdid we change, and what do they represent?

- 4 - # sides

- 200 - length

- 90 - degrees

These are magic numbers

> A 'magic number' is a literal value that appears in a program.

Remove the magic numbers from the code, by giving them labels. These labels are called variables.

```python
import turtle

sides = 3
length = 200
degrees = 120

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(degrees)
```

Change to a hexagon

Change length to 100

Are there any more magic numbers?

## Remove calculations from meat space

How did we know that degrees = 60?

Remove unnecessary variables

Change code.

```python
import turtle

screen = 500
sides = 6
length = 100

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)
```

L3_Ex1

L3_Ex2

## Functions

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

## Coordinates


