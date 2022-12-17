# Python Turtle - Lesson 5

> **Topics**
> In this lesson you will learn:
>
> - [ ] how to capturing errors
> - [ ] what are branching control structures (`if` statements) 
> - [ ] how and when to use `if` / `elif` / `else` in Python
> - [ ] the difference between definite and indefinite iteration
> - [ ] how and when to use `where` loops in Python
> - [ ] how to generate random numbers in Python

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
        myttl.right(360 / sides)


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

num_sides = int(input("How many sides?> "))
size = int(input("How long are the sides?> "))

draw_poly(size, num_sides)
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
        myttl.right(360 / sides)


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

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

draw_poly(size, num_sides)
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
        myttl.right(360 / sides)


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

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

draw_poly(size, num_sides)
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
        myttl.right(360 / sides)


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
window.setup(screen, screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")

draw_poly(size, num_sides)
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
    myttl.color("black", color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360 / sides)
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
window.setup(screen, screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")

draw_poly(size, num_sides, "red")
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
    myttl.color("black", color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360 / sides)
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
window.setup(screen, screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(size, num_sides, fill)
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

## Part 1 Exercises

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

``` python
import turtle

#####################################################
## Adjust the code below to allow the user to      ##
## choose the coordinates where the shape is drawn ##
#####################################################


def draw_poly(length, sides, color):
    myttl.color("black", color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360 / sides)
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
window.setup(screen, screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(size, num_sides, fill)
```

Follow the instructions in the comments (check line `37`) and use your Python knowledge to enhance our shape drawing code. Remember to apply the DRY principle.

## Tutorial 2: While Loop

<iframe width="560" height="315" src="https://www.youtube.com/embed/A9j7N6kLL1U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In Python we have two form of iteration. We have already looked at the `for` loop, and in the section we will look at the other iteration control structure, the `while` loop.

The two type of loops are used for two different types of iteration:

- **definite iteration**
  - used, when you know how many times the loop will need to run
  - `for` loops are used for definite iteration since they loop for a set number of times
- **indefinite iteration**
  - used whe you don't know how many times the loop will need to run
  - `while` loops are used for indefinite iteration since they will keep looping as long as a condition is `True`

The best example for the difference between definite and indefinite loops is dealing cards for a game:

- Dealing for Uno
  - how many times do you need to deal to each player?
  - answer: seven times, so each player has seven cards
  - definite iteration as you will need to deal to the players seven times.
- Dealing for Snap
  - how many times do you you need to deal to each player?
  - answer: until there are no more cards left to deal
  - indefinite iteration as you will need to deal to the players while there are still cards left to deal

In summary:

- `for` loop is count controlled - we know how many times to run it.
- `while` loop is condition controlled - we don't know how many times to run it.


To understand `while` loops, lets look at a number guessing game example.

### Number guessing game

Create a new file in Thonny and call it `lesson_5_pt_2.py`, then enter the code below.

```python
import random


def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()


number = random.randint(1, 100)

guess = get_number("Guess a number between 1 and 100> ")

if guess == number:
    print("Correct!")
else:
    print("Incorrect. The number was", number)
```

PRIMM

- *Predict* what you think will happen when you run the code:
- *Run* the code. Did it follow your prediction?
- Let's *investigate* that code.

Code breakdown

- line `1`: `import random`
  - a module we haven't used before
  - the random module gives us access to a whole heap of functions to produce random results
  - we will be using one of these functions `randint()`, so we need to `import random`.
  - to see all the commands you can go the [**W3Schools Python Random Module page**](https://www.w3schools.com/python/module_random.asp).
- lines `3` to `9` is the same `get_number()` function we have been using previously.
- line `11`: `number = random.randint(1,100)`
  - `random.randint(1,100)` &rarr; use the `randint` function from the `random` module to give a random integer between `1` and `100` (inclusive)
  - `number =` &rarr; assign the returned integer to the variable `number`
- line `13`: `guess = get_number("Guess a number between 1 and 100> ")`
  - `get_number("Guess a number between 1 and 100> ")` &rarr; calls the `get_number` function to ask the user to provide a guessed number
  - `guess =` &rarr; assigns the returned integer to the variable `guess`
- line `15`: `if guess == number:` 
  - checks if the guessed and random number are the same
  - the `==` symbol is a *comparrison opperator* (see below), that is used to see if two values are the same
  - if the two values are the same run the code block on line `16`
- line `17`: `else:` &rarr; if the guessed and random number are not the same, run the code block on line `18`

> **Comparison Operators**
>
> A *comparison operation* compares two values and either returns `True` or `False`
> Python has many comparison operators that we use in condition testing
>
> - `==` &rarr; checks if two values are the same (equal to)
> - `!=` &rarr; checks if two values are not the same (not equal to)
> - `>` &rarr; checks if the left value is greater than the right value
> - `<` &rarr; checks if the left value is less than the right value
> - `>=` &rarr; checks if the left value is greater than or equal to the right value
> - `<=` &rarr; checks if the right value is less than or equal to the right value

So we've made a simple game, but it is not a really good one. Having a one in one hundred chance of guessing a number is not goint to keep the user entertained for too long. How about we adjust the code to allow the user to have 10 guesses.

Now that sounds like iteration, but what kind? Since we know how many times this will need to loop (10), its definite ireation, so that would require a `for` loop.

Change your code so it look like the code below. Specifically:

- line `13` &rarr; provide user instructions
- lines `15` to `21` &rarr; place the guessing process within a `for` loop
- line `21` &rarr; make sure you remove the number reveal
- line `23` &rarr; reveal the number after all 10 guesses are finished

```python
import random


def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()


number = random.randint(1, 100)

print("You have 10 turns to guess a number between 1 and 100")

for turn in range(10):
    guess = get_number("Guess a number between 1 and 100> ")

    if guess == number:
        print("Correct!")
    else:
        print("Incorrect. Try again")

print("The number was", number)
```

PRIMM

- *Predict* what you think will happen when you run the code:
- *Run* the code. Did it follow your prediction?
- We won't worry about *investigating* that code as it implenting code we have used before.

This is better, but still isn't great. There is a one in ten chance of getting the right number, and each guess is just a stab in the dark, with no knowledege gained from the previous guesses. How about we give the user hints? Let them know that their guess is too high or too low.

Change the `if` / `else` statement into the `if` / `elif` / `else` statement on lines `18` to `23` in the code below:

```python
import random


def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()


number = random.randint(1, 100)

print("You have 10 turns to guess a number between 1 and 100")

for turn in range(10):
    guess = get_number("Guess a number between 1 and 100> ")

    if guess > number:
        print("Guess is too high")
    elif guess < number:
        print("Guess is too low")
    else:
        print("Correct!")

print("The number was", number)
```

We've done a fair bit of coding with out any serious testing. So this time lets keep running our code until we cover all four branches:

1. guess is too high
2. guess is too low
3. guess is correct
4. all 10 guess used up without guessing the number

This might be easier to do if we know the random number. Feel free to add a line that prints the random number, but make sure you comment it out after testing.

PRIMM

- *Predict* what you think will happen when you run the code:
- *Run* the code. Did it follow your predictions?
- We won't worry about *investigating* that code as it implenting code we have used before.

Did you identify a probelm when the user guesses the number before their ten guesses were used up? The game prints `Correct!` but then contiunes to ask them to guess a number. This is because we have a set numbers. We use a `for` loop which to impliment a definite iteration.

What we actuallly have is an indefinite iteration which keep looping until the user gueses the number. To do this we will use a `while` loop.

### Using a `while` loop

Change your code so that is the same as the code below. Specifically:

- line `13` &rarr; add `guess = 0`
- line `15` &rarr; change the `for` statement to `while guess != number:`

```python
import random


def get_number(prompt):
    num = input(prompt)
    if num.isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()


number = random.randint(1, 100)

guess = 0

while guess != number:
    guess = get_number("Guess a number between 1 and 100> ")

    if guess > number:
        print("Guess is too high")
    elif guess < number:
        print("Guess is too low")
    else:
        print("Correct!")

print("The number was", number)
```

Again you want to run this code enough time that you have covered all four possible branches:

1. guess is too high
2. guess is too low
3. guess is correct
4. all 10 guess used up without guessing the number

PRIMM

- *Predict* what you think will happen when you run the code:
- *Run* the code. Did it follow your predictions?
- Let's *investigating* the new code to see how `while` statements work.

We're going ot do this code breakdown out of order to help our understanding:

- line `15`: `while guess != number:`
  - `guess != number` &rarr; this is the loop condition
  - as long as `guess` and `number` will:
    - return `True` if `guess` and `number` are not the same
    - return `False` if `guess` and `number` are the same
  - `while` tells Python to keep looping the following code block as long as the loop condition returns `True`
- line `13`: `guess = 0`
  - in our `while` statement we use the variale `guess` before getting an input from the user &rarr; this is raise an error
  - we need to assign value to `guess` before the `while` statement
    - if the value we assign to `guess` is the same as `number` the `while` loop will not run, and the user will not provide input.
    - so we assign `0` because `number` will always be between `1` and `100`

### Using `while` to enhance our error capture

We now have a somewhat fun game where the user has a good chance of gusessing the number. But in learning about `while` we have an opportunity to enhance ouir error capture in the `get_number()` function.

At the moment, if the user provides an input which isn't an integer, the game just ends. This is a bit harsh, especially if they have already made three or four guesses.

Adjust your `get_number()` function so that it is the same as in the code below.

```python
import random


def get_number(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid input")


number = random.randint(1, 100)

guess = 0

while guess != number:
    guess = get_number("Guess a number between 1 and 100> ")

    if guess > number:
        print("Guess is too high")
    elif guess < number:
        print("Guess is too low")
    else:
        print("Correct!")

print("The number was", number)
```

Again you want to run this code enough time that you have covered all four possible branches:

1. guess is too high
2. guess is too low
3. guess is correct
4. all 10 guess used up without guessing the number

PRIMM

- *Predict* what you think will happen when you run the code:
- *Run* the code. Did it follow your predictions?
- Let's *investigating* the new code to see how this use of a `while` loop works

Code breakdown:

- line `4`: `while True`
  - this is called an infinite loop, since the condition of will always be `True` the loop will always run.
  - infinite loops are frequently cause by errors, although not in this case
  - infinite loops can be broken out of by using the `break` statement, or the `return` statement, if it is in a function.
- lines `5` to `9` are the same as before, except they are now a code block inside of a `while` loop.
- it is worth noting the importance of line `7`
  - since the `while` loop is infinite, the program will keep asking for input unless it executes line `7`
  - in line `7` the value assigned to `num` is converted into an integer and then returned to the main program, effectively ending the function and exiting the `while` loop in the process.

The end effect of these changes is the program will endlessly ask the user for a number between 1 and 100, until the user provides an integer.

## Part 2 Exercise

In this course, the exercises are the *make* component of the PRIMM model. So work through the following exercises and *make* your own code.

### Exercise 4

Create a new file and save it in your subject folder calling it **lesson_5_ex_4.py**. Then type the following code into it.

``` python
import turtle


def draw_poly(length, sides, color):
    myttl.color("black", color)
    myttl.begin_fill()
    for i in range(sides):
        myttl.forward(length)
        myttl.right(360 / sides)
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
    myttl.goto(x_val, y_val)
    myttl.pendown()


# setup window
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create instance of turtle
myttl = turtle.Turtle()
myttl.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

move_pen()
draw_poly(size, num_sides, fill)
```

Follow the instructions in comments and make changes to the `get_number()` and `get_colour()` functions so they capture user input errors.