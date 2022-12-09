# Python Turtle - Lesson 5

> **Topics**
> In this lesson you will learn:
>
> - [ ] How to capturing errors
> - [ ] About the branching control structure (if statements)
> - [ ] How and when to use if statements

## Part 1: Branching

<iframe width="560" height="315" src="https://www.youtube.com/embed/fGEz4QNXpEE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Branching control structure

Branching is the control structure that allows the program's flow it take alternative paths. Let's use a practical example to better understand this.

Open the file **lesson_4_pt_2.py** then save it as **lesson_5_pt_1a.py**

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

num_sides = int(input("How many sides?> "))
size = int(input("How long are the sides?> "))

draw_poly(size,num_sides)
```
Run the program, and at the prompt, instead of providing a number, provide a word like, for example `dog`

This will raise the following error:

```
Traceback (most recent call last):
  File "<string>", line 17, in <module>
ValueError: invalid literal for int() with base 10: 'dog'
```

This error occurs because in line `17` we are trying to convert the literal (string) `dog` into an integer. Since `dog` is not a whole number, it causes an error.

What we need to do is check if the user has entered a whole number before converting it into an integer.

Create a new file in, enter the code below then save it as **lesson_5_pt_1b.py**.

```python
user_value = input("Enter a number: ")

print(user_value.isdigit())
```

PRIMM:

- *Predict* what you think will happen when you run the code twice:
  - first time enter the value `10`
  - second time enter the value `dog`
- *Run* the code. Did it follow your prediction?
- Let's *investigate* that code.

Remember that Python inputs are strings. Strings have special operations called *methods*. One of those is the `isdigit()` method. `isdigit()` returns the Boolean value of `True` if all characters in a string are digits.

> **String Methods**
>
> Python has many useful string methods. If you are interested in exploring them [W3Schools' Python String Methods](https://www.w3schools.com/python/ref_string_isdigit.asp) is a good place to start.

We can tell if the user's input is a number or not. Now we just need to tell the computer how to respond to this information.

### `if` statements

Adjusts your code so it is the same as the code below:

```python
user_value = input("Enter a number: ")

if user_value.isdigit():
    print("Yes that is a number")
```

PRIMM

- Again *Predict* what you think will happen when you run the code twice:
  - first time enter the value `10`
  - second time enter the value `dog`
- *Run* the code. Did it follow your prediction?
- Let's *investigate* that code.

Code breakdown:

- line `3`: `if user_value.isdigit():`
  - this is the definition of an `if` statement.
  - the `if` tells Python that this is an `if` statement
  - the next part is called a *conditional*
    - conditions are operations that return a Boolean value (`True` or `False`)
    - this *conditional* is `user_value.isdigit()`
    - we already know how this responds from our previous work
      - `10` &rarr; `True`
      - `dog` &rarr; `False`
  - ends with `:`
    - this is the same as with `for` loops and functions, it indicates that an indented code block follows.
  - the indented code block, will only run if the condition is `True`. In our example:
    - `10` &rarr; `user_value.isdigit()` is `True` &rarr; run indented code block
    - `dog` &rarr; `user_value.isdigit()` is `False` &rarr; don't run indented code block
- line `4`: `print("Yes that is a number")`
  - the idented code block that will run if `user_value.isdigit()` is `True`

This is awesome, we can now respond to a digit being entered. But what if we want to provide a different response when `user_value.isdigit()` is `False`?

### `if` `else` statements

Adjust your code by adding lines `5` and `6` in the code below:

```python
user_value = input("Enter a number: ")

if user_value.isdigit():
    print("Yes that is a number")
else:
    print("Silly, that is not a number")
```

PRIMM

- Again *Predict* what you think will happen when you run the code twice:
  - first time enter the value `10`
  - second time enter the value `dog`
- *Run* the code. Did it follow your prediction?
- Let's *investigate* that code.

Code breakdown:

- lines `3` and `4` operate the same as previously
- line `5` - `else:`
  - `else` uses the `if` statement's condition. 
  - in this case it is saying if `user_value.isdigit()` is not `True` then run the following indented block code
  - `:` tells Python that an indented code block follows
- line `6` - `print("Silly, that is not a number")`
  - the idented code block that will run if `user_value.isdigit()` is not `True`

To really check out what is happening here run through the code again, using our `10` and `dog` values, but this time step through the code with the **debugger**.

### Use `if` and `else` to capture errors

Go back to **lesson_5_pt_1a.py** and adjust the code by replacing line `17` with the following code:

``` python
# get user input
num_sides = input("How many sides?> ")
if num_sides.isdigit():
    num_sides = int(num_sides)
else:
    print("Invalid input")
    quit()
```

Your code should look like the code below:

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = input("How many sides?> ")
if num_sides.isdigit():
    num_sides = int(num_sides)
else:
    print("Invalid input")
    quit()
    
size = input("How long are the sides?> ")

draw_poly(size,num_sides)
```

Then replace line `25` with this code:

``` python
size = input("How long are the sides?> ")
if size.isdigit():
    size = int(size)
else:
    print("Invalid input")
    quit()
```

Your code should look like the code below:

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = input("How many sides?> ")
if num_sides.isdigit():
    num_sides = int(num_sides)
else:
    print("Invalid input")
    quit()

size = input("How long are the sides?> ")
if size.isdigit():
    size = int(size)
else:
    print("Invalid input")
    quit()

draw_poly(size,num_sides)
```

Let's test this code to see if it works.

PRIMM

- *Predict* what you think will happen when you run the code in the following scenarios:
  - valid `sides` value and valid `size` value
  - valid `sides` value and invalid `size` value
  - invalid `sides` value and valid `size` value
  - invalid `sides` value and invalid `size` value
- *Run* the code. Did it follow your prediction?
- Let's *investigate* that code.

> **Testing tips:**
>
> - when testing branching code you need to test all possible paths.
> - test `if` statements for both `True` conditions and `False` conditions
> - our code had four possible branches so we needed to test all four of them

Code breakdown:

- line `17` - `# get user input` &rarr; a comment used to structure the code
- line `18` - `num_sides = input("How many sides?> ")` &rarr; accepts user input and assigns it to `num_sides`
- line `19` - `if num_sides.isdigit():` &rarr; tests if `num_sides` only contains numbers
  - if `num_sides.isdigit()` is `True` then run the code block in line `20`
- line `20` - `num_sides = int(size)` takes the value assigned to `num_sides` converts it to an integer, then reassigns it to `num_sides`
- line `21` - `else:` &rarr; if `num_sides` is not all numbers execute following code block (lines `22` to `23`)
- line `22` - `print("Invalid input")` &rarr; informs user of their mistake
- line `23` - `quit()` &rarr; exits the program
- line `25` - `size = input("How long are the sides?> ")` &rarr; accepts user input and assigns it to `size`
- line `26` - `if size.isdigit():` &rarr; tests if `size` only contains numbers
  - if `size.isdigit()` is `True` then run the code block in line `27`
- line `27` - `size = int(size)` takes the value assigned to `size` converts it to an integer, then reassigns it to `size`
- line `28` - `else:` &rarr; if `size` is not all numbers execute following code block (lines `29` to `30`)
- line `22` - `print("Invalid input")` &rarr; informs user of their mistake
- line `23` - `quit()` &rarr; exits the program



Now, does this pass the dry test?

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)
        
def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()
        
# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")

draw_poly(size,num_sides)
```

### Introduce `if` `elif` `else` statements

What if we want to colour our shape?

```python
import turtle

def draw_poly(length, sides, color):
    myttl.color("black",color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)
    myttl.end_fill()
        
def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()
        
# setup window
screen = 500
window = turtle.Screen() 
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")

draw_poly(size,num_sides,"red")
```

Can we let the user choose the colour

```python
import turtle

def draw_poly(length, sides, color):
    myttl.color("black",color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)
    myttl.end_fill()
        
def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()
        
def get_color():
    color = input("Fill colour (red, blue, green)?> ").lower()
    if color == "red":
        return color
    elif color == "blue":
        return color
    elif color == "green":
        return color
    else:
        print("Invalid input")
        quit()
        
# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(size,num_sides, fill)
```

### Exercises

#### L5_Ex1.py

```python
# Almyttl's security guard program

#####################################################
## Write a program that asks for a person's name   ##
## and then grants entry of that person is Almyttl ##
## everyone else is told, politely, to go away     ##
#####################################################

```

#### L5_Ex2.py

``` python
# Almyttl's security guard program

friends = "Bruce"

#####################################################
## Write a program that asks for a person's name   ##
## and then grants entry of that person is Almyttl  ##
## or a friend of Almyttl.                          ##
## Everyone else is told, politely, to go away     ##
#####################################################

```

#### L5_Ex3.py

```python
import turtle

#####################################################
## Adjust the code below to allow the user to      ##
## choose the coordinates where the shape is drawn ##
#####################################################

def draw_poly(length, sides, color):
    myttl.color("black",color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)
    myttl.end_fill()
        
def get_number(prompt):
    num = input(prompt)
    if num.lstrip("-").isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()
        
def get_color():
    color = input("Fill colour (red, blue, green)?> ").lower()
    if color == "red":
        return color
    elif color == "blue":
        return color
    elif color == "green":
        return color
    else:
        print("Invalid input")
        quit()

def move_pen():
    # write your code here to get coordinates from user #

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(size,num_sides, fill)
```



## Tutorial 2: While Loop

### Number guessing game

See if the user can guess a random number

#### Introduce `random.randint`

```python
import random

def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()

number = random.randint(1,100)

guess = get_number("Guess a number between 1 and 100> ")

if guess == number:
    print("Correct!")
else:
    print("Incorrect. The number was", number)
```

What would make this more fun? More than one guess! How can we do that?

```python
import random

def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()

number = random.randint(1,100)

print("You have 10 turns to guess a number between 1 and 100")

for turn in range(10):
    guess = get_number("Guess a number between 1 and 100> ")

    if guess == number:
        print("Correct!")
    else:
        print("Incorrect. Try again")

print("The number was", number)
```

How about giving hints?

```python
import random

def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()

number = random.randint(1,100)

print("You have 10 turns to guess a number between 1 and 100")

for turn in range(10):
    guess = get_number("Guess a number between 1 and 100> ")

    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("Correct!")

print("The number was", number)
```

Problem when we get the answer correct.

#### Introduce `while` loop

Think of playing cards.

- Dealing poker -  how many times does the loop run?
- Dealing snap - how many times do you loop?

`for` loop is count controlled - we know how many times to run it.

`while` loop is condition controlled - we don't know how many times to run it.

```python
import random

def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()

number = random.randint(1,100)

guess = 0

while guess != number:
    guess = get_number("Guess a number between 1 and 100> ")

    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("Correct!")

print("The number was", number)
```

What happens with a typo putting numbers in?

```python
import random

def get_number(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid input")
            
number = random.randint(1,100)

guess = 0

while guess != number:
    guess = get_number("Guess a number between 1 and 100> ")

    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("Correct!")

print("The number was", number)
```

### Exercises

#### L5_Ex4.py

``` python
import turtle

def draw_poly(length, sides, color):
    myttl.color("black",color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360/sides)
    myttl.end_fill()

############################################
## adjust the get_number code so it loops ##
## until the user provides a valid input  ##
############################################

def get_number(prompt):
    num = input(prompt)
    if num.lstrip("-").isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()

###########################################
## adjust the get_color code so it loops ##
## until the user provides a valid input ##
###########################################

def get_color():
    color = input("Fill colour (red, blue, green)?> ").lower()
    if color == "red":
        return color
    elif color == "blue":
        return color
    elif color == "green":
        return color
    else:
        print("Invalid input")
        quit()
        
def move_pen():
    x_val = get_number("x axis position?> ")
    y_val = get_number("y axis position?> ")
    myttl.penup()
    myttl.goto(x_val,y_val)
    myttl.pendown()
    
# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

move_pen()
draw_poly(size,num_sides, fill)
```

