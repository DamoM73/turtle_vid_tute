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
- Boolean comparisons (`==`, `!=`, `>`, `<` `>=` or `<=`) return either `True` or `False`
- Boolean operations (we'll learn about these later) return either `True` or `False`

The values `True` and `False` are special values. If you type them into your IDE the syntax highlight will tell you indicate they are special.

In Python testing if something is `True` or `False` is called testing the Turthiness. When you compare two values, you are testing it's truthiness.

### Boolean Comparisons

We have tested truthiness in the conditions in our `if` and `while` statements using Boolean comparisons. Let's refresh those.

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

- *Predict* the six values that will be printed to the **Shell** (hint, they will be either `True` or `False`)
- *Run* the code and see if your predictions are correct.

It doesn't matter if the values are literals (magic numbers) or if they are stores in a variable. Change your code to the code below.

```python
score = 10
print(score > 5)
```

PRIMM:

- *Predict* if the code will print `True` or `False`
- *Run* the code and see if your prediction was correct.

### Boolean Operations

You can also do operations on Boolean values using Boolean operators. Boolean operations are like preforming a calculation with only Boolean values (ie. `True` and `False`). Like all things Boolean, they return as single `True` or `False` value. They are really useful for creating complex condition tests.

There are three Boolean operators:

- `and`
- `or`
- `not`


#### The `not` operator

The simplest operator to understand is the `not` operator. It simply reverses the Boolean value:

- `not True` &rarr; `False`
- `not False` &rarr; `True`

Change the code in your program to the code below

```python
print("not True is:", not True)
print("not False:", not False)
```

PRIMM:

- *Predict* what you think will be written to the **Shell** when your run this code.
- *Run* the code and check your predictions.

#### The `and` operator

The `and` operator and the `or` operator are a little bit more complicated.

The `and` operators will return `True` if **all** the values in the operation are `True`.

Again, change your code so it reflects the code below.

```python
print("True and True is:", True and True)
print("True and False is:", True and False)
print("False and True is:", False and True)
print("False and False is:", False and False)
print("True and True and True is:", True and True and True)
print("True and True and False is:", True and True and False)
```

PRIMM:

- *Predict* what you think will be written to the **Shell** when your run this code.
- *Run* the code and check your predictions.
- Let's *Investigate* that code

Code breakdown:

- line `1`: `print("True and True is:", True and True)`
  - `True and True` &rarr; all values are `True` &rarr; `True`
  - `True and True is: True` is printed
- line `2`: `print("True and False is:", True and False)`
  - `True and False` &rarr; not all values are `True` &rarr; `False`
  - `True and False is: False` is printed
- line `3`: `print("False and True is:", True and False)`
  - `False and True` &rarr; not all values are `True` &rarr; `False`
  - `False and True is: False` is printed
- line `4`: `print("False and False is:", True and False)`
  - `False and False` &rarr; not all values are `True` &rarr; `False`
  - `False and False is: False` is printed
- line `5`: `print("True and True and True is:", True and True and True)`
  - `True and True and True` &rarr; all values are `True` &rarr; `True`
  - `True and True and True: True` is printed
- line `6`: `print("True and True and False is:", True and True and False)`
  - `True and True and False` &rarr; not all values are `True` &rarr; `False`
  - `True and True and False is: False` is printed

#### The `or` operator

The `or` operator is the inverse of the `and` operator.

The `or` operator will return `True` if just one of the values in the statement is `True`.

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

- *Predict* what you think will be written to the **Shell** when your run this code.
- *Run* the code and check your predictions.
- Let's *Investigate* that code

Code breakdown:

- line `1`: `print("True or True is:", True or True)`
  - `True or True` &rarr; at least one value is `True` &rarr; `True`
  - `True or True is: True` is printed
- line `2`: `print("True or False is:", True or False)`
  - `True or False` &rarr; at least one value is `True` &rarr; `True`
  - `True or False is: False` is printed
- line `3`: `print("False or True is:", True or False)`
  - `False or True` &rarr; at least one value is `True` &rarr; `True`
  - `False or True is: False` is printed
- line `4`: `print("False or False is:", True or False)`
  - `False or False` &rarr; no values are `True` &rarr; `False`
  - `False or False is: False` is printed
- line `5`: `print("True or True or True is:", True or True or True)`
  - `True or True or True` &rarr; at least one value is `True` &rarr; `True`
  - `True or True or True: True` is printed
- line `6`: `print("True or True or False is:", True or True or False)`
  - `True or True or False` &rarr; at least one value is `True` &rarr; `True`
  - `True or False or False is: True` is printed

#### Using Boolean operators

So far we have just been playing around with Boolean values and deriving `True` or `False` from other values of `True` and `False`. This really isn't that useful, until you remember that comparison operators return Boolean values. Then you can start using Boolean operators to combine comparison operations and create more complex conditions for your `if` and `while` statements.

Consider the following code:

```python
print(7 < 8 and "a" < "o")
```

PRIMM:

- *Predict* what you think will be written to the **Shell** when your run this code.
- *Run* the code and check your predictions.
- Let's *Investigate* that code

Code breakdown:

- line `1`: `print(7 < 8 and "a" < "o")`
  - first Python will complete the comparison operations from left to right
    - `7 < 8` &rarr; `True`
    - `"a" < "o"` &rarr; `True`
  - the code is now: `print(True and True)`
    - `True and True` &rarr; `True`
  - Python prints `True` to the **Shell**

## Part 2: Mouse input in Turtle

To reinforce our understanding of Boolean logic, we are going to do something new with Turtle. So far we have only use the terminal for user input, but Turtle can also use mouse input (and keys as well).

We are going to use the code below for our Boolean exercise, but we will have to explore the code first.

Create a new file and call it **lesson_6_ex_0.py** then add the code below.

### Introduce the homework task

```python
import turtle

## Prepare the windows and turtle ##
def set_scene():
    turtle.setup(800, 600)

    ## Respond to mouse click (signal) ##
    turtle.onscreenclick(draw_dot)

    ## Set up the grid ##
    driver.speed(0)
    for i in range(4):
        driver.forward(400)
        driver.back(400)
        driver.right(90)
    driver.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
    print(x, y)
    dot_colour = "orange"
    dot_size = 10
    driver.goto(x, y)
    driver.dot(dot_size, dot_color)


## Main Program
driver = turtle.Turtle()
set_scene()
driver.hideturtle()
```

- *Predict* what you think will be written to the **Shell** when your run this code.
- *Run* the code and check your predictions.
- Let's *Investigate* that code

The code is in three sections, so let's look at them in the order they are executed:

- lines `26` to `29`: the main program
  - line `27`: `driver = turtle.Turtle()` &rarr; create a Turtle object and names it `driver`
  - line `28`: `set_scene()` calls the `set_scene()` function
  - line `29`: `driver.hideturtle()` make the turtle invisible
- lines `4` to `16`: the `set_scene()` function
  - line `4`: `def set_scene()` &rarr; defines the `set_scene()` function without any arguments
  - line `5`: `turtle.setup(800, 600)` &rarr; creates a `800` x `600` window
  - line `8`: `turtle.onscreenclick(draw_dot)` &rarr; this is **new**
    - if a mouse click is detected:
      - call the `draw_dot` function
      - pass the `draw_dot` function the `x` and the `y` coordinates of the mouse click
  - line `11`: `driver.speed(0)` &rarr; a turtle speed of `0` means you don't see the turtle move
  - lines `12` to `15`: draws four lines from `(0, 0)` making the four quadrants
  - line `16`: `penup` prevents turtle drawing line to the mouse click coordinates (try commenting it out and see what happens)
- lines `19` to `24`: the `draw_dot()` function
  - line `19`: `def draw_dot(x, y):`
    - defines the `draw_dot()` function
    - accepts the two arguments `x` and `y` which are passed from line `8`: `turtle.onscreenclick(draw_dot)`
    - `turtle.onscreenclick()` always passes the `x` and `y` coordinates as arguments
  - line `20`: prints the `x` and `y` coordinates to the **Shell**. This is to help your plan your code
  - line `21`: assigns `"orange"` to the variable `dot_colour`
  - line `22`: assigns `10` to the variable `dot_size`
  - line `23`: sends the turtle to the `x` and `y` coordinates
  - line `24`: `driver.dot(dot_size, dot_color)` draws a dot at the turtle position of size `dot_size` and colour `dot_colour`
  
## Exercises

In this course, the exercises are the *make* component of the PRIMM model. So work through the following exercises and *make* your own code.

So far the dot colour is always orange. In these exercises you will change the colour of the dot depending on which quadrant the mouse clicks.

To do this your will need to use:

- `if` / `elif` / `else` statements
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
    driver.speed(0)
    for i in range(4):
        driver.forward(400)
        driver.back(400)
        driver.right(90)
    driver.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
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

    driver.goto(x, y)
    dot_size = 10
    driver.dot(dot_size, dot_color)


driver = turtle.Turtle()
set_scene()
driver.hideturtle()
```

Follow the instructions in the comments from line `22` to line `40`.

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
    driver.speed(0)
    for i in range(4):
        driver.forward(400)
        driver.back(400)
        driver.right(90)
    driver.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
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

    driver.goto(x, y)
    dot_size = 10
    driver.dot(dot_size, dot_color)


driver = turtle.Turtle()
set_scene()
driver.hideturtle()
```

Follow the instructions in the comments from line `22` to line `35`.

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
    driver.speed(0)
    for i in range(4):
        driver.forward(400)
        driver.back(400)
        driver.right(90)
    driver.penup()


## Reaction to signal (slot) ##
def draw_dot(x, y):
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

    driver.goto(x, y)
    dot_size = 10
    driver.dot(dot_size, dot_color)


driver = turtle.Turtle()
set_scene()
driver.hideturtle()
```

Follow the instructions in the comments from line `22` to line `35`.
