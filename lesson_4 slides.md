---
marp: true
---

# Python Turtle - Lesson 4

---

## Topics

In this lesson you will learn:

- What is coding modularisation
- When to use *functions* in Python
- How to define and use functions in Python
- How to get user's input into your code
- What are *data types*
- How to convert between data types

---

## Part 1: Functions

---

### What are functions?

Functions are:

- blocks of code that we can run several times in our program
- how to use:
  - block of code outside of the main program sequence
  - give it a label
  - use that block by *calling* it

To understand this more clearly, we will start with my solution for ***lesson_3_ex_4.py**.

---

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
for index in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for index in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
# move pen
my_ttl.penup()
my_ttl.goto(-25,-200)
my_ttl.pendown()

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(-80,-100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(45,-100)
my_ttl.pendown()

# draw square
for index in range(4):
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

---

PRIMM:

- *Predict* &rarr; the type of house that the code will draw
- *Run* &rarr; did it resembles your prediction?

DRY principle - **Don't Repeat Yourself**

Can you identify any repetition?

---

Let's look at the comments?

- move pen
- draw square
- draw triangle
- move pen
- draw rectangle
- move pen
- draw square
- move pen
- draw square
- move pen
- draw circle

---

In summary we have two main types of repetition:

- moving the pen
- drawing the shape

In writing code I used a heap of copy and paste.

- clear indicator of a need for functions.
- functions &rarr; main tool to enforce the DRY Principle.

---

### Creating functions

#### Take all the *move pen code* and consolidate that in one spot
   
Copy the first move pen action (lines `17` to `20`)

``` python
# move pen
my_ttl.penup()
my_ttl.goto(-100,0)
my_ttl.pendown()
```

Then paste them up to the top (lines `3` to `6`)

---

Turned them into a function

``` python
def move_pen():
    my_ttl.penup()
    my_ttl.goto(-100,0)
    my_ttl.pendown()
```

Replace the original code with a call to the function

``` python
move_pen()
```

Your code should look the same as the next slide:

---

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
for index in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for index in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
# move pen
my_ttl.penup()
my_ttl.goto(-25,-200)
my_ttl.pendown()

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(-80,-100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(45,-100)
my_ttl.pendown()

# draw square
for index in range(4):
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

---

PRIMM:

- *Predict* what you think will happen
- *Run* the code and check you prediction

Now lets *investigate* the code by unpacking it:

- line `3`: `def move_pen():` &rarr; creates the function:
- lines `4` to `6` are indented &rarr; the code that is executed when the function is called
- line `22`: `move_pen()` &rarr calls the function:

---

### Passing arguments

Adjust for other pen movements:

- coordinate values &rarr; magic numbers
- need a way to send the coordinates to the function when called
- these are called arguments.

What are the magic numbers?

``` python
def move_pen():
    my_ttl.penup()
    my_ttl.goto(-100,0)
    my_ttl.pendown()
```

---

What do the two magic numbers represent? 

- `x` coordinate
- `y` of the coordinates

Replace them with variables.

``` python
def move_pen():
    my_ttl.penup()
    my_ttl.goto(x, y)
    my_ttl.pendown()
```

---

But how do we assign values to `x` and `y`? 

Use arguments:

- function definition &rarr; `def move_pen(x, y):` 
- function call &rarr; `move_pen(-100,0)` 

``` python
def move_pen(x, y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()

...

move_pen(-100,0)

```

---

Let's unpack that:

- `def move_pen(x, y):`
  - when you call the `move_pen()` function &rarr; need to provide two values
    - first value &rarr; assigned to `x`
    - second value &rarr; assigned to `y`
- `move_pen(-100,0)` says:
  - call the `move_pen()` function
  - `-100` &rarr; `x` value
  - `0` &rarr; `y` value

Your code should now look like the following code:

---

```python
import turtle

def move_pen(x, y):
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
for index in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for index in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
# move pen
my_ttl.penup()
my_ttl.goto(-25,-200)
my_ttl.pendown()

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(-80,-100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
# move pen
my_ttl.penup()
my_ttl.goto(45,-100)
my_ttl.pendown()

# draw square
for index in range(4):
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

---

Run code &rarr; check it draws the house

Use the debugger &rarr; step your way through the program.

Replace the remaining `# move pen` blocks with a `move_pen()` call.

Your code should now look like the following slide:

---

```python
import turtle

def move_pen(x, y):
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
for index in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for index in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
move_pen(-25,-200)

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)
    
move_pen(-80,-100)

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

move_pen(45,-100)

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)
    
move_pen(15,-150)

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

---

Run code &rarr; check it draws the house

Line count down from `71` to `61`

---

#### Testing

Testing hints:

- frequently test your code
- each time you change your code, test it
- too many changes between testing &rarr; harder to identify errors
- function passes test &rarr; don't need to testing it again, unless changed
- errors occur and functions passed tests &rarr; error is elsewhere in the code

---

### Shape functions

Identified the drawing shapes repetition &rarr; make function to draw squares

Process:

- copy first `# draw square` blocks to the top of the code
- change it into a function called `draw_square()`
- function needs one argument: `length`
- replace all `# draw square` blocks with appropriate `draw_square()` call

---

#### Functions location

Function definitions &rarr; top of code, after import statements

- prevents `NameError` being generated
- easier to find them and read your code

After `draw_square()` function changed, code should look like:

---

```python
import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()
    
def draw_square(length):
    for index in range(4):
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
for index in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)
    
move_pen(-25,-200)

# draw rectangle
for index in range(2):
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

---

We are now down to 52 lines of code.

---

No more repetition in the main code &rarr; three code blocks remaining

Transform the `# draw triangle`, `# draw rectangle` and `# draw circle` into functions

Provide two benefits:

- the code more readable
- easier to extend the drawing

Test each function when created

Finished code should look like this:

---

```python
import turtle

def move_pen(x,y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()
    
def draw_square(length):
    for index in range(4):
        my_ttl.forward(length)
        my_ttl.right(90)
        
def draw_triangle(length):
    for index in range(3):
        my_ttl.forward(length)
        my_ttl.left(120)

def draw_rectangle(long, short):
    for index in range(2):
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

---

That's our final code:

- down from `71` lines to `53` lines
- easier to read
- easier to test and troubleshoot errors

---

## Part 1 Exercises

The exercises are the *make* component of the PRIMM model

Work through the three exercise and *make* your own code

---

## Part 2: User Input

---

Copy the code below, save it as **lesson_4_pt_2.py**

``` python
import turtle

def draw_poly(length, sides):
    for index in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.setup(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = 9
length = 100

draw_poly(length,sides)
```

---

PRIMM

- *Predict* what you think will happen.
- *Run* the code and see how close your prediction is.
- *Modify* the code so the shape fits within the window.

Run the code &rarr; shape is partially off the screen

Change the length from `100` &rarr; `80`

Simple for people who know how to code &rarr; what about those who don't

---

How do we make our programs interactive by getting the user's input?

Use the `input()` command &rarr; ask user for input in the **Shell**.

To do this change:

- line `17` to `sides = input("How many sides?> ")`
- line `18` to `length = input("How long are the sides?> ")`

---

Your code should look like:

``` python
import turtle

def draw_poly(length, sides):
    for index in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.setup(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = input("How many sides?> ")
length = input("How long are the sides?> ")

draw_poly(length,sides)
```

---

PRIMM

- *Predict* what you think will happen
- *Run* run the code. Did it do what you thought?

---

Did you predict this?

![user input](./assets/input.png)

---

Did you predict this?

```
Traceback (most recent call last):
  File "<string>", line 20, in <module>
  File "<string>", line 4, in draw_poly
TypeError: 'str' object cannot be interpreted as an integer
```

---

- Let's *investigate* by:
  - unpacking the code we changed
  - explaining the error

---

Unpacking line `17`

- `input` &rarr; keyword &rarr; get input from the user
- `("How many sides?> ")` &rarr; what *prompt* to write to the **Shell**
- `sides =` &rarr; assigns user input to `sides`

To understand `TypeError` &rarr; learn about *data types*

---

### Data types

Variables can hold different types of data

- integer numbers (`int`) &rarr; store whole numbers
- floating point numbers (`float`) &rarr; store numbers that have a decimal points
- strings (`str`) &rarr; store characters like letters, numbers and special characters
- Booleans (`bool`) &rarr; store either `True` or `False`

Data types establish what operations can be used with the variable.

---

```
Traceback (most recent call last):
  File "<string>", line 20, in <module>
  File "<string>", line 4, in draw_poly
TypeError: 'str' object cannot be interpreted as an integer
```

---

Break down:

- `TypeError: 'str' object cannot be interpreted as an integer` &rarr; trying to use string when integer
- `Traceback` &rarrl check the last line first:
  - error occurred at line `4` `for index in range(sides):`
  - trying to use `sides` to create a `range()`
  - Python thinks it is a string!
  - where did we get the value for `sides`?
- line `17`: `sides = input("How many sides?> ")`: 
  - user input &rarr; assigned it to `sides`
  - user entered `3` &rarr; integer, but Python think &rarr; string. WT!

---

User input with the `input()` command &rarr; always a string

String can contain all characters

To fix we convert the variable's data type

---

### Converting data types

If we had a variable called `var`:

- convert `var` &rarr; string: `str(var)`
- convert `var` &rarr;integer: `int(var)`
- convert `var` &rarr; float: `float(var)`

---

Change `input()` string &rarr; integer:

- `sides = int(input("How many sides?> "))`
- `length = int(input("How long are the sides?> "))`

---

```python
import turtle

def draw_poly(length, sides):
    for index in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.setup(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

sides = int(input("How many sides?> "))
length = int(input("How long are the sides?> "))

draw_poly(length,sides)
```

---

PRIMM

- *Predict* &rarr; what will happen
- *Run* code &rarr; were predictions were correct?
- *Investigate* &rarr; enter different values for sides and length:
  - draw different shapes
  - what values draw a circle?
  - enter float or string
- *Modify* &rarr; use different prompts

---

## Part 2 Exercise

The exercises are the *make* component of the PRIMM model

Work through the last lesson 3 exercise and *make* your own code