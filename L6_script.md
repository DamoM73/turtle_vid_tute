# Lesson 6

## Tutorial 1: Boolean Logic

In Python Boolean values and logic are all about True and False.

In Python you can test the Turthiness of something. When you compare two values, you are testing it's truthiness. 

There are six comparison operators  you can use

```python
print("jeff" == "jeff")  # equal to
print(1 != 1)            # not equal to
print(500 > 300)         # greater than
print(100 >= 250)        # greater than or equal to
print("a" < "q")         # less than
print(-30 <= 3)          # less than or equal to
```

It doesn't matter if you are testing literals or variables

```python
score = 10
print(score > 5)
```

You can also do operations on Boolean values using Python's Boolean operators:

- `and`
- `or`
- `not`

### `not` operator

The simplest operator to understand is the not operator. 

```python
print("not True is:", not True)
print("not False:", not False)
```

### `and` operator

For `and` to return `True` all values in the statement must be `True`

```python
print("True and True is:", True and True)
print("True and False is:", True and False)
print("False and True is:", False and True)
print("False and False is:", False and False)
print("True and True and True is:", True and True and True)
print("True and True and False is:", True and True and False)
```

### `or` operator

For `or` to return `True` just one value in the statement needs to be `True`

```python
print("True or True is:", True or True)
print("True or False is:", True or False)
print("False or True is:", False or True)
print("False or False is:", False or False)
print("True or True or True is:", True or True or True)
print("True or False or False is:", True or False or False)
```

You can combine comparison operators and Boolean operators

```python
print(7 < 8 and "a" < "o")
```

### Introduce the homework task

```python
import turtle

## Prepare the windows and turtle ##
def setScene():
    turtle.setup(800, 600)

    ## Respond to mouse click (signal) ##
    turtle.onscreenclick(drawDot)
    
    ## Set up the grid ##
    driver.speed(0)
    for i in range(4):
        driver.forward(400)
        driver.back(400)
        driver.right(90)
    driver.penup()

## Reaction to signal (slot) ##
def drawDot(x, y) :
    print(x,y)
    dotColor = 'orange'
    driver.goto(x, y)
    dotSize = 10
    driver.dot(dotSize, dotColor)

driver = turtle.Turtle()
setScene()
driver.hideturtle()
```

What needs to happen to make clicks on the lower half green?

### Exercises

- L6_Ex1.py
- L6_Ex2.py
- L6_Ex3.py



