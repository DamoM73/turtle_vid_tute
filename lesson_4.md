# Python Turtle - Lesson 4

> **Topics:**
> In this lesson you will learn:
>
> - [ ] about coding modularisation
> - [ ] when and how to use functions in Python
> - [ ] how to accept user's input into your code
> - [ ] about data types
> - [ ] how to convert between data types

## Part 1: Functions

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZQNU29m5pHY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### What are functions?

**Functions** are blocks of code that we can run several times in our program. So far in our programming, all our blocks of code are only run once. Even loop blocks are only run once, although the code inside the block is repeated. But once you have gone past a loop, you can't go back and run it gain.

With functions, we move a block of code outside of the main program sequence, then give it a name. We can then use that block as many times as we like by **calling** the function name from within the main program sequence.

To understand this more clearly, we will start with my solution for **lesson_3_ex_4.py**.

Here is the flowchart for the solution:

<img align="left" src="assets/flowchart_lesson_4_1.png">

Here is the code. Type it into a new file and save in as **lesson_4_pt_1.py**.

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
my_ttl.goto(-100, 0)
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
my_ttl.goto(-25, -200)
my_ttl.pendown()

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)

# move pen
my_ttl.penup()
my_ttl.goto(-80, -100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

# move pen
my_ttl.penup()
my_ttl.goto(45, -100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

# move pen
my_ttl.penup()
my_ttl.goto(15, -150)
my_ttl.pendown()

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

PRIMM:

- **Predict** the type of house that the code will draw
- **Run** the code and see if it resembles your prediction.

Remember the DRY principle (**Don't Repeat Yourself**)? Look at the code. How well does it go in relation to DRY?

Can you identify any repetition?

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

In summary we have two main types of repetition:

- moving the pen
- drawing the shape

When I wrote this code, I didn't type it straight out, I copied and pasted a lot of the code and just changed the magic values. Copying and pasting is a clear indicator that you need to use a function. Why? Because functions are one of the main tools we can use to enforce the DRY Principle.

### Creating functions

Let's look at how this works.

1. Take all the **move pen code** and consolidate that in one spot.
   - Below I have copied the first move pen action (lines `17` to `20` in the previous code)
   - I have pasted them up to the top (lines `4` to `7`)
   - I then turned them into a function
2. Replace the original code with a **call** to the function (line `24`).

Adjust your code so that it looks the same as below:

```python
import turtle


def move_pen():
    my_ttl.penup()
    my_ttl.goto(-100, 0)
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
my_ttl.goto(-25, -200)
my_ttl.pendown()

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)

# move pen
my_ttl.penup()
my_ttl.goto(-80, -100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

# move pen
my_ttl.penup()
my_ttl.goto(45, -100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

# move pen
my_ttl.penup()
my_ttl.goto(15, -150)
my_ttl.pendown()

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

PRIMM:

- **Predict** what you think will happen
- **Run** the code and check you prediction

Now lets **investigate** the code by unpacking it:

- Line `4`: `def move_pen():` create the function:
  - In programming we call this **defining** a function.
  - The program reads and bookmarks the code, but does not execute it.
  - `def` is the key word for defining a function.
  - `move_pen` is the name we are giving the function.
    - This name is how the function is called and follows the same rules as variable names.
    - By using a descriptive name, we also remove the need for comments, as the code explains itself.
  - `()` is where we can put values. We'll deal with this soon.
  - `:` tells Python that an indented code block follows (the same as a `for` loop).
- Lines `5` to `7` are indented:
  - This is the code that is executed when the function is called
  - The indentation rules are the same as the `for` loop
    - indentations can be many lines
    - multiple line indented code is called a **block**
    - indents should be four spaces
- Line `24`: `move_pen()` calls the function:
  - At this point the program will go to line `4` run the code in the function.
  - When the code in the function is finished, the program will return to line `24` and continue with the rest of the code.

### Passing arguments

This works for our first pen movement, but since the coordinate values are magic numbers, I would have to create a function for each movement of the pen. This defeats the purpose of functions. What we need is a way to send the coordinates to the function when we call it. Well, we can, and they are called **arguments**.

Looking back at our `move_pen` function in the code, what we need to do is get rid of those magic numbers.

``` python
def move_pen():
    my_ttl.penup()
    my_ttl.goto(-100, 0)
    my_ttl.pendown()
```

What do the two magic numbers in `my_ttl.goto(-100,0)` represent? The `x` and the `y` of the coordinates. So let's replace them with variables.

``` python
def move_pen():
    my_ttl.penup()
    my_ttl.goto(x, y)
    my_ttl.pendown()
```

But how do we assign values to `x` and `y`? This is where **arguments** are used.

1. Change the function definition to `def move_pen(x, y):` so it will **accept** two values.
2. Change the function call in line `24` to `move_pen(-100,0)` passing two values to the function.

Let's unpack that:

- `def move_pen(x, y):` says:
  - When you call the `move_pen` function, you need to provide two values.
  - First value will be assigned to the variable `x`.
  - Second value will be assigned to the variable `y`.
- `move_pen(-100,0)` says:
  - Call the `move_pen` function.
  - Use `-100` as the first value (the `x` value).
  - Use `0` as the second value (the `y` value).

Your code should now look like the code below:

```python
import turtle


def move_pen(x, y):
    my_ttl.penup()
    my_ttl.goto(x, y)
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

move_pen(-100, 0)

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
my_ttl.goto(-25, -200)
my_ttl.pendown()

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)

# move pen
my_ttl.penup()
my_ttl.goto(-80, -100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

# move pen
my_ttl.penup()
my_ttl.goto(45, -100)
my_ttl.pendown()

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

# move pen
my_ttl.penup()
my_ttl.goto(15, -150)
my_ttl.pendown()

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

PRIMM

- **Predict** what this code will now do.
- **Run** the code to check if your prediction was correct.
- **Investigate** the code by using the debugger and stepping your way through the program.

---

Go through the code and replace the remaining `# move pen` blocks with a `move_pen()` call.

Your code should now look like this:

```python
import turtle


def move_pen(x, y):
    my_ttl.penup()
    my_ttl.goto(x, y)
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

move_pen(-100, 0)

# draw square
for index in range(4):
    my_ttl.forward(200)
    my_ttl.right(90)

# draw triangle
for index in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)

move_pen(-25, -200)

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)

move_pen(-80, -100)

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

move_pen(45, -100)

# draw square
for index in range(4):
    my_ttl.forward(35)
    my_ttl.right(90)

move_pen(15, -150)

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

**Run** the code to make sure the house is still being drawn.

Notice that our line count is down from the original `71` to `63`.

> **Testing**
>
> Testing hints:
>
> - It is good to frequently test your code.
> - Each time you change your code, test it.
> - Try not to make too many changes between testing, it makes it harder to identify your errors.
> - If a function is tested and works, you don't have to testing it again, unless your change the function.
> - If your program has errors, and your functions have passed their tests, then you know your error is elsewhere in the code.

### Functions in Flowcharts

Flowcharts normally don't represent whole programs, they represent algorithms. 

> **Algorithms**
>
> Algorithms are basically a set of rules to be followed to solve a problem. A cake recipe is an algorithm to bake a cake. You follow an algorithm to perform long division in maths. In computers, you code instructions are the algorithms. 

When a program is broken into smaller algorithms (eg. functions) you create a flowchart for each algorithm, and then show when one algorithm calls another algorithm.

We show the name of the function in the terminator symbol, with the first algorithm being called **main**.

Here is the flowchart of the code with the `move_pen` function. The function calls use the procedure symbol (I have coloured them red to make them stand out).

<img align="left" src="assets/flowchart_lesson_4_2.png">

### Shape functions

When we first looked for repetition, we also identified the drawing shapes repetition. Lets make a function to draw squares.

From the current code:

- copy one of the `# draw square` blocks to the top of the code
- change it into a function that draws a square called `draw_square`
- the function will need to accept a value for the `length` of the square's side
- then replace all the `# draw square` blocks with an appropriate `draw_square` call

> **Function location**
>
> Normally we put all out function definitions at the top of our code, just under the import statements.
>
> This is done for two reasons:
>
> - If the function is not defined before you call it, your code will generate a `NameError`.
> - Placing all your functions at the start improves you code's maintainability by making it easier to find them.

Once you have made `draw_square` function changes, you code should look like:

```python
import turtle


def move_pen(x, y):
    my_ttl.penup()
    my_ttl.goto(x, y)
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

move_pen(-100, 0)
draw_square(200)

# draw triangle
for index in range(3):
    my_ttl.forward(200)
    my_ttl.left(120)

move_pen(-25, -200)

# draw rectangle
for index in range(2):
    my_ttl.forward(50)
    my_ttl.left(90)
    my_ttl.forward(100)
    my_ttl.left(90)

move_pen(-80, -100)
draw_square(35)
move_pen(45, -100)
draw_square(35)
move_pen(15, -150)

# draw circle
my_ttl.circle(5)
my_ttl.hideturtle()
```

We are now down to 55 lines of code.

---

There is no more repetition in the main code, but there is still three code blocks remaining. Notice how the rest of the code is easier to read? Therefore, we are going to transform the `# draw triangle`, `# draw rectangle` and `# draw circle` code blocks into functions.

This will provide two benefits:

- It will improve maintainability by making the code more readable.
- If we want to extend the drawing we can easily add more rectangles, triangle and circles.

See if you can change all three blocks into functions. Remember to test each function when you create it.

When you finish your code should look like this:

```python
import turtle


def move_pen(x, y):
    my_ttl.penup()
    my_ttl.goto(x, y)
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

move_pen(-100, 0)
draw_square(200)
draw_triangle(200)
move_pen(-25, -200)
draw_rectangle(100, 50)
move_pen(-80, -100)
draw_square(35)
move_pen(45, -100)
draw_square(35)
move_pen(15, -150)
draw_circle(5)
my_ttl.hideturtle()
```

That's our final code:

- Down from `71` lines to `59` lines.
- Easier to read.
- Easier to test and troubleshoot errors.

Maybe the easiest way to see the improvement in our code is to look at the flowchart.

<img align="left" src="assets/flowchart_lesson_4_3.png">

## Part 1 Exercises

In this course, the exercises are the **make** component of the PRIMM model. So work through the following exercises and make your own code.

### Exercise 1

Create a new file and save it in your subject folder calling it **lesson_4_ex_1.py**. Then type the following code into it.

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
my_ttl.goto(0, -200)
my_ttl.pendown()

# draw head
my_ttl.color("black", "yellow")
my_ttl.begin_fill()
my_ttl.circle(200)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(-75, 0)
my_ttl.pendown()

# draw eye
my_ttl.color("black", "black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(75, 0)
my_ttl.pendown()

# draw eye
my_ttl.color("black", "black")
my_ttl.begin_fill()
my_ttl.circle(50)
my_ttl.end_fill()

# move pen
my_ttl.penup()
my_ttl.goto(-100, -75)
my_ttl.pendown()

# draw mouth
my_ttl.color("black", "black")
my_ttl.begin_fill()
for index in range(2):
    my_ttl.forward(200)
    my_ttl.right(90)
    my_ttl.forward(25)
    my_ttl.right(90)
my_ttl.end_fill()

my_ttl.hideturtle()
```

Follow the instructions in the comments and adapt the code so it uses functions.

### Exercise 2

Create a new file and save it in your subject folder calling it **lesson_4_ex_2.py**. Then type the following code into it.

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

Follow the instructions in the comments and write a program that draws a car.

## Part 2: User Input

<iframe width="560" height="315" src="https://www.youtube.com/embed/HUEgYhYAuB0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introduction

Copy the code below, save it as **lesson_4_pt_2.py** then run it.

``` python
import turtle


def draw_poly(length, sides):
    for index in range(sides):
        my_ttl.forward(length)
        my_ttl.right(360 / sides)


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create instance of turtle
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

sides = 9
length = 100

draw_poly(length, sides)
```

PRIMM

- **Predict** what you think will happen.
- **Run** the code and see how close your prediction is.
- **Modify** the code so the shape fits within the window.

When we run the code the shape is partially off the screen. That's not a big problem, you just need to change the length from `100` to `80`. This something quite simple for you, because you have learnt how to code, but what about people who haven't?

How do we make our programs interactive by getting input from users who cannot code?

### Making your program interactive

The simplest way to make your program interactive is to use the `input` command which will ask the user for their input in the **Shell**.

To do this change:

- line `19` to `sides = input("How many sides?> ")`
- line `20` to `length = input("How long are the sides?> ")`

Your code should look like the following:

``` python
import turtle


def draw_poly(length, sides):
    for index in range(sides):
        my_ttl.forward(length)
        my_ttl.right(360 / sides)


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create instance of turtle
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

sides = input("How many sides?> ")
length = input("How long are the sides?> ")

draw_poly(length, sides)
```

PRIMM

- **Predict** what you think will happen.
- **Run** run the code. Did it do what you thought?
  - Did you predict:
    - a **prompt** appearing in the **Shell** like the image below?
    - the program raising an error.

<img style="border:1px solid black" align="left" src="./assets/input.png">

```
Traceback (most recent call last):
  File "<string>", line 22, in <module>
  File "<string>", line 5, in draw_poly
TypeError: 'str' object cannot be interpreted as an integer
```

- Let's **investigate** by:
  - unpacking the code we changed
  - explaining the error

Unpacking line `19` (note line `20` is virtually the same):

- `input`: is the keyword that tells Python to wait for an input from the user from the **Shell**.
- `("How many sides?> ")` tells Python what **prompt** to write to the **Shell** before it waits for a response.
- `sides =` takes whatever the user enters and assigns it to the variable `sides`

Now for the error. This is a `TypeError` and to understand it we need to learn about **data types**.

### Data types

Variables in Python can hold different types of data. The four types of data we will be concerned with are:

- **integer numbers** (`int`)
  - stores whole numbers
  - can be identified by a whole whole number
- **floating point numbers** (`float`)
  - stores numbers that have a decimal points
  - can be identified by having a decimal point with at least one number after it. For example, `1` is and integer, `1.0` is a float
- **strings** (`str`)
  - stores characters like letters, numbers and special characters
  - start and end with `"` or `'` (just make sure they are the same the at beginning or end)
  - numbers can be a string. For example, a phone number like `0432 789 367` is a string not and integer or float. It contains spaces and you would never do a calculation with it.
- **Booleans** (`bool`)
  - stores either `True` or `False`

Using data types helps Python work out what kind of operations it can do with the variable. For example, it wouldn't make much sense to divide a string. Python also has special operations called **methods**. Each data type has it's own collection of methods. You will learn more about data types throughout your programming journey.

Now, lets look at the error again:

```
Traceback (most recent call last):
  File "<string>", line 22, in <module>
  File "<string>", line 5, in draw_poly
TypeError: 'str' object cannot be interpreted as an integer
```

Breaking the error down:

- Error line `4`: `TypeError: 'str' object cannot be interpreted as an integer`:
  - This tells us that this involves two data types (string and integer).
  - It says we are trying to use a string when Python is expecting an integer.
- `Traceback`:
  - When looking at a `Traceback` always check the last line first
  - Error line `3` tells us that the error occurred at line `5` in the code: `for index in range(sides):`
    - Here we are trying to use the values in `sides` in a `range` function but Python thinks it is a string.
    - let's look at where we got the value for `sides`
  - Line `19`: `sides = input("How many sides?> ")`
    - We took the value the user entered and assigned it to `sides`.
    - I entered `3` which is an integer.
    - Why does Python think it's a string?

When Python accepts a value using the `input` function, it is always accepted it as a string. This is because strings can contain all characters.

How do we fix this? Luckily we can convert a variable's data type.

### Converting data types

There is a function to convert any data type into each other data type (other than Boolean).

If we had a variable called `var`:

- convert `var` &rarr; string, use `str(var)`
- convert `var` &rarr; integer, use `int(var)`
- convert `var` &rarr; a float, use `float(var)`

There is a great deal more to this, but at the moment this is all you need to know.

So let's change our code so that the strings that are received by the `input` functions are converted into integers.

Here is the finished code as a flowchart. Note that we use the same symbol for input as we do for output, with different wording.

<img align="left" src="assets/flowchart_lesson_4_4.png">

Below is the finished code, with the changes on lines `19` and `20`.

```python
import turtle


def draw_poly(length, sides):
    for index in range(sides):
        my_ttl.forward(length)
        my_ttl.right(360 / sides)


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create instance of turtle
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

sides = int(input("How many sides?> "))
length = int(input("Length of sides?> "))

draw_poly(length, sides)
```

PRIMM

- **Predict** what you think will happen
- **Run** you code and see if your predictions were correct
- **Investigate** by trying to enter different values for sides and length:
  - draw different shapes
  - what are the correct values to make your turtle draw a circle?
  - what happens when you enter a float or a string?
- **Modify** your code to use different prompts

## Part 2 Exercise

In this course, the exercises are the make component of the PRIMM model. So work through the following exercises and make your own code.

### Exercise 4

Create a new file and save it in your subject folder calling it **lesson_4_ex_4.py**. Then type the following code into it.

``` python
###############################################
## write a program that askes the user for a ##
## number and then counts up to that number. ##
###############################################
```

Follow the instructions in the comments and use your Python knowledge to create a count up app. Remember to apply the DRY principle
