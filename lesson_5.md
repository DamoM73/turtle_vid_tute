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
window.setup(screen,screen)

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
window.setup(screen,screen)

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
window.setup(screen,screen)

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
- line `29` - `print("Invalid input")` &rarr; informs user of their mistake
- line `30` - `quit()` &rarr; exits the program

### Refactor Code - DRY

Looking at our code, does it pass the DRY test?

The `# get user input` section from line `17` to `30` definitely has repeatition in it. Twice the code:

1. asks the user for input
2. checks if that input is all numbers
3. either converts or quits the program depending on the `if` statement.

During all this the only part of the code that differs is:

- line `18` and `25` the `input` prompt is different:
  - line `18` &rarr; `"How many sides?> "`
  - line `25` &rarr; `"How long are the sides?> "`
- in the respectice section different variable names are used:
  - lines `18` to `23` &rarr; `num_sides`
  - lines `25` to `30` &rarr; `size`

This looks like a prefect opportunity to *refactor* the code using a function.

> **Refactoring**
>
> *Refactoring* is the computer science term for changing your code **without changing the way it works**. This is normally done to make code more efficient or more maintainable.
>
> - effienct code uses less computing resources (processing power, storage, internet bandwidth etc.)
> - maintainable code is easier for programmers to understand, and therefore easier to fix, update and enhance.

To refactor our code we need add the following function at line `8` of your code:

``` python
def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()
```

Then remove the code under `# get user input` from lines `17` to `30`, and replace it with two calls to the function;

``` python
# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
```

In the end your code should look like the below:

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
window.setup(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")

draw_poly(size,num_sides)
```

It is really important, when you refactor code, to ensure that the code still works the same as it did before you refactored. So run the code to ensure that it still works the same way. Remeber to test all 4 possible branches:

- valid `sides` value and valid `size` value
- valid `sides` value and invalid `size` value
- invalid `sides` value and valid `size` value
- invalid `sides` value and invalid `size` value

If your code still works as it should, lets unpack the code we just added:

- the `get_number` function:
  - `def get_number(prompt):` &rarr; defines our new function with one argument `prompt`:
    - we observed that the prompt was one of the differnces between our two blocks of simlar code
    - we can provide a different prompt each time we call the function
  - `num = input(prompt)` &rarr; uses the `prompt` argument and assigns the user input to `num`
  - `if num.isdigit():` &rarr; checks if `num` only contains numbers
  - `return int(num)` &rarr; converts the value assigned to `num` then `returns` to the main program:
    - `return` is new
    - `return` sends a value back to the main program and then finishes the function.
  - `else:` &rarr; if `num` does not only contain numbers, run the following code
  - `print("Invalid input")` &rarr; informs the user their input is not correct
  - `quit()` &rarr; exits the program
- `num_sides = get_number("How many sides?> ")` &rarr; calls the `get_number` function
  - `get_number()` &rarr; calls the function
  - `"How many sides?> "` &rarr; provides the prompt string to the function
  - `num_sides =` takes the value returned by the function and assigns it to `num_sides`
- `size = get_number("How long are the sides?> ")` &rarr; calls the `get_number` function
  - `get_number()` &rarr; calls the function
  - `"How long are the sides?> "` &rarr; provides the prompt string to the function
  - `size =` takes the value returned by the function and assigns it to `size`

### Playing with colour

Let's keep adding features to our program. Turtle allows you to also change the colour of your shapes and lines using the method `color()`:

`color()` accepts two arguments:

- first argument &rarr; line colour
- second argument &rarr; fill colour

> **Spelling**
>
> Like most programming languages, Python uses US spelling. Using Australian spelling (eg. colour) will generate an error.
>
> It up to the programmer to decide what spelling to follow in your naming of variables and functions. I choose to use the US spelling. This means all the code uses the same spelling and therefore reduce the likelihood of errors.

Now let's change the colour of our shape.

Make the changes in code the code below to:

- line `3`
- line `4`
- line `32`

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
window.setup(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")

draw_poly(size,num_sides,"red")
```

PRIMM

- *Predict* what you think will happen when you run the code:
- *Run* the code. Did it follow your prediction?
- Let's *investigate* that code.

Breakdown of our code changes:

- `def draw_poly(length, sides, color):` &rarr; accepts a third argument `color`
- `myttl.color("black",color)` &rarr; sets the turtle color
  - line colour &rarr; `"black"` 
  - fill colour &rarr; the value in the `color` argument

> **Turtle colours**
>
> Turtle allows the use of named colours. [Here is a list of all the named colours](https://cs111.wellesley.edu/labs/lab02/colors).

Now that we can change colour, can we let the user choose between `red`, `blue` and `green` for the fill colour?

We will need to capture the error when the user enters anythin other than `"red"`, `"blue"` or `"green"`, so that's means using an `if` statement. But the `if` / `else` statement only allows two brnaces, as we need to have three.

To choos between three or more branches we need to learn about the last part of the `if` statement: `elif`.

### `if` `elif` `else` statements

The `elif` statement is effectively a `else` + `if` statement and allows branching between multiple blocks of code. The best way to explpore this is by using it in our code.

Create a function so the user can choose between `red`, `blue` and `green` for the fill colour.

Adjust your code so it is the same as the code below. Changes are on:

- lines `19` to `29`
- line `43`
- line `45`

``` python
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
window.setup(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(size,num_sides, fill)
```

PRIMM

- *Predict* what you think will happen when you run the code:
- *Run* the code. Did it follow your prediction?
- Let's *investigate* that code.

There are a few new concepts for us to breakdown:

- line `20` - `color = input("Fill colour (red, blue, green)?> ").lower()` &rarr; `lower()` is new
  - `lower()` is another string method
  - it converts all the letters in a string to their lowercase version
- line `21` - `if color == "red":` &rarr; tests if the user inputed `"red"`
- line `22` - `return color`
  - sends the value of `color` (in this case `"red"` back to the main program)
  - ends the function
- line `23` - `elif color == "blue":`
  - is only executed if the condition in line `21` is `False`
  - checks if the value of `color` is `"blue"`
- line `24` - `return color`
  - sends the value of `color` (in this case `"blue"` back to the main program)
  - ends the function
- line `25` - `elif color == "green":`
  - is only executed if the conditions in line `21` and line `23` are both `False`
  - checks if the value of `color` is `"green"`
- line `26` - `return color`
  - sends the value of `color` (in this case `"green"` back to the main program)
  - ends the function
- line `27` - `else:`
  - is only executed if the conditions in line `21`, line `23` and line `24` are all `False`
- line `28` and line `29` are the same as the `get_number()` function

The `if` / `elif` / `else` statement very useful and flexiable. You will use it in various configurations, so let look at it's rules.

> **`if` / `elif` / `else` structure**
> 
> The structure of a full `if` / `elif` / `else` statement is:
>
> - the `if` component
>   - always at the beginning of an `if` / `elif` / `else` statement
>   - the only compulsary part
>   - there can only be one per `if` / `elif` / `else` statement
> - the `elif` component
>   - must come after the `if` statement and before the `else` statement
>   - is optional
>   - there can be as many `elif` components as you wish
>   - is only accessed when all the conditions before it are `False` and its condition is `True`
> - the `else` componet
>   - must be at the end of an an `if` / `elif` / `else` statement
>   - is optional
>   - there can only be one per `if` / `elif` / `else` statement
>   - is only accessed when all the conditions before it are `False`

## Part 2 Exercise

In this course, the exercises are the *make* component of the PRIMM model. So work through the following exercises and *make* your own code.

### Exercise 1

Create a new file and save it in your subject folder calling it **lesson_5_ex_1.py**. Then type the following code into it.

```python
# Almyttl's security guard program

#####################################################
## Write a program that asks for a person's name   ##
## and then grants entry of that person is Almyttl ##
## everyone else is told, politely, to go away     ##
#####################################################

```

Follow the instructions in the comments and use your Python knowledge to create a password checker. Remember to apply the DRY principle

### Exercise 2

Create a new file and save it in your subject folder calling it **lesson_5_ex_2.py**. Then type the following code into it.

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

Follow the instructions in the comments and use your Python knowledge to create an enhanced password checker. Remember to apply the DRY principle

### Exercise 3

Create a new file and save it in your subject folder calling it **lesson_5_ex_3.py**. Then type the following code into it.

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
window.setup(screen,screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(size,num_sides, fill)
```

Follow the instructions in the comments (check line `37`) and use your Python knowledge to enhance our shape drawing code. Remember to apply the DRY principle.


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
window.setup(screen,screen)

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

