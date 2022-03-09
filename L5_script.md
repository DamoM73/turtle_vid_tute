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

Introduce `if` statements

```python
user_value = input("Enter a number: ")

if user_value.isdigit():
    print("Yes that is a number")
```

Introduce `if` `else` statements

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



## Tutorial 2: While Loop



