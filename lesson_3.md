# Lesson 3

> **Topics**
> In this lesson you will:
>
> - [ ] learn how to store values in variables
> - [ ] learn when to use variables

## Tutorial 1: Variables

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/mG1O_JamxjQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Conventual range

Before we start looking at variables, we want to make our use of range more conventual.

Previously we would print four numbers using the code below

``` python
for number in range(1,5):
    print(number)
```

If you run this code you get:

```
1
2
3
4
```

If we weren't worried about the actual numbers, and we just needed to loop 4 times we could say:

``` python
for number in range(0,4):
    print(number)
```

This will produce:

```
0
1
2
3
```

It still has four iterations, but just starts counting at 0.

In Python the `range` function, if you don't provide a starting number, it will automatically start from `0`. So we could just say.

``` python
for number in range(4):
    print(number)
```

### Replace magic numbers

Look at code below for an iterated square. 

```python
import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(4):
    my_ttl.forward(100)
    my_ttl.left(90)
```

What do we need to change to make this into a large triangle with a length of 200 for each size? Try and work it out before looking at the code below.

```python
import turtle

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
```

What values did we change? What do those numbers represent?

- `4` &rarr; `3` representing the number sides
- `100` &rarr; `200` representing the length of the sides
- `90` &rarr; `120` representing the degrees the Turtle has to turn

If I wanted to make a hexagon, or any other shape, you would need to change these values each time.

In programming these are called *magic numbers*. A *magic number* is a literal value that appears in a program. Magic numbers are not good. If someone else was to look at my code, they would have to work out what the `3`, `200` and `120` meant. Additionally, if my program drew 1000 squares, and I wanted to change them all to triangles, I would have to make 3000 edits.

To write better code we remove the magic numbers by giving them labels. These labels are called variables.Below is the triangle code.

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

Lets break that code down

- `sides = 3` creates the variable `sides` and assigns the value of `3` to it
- `length = 200` creates the variable `length` and assigns the value of `200` to it
- `degress = 120` creates the variable `degrees` and assigns the value of `120` to it
- `for i in range(sides):` substitutes `sides` with the value assigned to it so the line becomes `for i in range(3)`.
- `my_ttl.forward(length)` substitutes `length` with the value assigned to it so the line becomes `my_ttl.forward(200)`
- `my_ttl.left(degrees)` substitutes `degrees` with the value assigned to it so the line becomes `my_ttl.left(120)` 

Using variables, I can copy the `for` loop and use it as many times as I want, and the values for `sides`, `length`, and `degrees` will always be whatever I assigned to the at the beginning. In programming this is called a *single point of truth*. This means that by changing the value assigned to `sides` I can change the value for all places where `sides` is used. Same for `length` and `degrees`.

Type our new code into Thonny and change it so to draw a hexagon with a side length of 100.

Your code should look like:

```python
import turtle

sides = 6
length = 100
degrees = 60

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(degrees)
```

### Remove calculations from 'meat space'

In creating our hexagon, how did we know that degrees needed to be 60? You may have worked it out in your head, or you calculated it using a calculator. But both of these approaches are flawed. 

- head calculations can be incorrect
- time is wasted in getting a calculator.

We can do the calculations directly in Python. The values assigned to `degrees` is `360` divided by the number assigned to `sides`. In code we would write that as `degrees = 306 / sides`

Let's put that into our code:

```python
import turtle

sides = 6
length = 100
degrees = 360 / sides

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(degrees)
```

Another good programming practice is to remove unnecessary variables. Do we need the `degrees` variable? We could simply place the calculation in the `for` loop.

So our code would look like this:

```python
import turtle

sides = 6
length = 100

window = turtle.Screen()
window.setup(500, 500)
my_ttl = turtle.Turtle()

for i in range(360 / sides):
    my_ttl.forward(length)
    my_ttl.left(degrees)
```

Are there any more *magic numbers*? See if you can find any more.

```python
import turtle

screen = 500
sides = 6
length = 100
DEGREES_IN_CIRCLE = 360

window = turtle.Screen()
window.setup(screen, screen)
my_ttl = turtle.Turtle()

for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(DEGREES_IN_CIRCLE / sides)
```

## Part 1 Exercises

In this course, the exercises are the *make* component of the PRIMM model. So work through the following exercise and *make* your own code.

### Exercise 1

Create a new file and save it in your subject folder calling it **`lesson_3_ex_1.py`**. Then type the following code into it.

``` python
import turtle

#################################################
## Change the variable values to draw a square ##
#################################################

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

Follow the instructions in the comments and change the code so it draws a square

### Exercise 2

Create a new file and save it in your subject folder calling it **`lesson_3_ex_2.py`**. Then type the following code into it.

``` python
import turtle

#################################################
## Change the variable values to draw a circle ##
#################################################

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

Follow the instructions in the comments and change the code so it draws a circle

### Exercise 3

Create a new file and save it in your subject folder calling it **`lesson_3_ex_3.py`**. Then type the following code into it.

```python
import turtle

###################################################
## Change the variable values to draw a pentagon ##
###################################################

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

Follow the instructions in the comments and change the code so it draws a pentagon.

## Tutorial 2: Coordinates

Before we keep going, we should tidy the code up by implementing some good coding principles. we will:

- group code under their functionality (what they do)
- use comment to signpost what this functionality

```python
import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("arrow")

# shape parameters
sides = 6
length = 100
DEGREES_IN_CIRCLE = 360

# draw the shape
for i in range(sides):
    my_ttl.forward(length)
    my_ttl.left(DEGREES_IN_CIRCLE / sides)
```

Anyone who reads the program now knows the location for the code that deals with the functionality of:

- setting up the screen
- creating the turtle instance
- defining the shape parameters
- drawing the shape

Save the file a **`lesson_3_pt_3.py`**

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

### Exercises

#### L3Ex_4

```python
import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("dot")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################
```

