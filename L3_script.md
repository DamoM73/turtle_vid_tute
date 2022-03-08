# Leason 3 script

## Tutorial 1: Variables

### Learning objective

Understand how and when to use variables

### Replace magic numbers

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

What values did we change, and what do they represent?

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

### Remove calculations from meat space

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
## Exercises
- L3_Ex1

- L3_Ex2

- L3_Ex3

## Tutorial 2: Coordinates

Tidy-up

Show Coordinates example

Draw boarder

```python
import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

# draw boarder
my_ttl.goto(-240,-240)
for i in range(4):
    my_ttl.forward(480)
    my_ttl.left(90)

# shape parameters
sides = 6
length = 100

my_ttl.goto(0,0)

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)
```

Introduce pen_up/pen_down

```python
import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

# draw boarder
my_ttl.penup()
my_ttl.goto(-240,-240)
my_ttl.pendown()
for i in range(4):
    my_ttl.forward(470)
    my_ttl.left(90)
my_ttl.penup()
my_ttl.goto(0,0)
my_ttl.pendown()

# shape parameters
sides = 6
length = 100

# draw shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(360 / sides)
```

## Exercises

- L3Ex_4
