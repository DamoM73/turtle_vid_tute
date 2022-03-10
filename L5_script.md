# Lesson 5

## Tutorial 1: Conditionals

Look back at L4_tut2.py

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

num_sides = int(input("How many sides?> "))
size = int(input("How long are the sides?> "))

draw_poly(size,num_sides)
```

What happens when we don't enter a number?

`ValueError: invalid literal for int() with base 10: 'd'`

```python
user_value = input("Enter a number: ")

print(user_value.isdigit())
```

### Introduce `if` statements

```python
user_value = input("Enter a number: ")

if user_value.isdigit():
    print("Yes that is a number")
```

### Introduce `if` `else` statements

```python
user_value = input("Enter a number: ")

if user_value.isdigit():
    print("Yes that is a number")
else:
    print("Silly, that is not a number")
```

Go back to L4_tut2.py

prevent errors from entering non digital values for sides

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

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

prevent errors for entering non digital values for size

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen,screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

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

Now, does this pass the dry test?

```python
import turtle

def draw_poly(length, sides):
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
        
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
fred = turtle.Turtle()
fred.shape("turtle")

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
    fred.color("black",color)
    fred.begin_fill()
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
    fred.end_fill()
        
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
fred = turtle.Turtle()
fred.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")

draw_poly(size,num_sides,"red")
```

Can we let the user choose the colour

```python
import turtle

def draw_poly(length, sides, color):
    fred.color("black",color)
    fred.begin_fill()
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
    fred.end_fill()
        
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
fred = turtle.Turtle()
fred.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

draw_poly(size,num_sides, fill)
```

### Exercises

L5_Ex1.py

L5_Ex2.py

L5_Ex3.py

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

