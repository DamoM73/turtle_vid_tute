# Python Turtle - Lesson 6

> **Topics**
>
> In this lesson your will learn:
>
> - [ ] about Boolean logic and how it is used in Python
> - [ ] about Boolean comparisons and how to use then
> - [ ] about Boolean operators and how to use them
> - [ ] how to use Boolean comparison and operators to make complex conditional statements 

## Part 1: Boolean logic

<iframe width="560" height="315" src="https://www.youtube.com/embed/5GrokwhCXXM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Boolean Introduction

In programming Boolean is all about `True` and `False` values:

- Boolean variables only contain either `True` or `False`
- Comparison operators (`==`, `!=`, `>`, `<` `>=` or `<=`) return either `True` or `False`
- Boolean operators (we'll learn about these later) return either `True` or `False`

The values `True` and `False` are special values. If you type them into your IDE the syntax highlighting will indicate that they are special.

In Python testing if something is `True` or `False` is called testing the turthiness. When you compare two values, you are testing it's truthiness.

### Comparison operators

We have tested truthiness in the conditions in our `if` and `while` statements using comparison operators. Let's refresh those.

There are six comparison operators you can use. Create a new file called `lesson_6_pt_1.py` and enter the code below.

```python
print("jeff" == "jeff")  # equal to
print(1 != 1)  # not equal to
print(500 > 300)  # greater than
print(100 >= 250)  # greater than or equal to
print("a" < "q")  # less than
print(-30 <= 3)  # less than or equal to
```

PRIMM:

- **Predict** the six values that will be printed to the **Shell** (hint, they will be either `True` or `False`)
- **Run** the code and see if your predictions are correct.

It doesn't matter if the values are literals (magic numbers) or if they are stores in a variable. Change your code to the code below.

```python
score = 10
print(score > 5)
```

PRIMM:

- **Predict** if the code will print `True` or `False`
- **Run** the code and see if your prediction was correct.

### Boolean Operations

You can also complete operations on Boolean values using Boolean operators. Boolean operations are like preforming a calculation, but only with Boolean values (ie. `True` and `False`). Like all things Boolean, they return a single `True` or `False` value. They are useful for creating complex condition tests.

There are three Boolean operators:

- `and`
- `or`
- `not`

#### The `not` operator

The simplest operator to understand is the `not` operator. It simply reverses the Boolean value:

- `not True` returns `False`
- `not False` returns `True`

Change the code in your program to the code below:

```python
print("not True is:", not True)
print("not False:", not False)
```

PRIMM:

- **Predict** what you think will be written to the **Shell** when your run this code.
- **Run** the code and check your predictions.

#### The `and` operator

The `and` operator and the `or` operator are a little bit more complicated.

The `and` operators will return `True` if **all** the values in the operation are `True`.

Again, change your code so it reflects the code below:

```python
print("True and True is:", True and True)
print("True and False is:", True and False)
print("False and True is:", False and True)
print("False and False is:", False and False)
print("True and True and True is:", True and True and True)print("True and True and False is:", True and True and False)
```

PRIMM:

- **Predict** what you think will be written to the **Shell** when your run this code.
- **Run** the code and check your predictions.
- Let's **Investigate** that code

Code breakdown:

- Line `1`: `print("True and True is:", True and True)`
  - `True and True` &rarr; all values are `True` &rarr; returns `True`
  - `True and True is: True` is printed
- Line `2`: `print("True and False is:", True and False)`
  - `True and False` &rarr; not all values are `True` &rarr; returns `False`
  - `True and False is: False` is printed
- Line `3`: `print("False and True is:", True and False)`
  - `False and True` &rarr; not all values are `True` &rarr; returns `False`
  - `False and True is: False` is printed
- Line `4`: `print("False and False is:", True and False)`
  - `False and False` &rarr; not all values are `True` &rarr; returns `False`
  - `False and False is: False` is printed
- Line `5`: `print("True and True and True is:", True and True and True)`
  - `True and True and True` &rarr; all values are `True` &rarr; returns `True`
  - `True and True and True: True` is printed
- Line `6`: `print("True and True and False is:", True and True and False)`
  - `True and True and False` &rarr; not all values are `True` &rarr; returns `False`
  - `True and True and False is: False` is printed

#### The `or` operator

The `or` operator is the inverse of the `and` operator.

The `or` operator will return `True` if **any one** of the values in the operation is `True`.

Change your code so it reflects the code below:

```python
print("True or True is:", True or True)
print("True or False is:", True or False)
print("False or True is:", False or True)
print("False or False is:", False or False)
print("True or True or True is:", True or True or True)
print("True or False or False is:", True or False or False)
```

PRIMM:

- **Predict** what you think will be written to the **Shell** when your run this code.
- **Run** the code and check your predictions.
- Let's **Investigate** that code

Code breakdown:

- Line `1`: `print("True or True is:", True or True)`
  - `True or True` &rarr; at least one value is `True` &rarr; returns `True`
  - `True or True is: True` is printed
- Line `2`: `print("True or False is:", True or False)`
  - `True or False` &rarr; at least one value is `True` &rarr; returns `True`
  - `True or False is: False` is printed
- Line `3`: `print("False or True is:", True or False)`
  - `False or True` &rarr; at least one value is `True` &rarr; returns `True`
  - `False or True is: False` is printed
- Line `4`: `print("False or False is:", True or False)`
  - `False or False` &rarr; no values are `True` &rarr; returns `False`
  - `False or False is: False` is printed
- Line `5`: `print("True or True or True is:", True or True or True)`
  - `True or True or True` &rarr; at least one value is `True` &rarr; returns `True`
  - `True or True or True: True` is printed
- Line `6`: `print("True or True or False is:", True or True or False)`
  - `True or True or False` &rarr; at least one value is `True` &rarr; returns `True`
  - `True or False or False is: True` is printed

#### Using Boolean operators

So far we have just been playing around with Boolean values and returning `True` or `False` from other values of `True` and `False`. This really isn't that useful, until you remember that comparison operators return Boolean values. With Boolean operators you can create conditions with multiple comparison operator leading to complex conditions for your `if` and `while` statements.

Consider the following code:

```python
print(7 < 8 and "a" < "o")
```

PRIMM:

- **Predict** what you think will be written to the **Shell** when your run this code.
- **Run** the code and check your predictions.
- Let's **Investigate** that code

Code breakdown:

- Line `1`: `print(7 < 8 and "a" < "o")`
  - first Python will complete the comparison operations from left to right
    - `7 < 8` returns `True`
    - `"a" < "o"` returns `True`
  - the code is now: `print(True and True)`
    - `True and True` returns `True`
  - Python prints `True` to the **Shell**

> **Combining multiple comparison operations**
>
> If you are going to use Boolean operations to create conditions that contain multiple comparisons, you need to have a comparison on both sides of the Boolean operations.
>
> `10 > 5 and 10 > 13` is not the same as `10 > 5 and 13`.

## Part 2: Mouse input in Turtle

To reinforce our understanding of Boolean logic, we are going to do something new with Turtle. So far we have only accepted user input via the **Shell**, but Turtle can also use mouse input (and keys as well).

We are going to use the code below for our Boolean exercise, but we will have to explore some code first.

Create a new file and call it **lesson_6_pt_2.py** then add the code below.

```python
import turtle

## Prepare the windows and turtle ##
def set_scene():
    turtle.setup(800, 600)

    ## Respond to mouse click (signal) ##
    turtle.onscreenclick(draw_dot)

    ## Set up the grid ##
    my_ttl.speed(0)
    for i in range(4):
        my_ttl.forward(400)
        my_ttl.back(400)
        my_ttl.right(90)
    my_ttl.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
    print(x, y)
    dot_colour = "orange"
    dot_size = 10
    my_ttl.goto(x, y)
    my_ttl.dot(dot_size, dot_color)


## Main Program
my_ttl = turtle.Turtle()
set_scene()
my_ttl.hideturtle()
```

- **Predict** what you think will be written to the **Shell** when your run this code.
- **Run** the code and check your predictions.
- Let's **Investigate** that code.

The code is in three sections, so let's look at them in the order they are executed:

- Lines `29` to `31`: the main program
  - Line `29`: `my_ttl = turtle.Turtle()` &rarr; create a Turtle object and names it `my_ttl`
  - Line `30`: `set_scene()` calls the `set_scene()` function
  - Line `31`: `my_ttl.hideturtle()` make the turtle invisible
- Lines `4` to `16`: the `set_scene` function
  - Line `4`: `def set_scene()` &rarr; defines the `set_scene` function without any arguments
  - Line `5`: `turtle.setup(800, 600)` &rarr; creates a `800` x `600` window
  - Line `8`: `turtle.onscreenclick(draw_dot)` &rarr; this is **new**
    - if a mouse click is detected:
      - calls the `draw_dot` function
      - passes to the `draw_dot` function the `x` and `y` coordinates of where the mouse clicked
  - Line `11`: `my_ttl.speed(0)` &rarr; a turtle speed of `0` means you don't see the turtle move
  - Lines `12` to `15`: draws four lines from `(0, 0)` making the four quadrants
  - Line `16`: `penup` prevents the turtle from drawing a line to the mouse click coordinates (try commenting it out and see what happens)
- Lines `20` to `25`: the `draw_dot` function
  - Line `20`: `def draw_dot(x, y):`
    - defines the `draw_dot` function
    - accepts the two arguments `x` and `y` which are passed from line `8`
    - `turtle.onscreenclick()` always passes the `x` and `y` coordinates as arguments
  - Line `21`: prints the `x` and `y` coordinates to the **Shell** (to help you plan your code)
  - Line `22`: assigns `"orange"` to the variable `dot_colour`
  - Line `23`: assigns `10` to the variable `dot_size`
  - Line `24`: sends the turtle to the `x` and `y` coordinates
  - Line `25`: `my_ttl.dot(dot_size, dot_color)` draws a dot at the turtle position of size `dot_size` and colour `dot_colour`
  
## Exercises

In this course, the exercises are the **make** component of the PRIMM model. So work through the following exercises and make your own code.

So far the dot colour is always orange. In these exercises you will change the colour of the dot depending on which quadrant the mouse clicks.

To do this your will need to use:

- `if` ... `elif` ... `else` statements
- Boolean comparisons
- Boolean operations

### Exercise 1

Create a new file and save it in your subject folder calling it **lesson_6_ex_1.py**. Then type the following code into it.

``` python
import turtle

## Prepare the windows and turtle ##
def set_scene():
    turtle.setup(800, 600)

    ## Respond to mouse click (signal) ##
    turtle.onscreenclick(draw_dot)

    ## Set up the grid ##
    my_ttl.speed(0)
    for i in range(4):
        my_ttl.forward(400)
        my_ttl.back(400)
        my_ttl.right(90)
    my_ttl.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
    print(x, y)
    dot_colour = "orange"

    ##################################
    ######## Answer goes here ########
    ##################################
    """ Part A
    Use an 'if' statement to set the dot color to red
    when the mouse clicks in the top right quadrant

    You can determine the position using the variables
    x and y

    To change the colour of the dot to red, run the command

    dot_color = 'red'

    """

    ##################################
    ##################################
    ##################################

    my_ttl.goto(x, y)
    dot_size = 10
    my_ttl.dot(dot_size, dot_color)


my_ttl = turtle.Turtle()
set_scene()
my_ttl.hideturtle()
```

Follow the instructions in the comments from line `24` to line `42`.

### Exercise 2

Create a new file and save it in your subject folder calling it **lesson_6_ex_2.py**. Then type the following code into it.

```python
import turtle

## Prepare the windows and turtle ##
def set_scene():
    turtle.setup(800, 600)

    ## Respond to mouse click (signal) ##
    turtle.onscreenclick(draw_dot)

    ## Set up the grid ##
    my_ttl.speed(0)
    for i in range(4):
        my_ttl.forward(400)
        my_ttl.back(400)
        my_ttl.right(90)
    my_ttl.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
    print(x, y)
    dot_color = "orange"
    
    ##################################
    ######## Answer goes here ########
    ##################################
    """ Part B
    Use both 'if' and 'else' to set the dot color to red
    if the mouse is clicked in the top right quadrant and
    green if clicked anywhere else
    """

    ##################################
    ##################################
    ##################################

    my_ttl.goto(x, y)
    dot_size = 10
    my_ttl.dot(dot_size, dot_color)


my_ttl = turtle.Turtle()
set_scene()
my_ttl.hideturtle()
```

Follow the instructions in the comments from line `25` to line `36`.

### Exercise 3

Create a new file and save it in your subject folder calling it **lesson_6_ex_3.py**. Then type the following code into it.

``` python
import turtle

## Prepare the windows and turtle ##
def set_scene():
    turtle.setup(800, 600)

    ## Respond to mouse click (signal) ##
    turtle.onscreenclick(draw_dot)

    ## Set up the grid ##
    my_ttl.speed(0)
    for i in range(4):
        my_ttl.forward(400)
        my_ttl.back(400)
        my_ttl.right(90)
    my_ttl.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
    print(x, y)
    dot_color = "orange"

    ##################################
    ######## Answer goes here ########
    ##################################
    """ Part C
    Use 'if', 'elif' and 'else' keywords to set the dot color to
    red when the mouse is clicked in the top right quadrant,
    blue in the top left quadrant, yellow in the bottom left quadrant
    and green in the bottom right quadrant
    """

    ##################################
    ##################################
    ##################################

    my_ttl.goto(x, y)
    dot_size = 10
    my_ttl.dot(dot_size, dot_color)


my_ttl = turtle.Turtle()
set_scene()
my_ttl.hideturtle()
```

Follow the instructions in the comments from line `24` to line `36`.
