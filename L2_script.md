# Lesson 2

Create a new file

## Tutorial 1: Iteration introduction

### To date

Writing out commands sequentially 

```python
print("Hello Hunter")
print("Hello Jordi")
print("Hello Adam")
print("Hello Jesse")
print("Hello Bryce")
print("Hello Ben")
```

Doesn't scale well.

- Large number of files

- updating issues

### For Loops

Solution - the `FOR` loop

Create a list of names

```python
names = ["Hunter", "Jordi", "Adam", "Bryce", "Ben"]

for name in names:
    print("Hello", name)
```

Run through with debugger

Show how blocks work

```python
names = ["Hunter", "Jordi", "Adam", "Bryce", "Ben"]

for name in names:
    print("Hello", name)
    print("How are you?")
```

```python
names = ["Hunter", "Jordi", "Adam", "Bryce", "Ben"]

for name in names:
    print("Hello", name)
    print("How are you?")

print("Come in and sit down")
```

Student added to class

```python
names = ["Hunter", "Jordi", "Adam", "Bryce", "Ben"]

for name in names:
    print("Hello", name)

names.append("Jasper")


for name in names:
    print(name, "come in and sit down")
```

extrapolate out to huge files

Change greeting

Remove repeating code: DRY principle

## Range

You can also run loops over lists of numbers

```python
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in number_list:
    print(number)
```

Ok, now print all the numbers between 1 and 100

```python
number_list = range(1,101)

for number in number_list:
    print(number)
```

Remove step

```python
for number in range(1,101):
    print(number)
```

### Use for Turtle

```python
import turtle

window = turtle.Screen()
window.setup(500,500)

my_ttl = turtle.Turtle()

for number in range(1,101):
    my_ttl.forward(100)
    my_ttl.backward(100)
    my_ttl.left(3)
```
## Exercises
- L2_Ex_1
- L2_Ex_2
- L2_Ex3
- L2_Ex4
- L2_Ex5