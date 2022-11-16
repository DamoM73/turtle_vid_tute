# Python Turtle - Lesson 1

## Part 1: Thonny Introduction

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/90T-NE_a50E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### What's an IDE

Welcome to our first lesson on Python Turtle. In this lesson you will be introduced to Thonny - the integrated development environment (IDE) we will use to write our code. We are going to have a look at a really basic python code and understand some of its syntax.

> We will be using Thonny as our IDE. Thonny is a Python IDE for beginners. It comes packages with Python, which helps with the setup. You can download it from: **[thonny.org/](https://thonny.org/)**.

It's important to understand that Thonny isn't the language we will be programming with, Python. Just like you use Microsoft Word to write English, we will be using Thonny to write Python. 

Python is programmed in text files called scripts. You can use any text editor to program Python. Integrated development environment like Thonny have additional features like highlighting syntax by marking it in different colours and helping you debug your program. We will deal with those features later, in the meanwhile just think of Thonny as a text editor with extra features built in.

### Setting up Thonny

Before we look at Thonny's User Interface (UI), we need to turn on a few features so our IDE looks the same.

> Throughout this course, **bold words** are words that you need to look for on the UI

First, go to the **View** menu and make sure there is a tick beside **Assistant**, **Shell** and **Variable**.

![Thonny view settings](./assets/thonny_view_settings.png)

Next go to **Tools** &rarr; **Options**

![Thonny tools options](./assets/thonny_tools_options.png)

On the **Editor** tab make sure that your check-boxes are the same as the image below.

![Thonny options editor](./assets/thonny_options_editor.png)

Finally on the **Theme and Font** tab make sure that the **Syntax theme** is set to **IDLE Classic**. Syntactic highlighting changes the colour of words, depending on their role in the code. This helps us to structure our code the right way.

![Thonny options theme](./assets/thonny_options_theme.png)

Now click **OK** and your Thonny will look the same as the one in the videos.

### The User Interface

The image below shows the Thonyy UI parts that you need to know to get started. We'll learn more as they are needed.

![Thonny UI](./assets/thonny_ui.png)

### First Program

For our first program we are going to make a really simple little program called *hello world*, because this is the traditional first program to write.

Type the following code into the Code panel.

``` python
# Our First Program

print("Hello World")
```

#### Predict

Remember the PRIMM process (*Predict*, *Run*, *Investigate*, *Modify*, *Make*). Before you run the code you need to *Predict* what you think will happen. Go ahead and have a guess at what you think will happen. 

#### Run

Now go ahead and *Run* the code by clicking on the **Play button** (or you can press F5 on your keyboard).

Your **Shell** should now show `Hello World`. Is that what you predicted would happen?

#### Investigate

Let's *Investigate* what happened.

The first thing to notice is that only `Hello World` appears in the terminal. The program completely misses the first line: `# Our First Program`. Why is that? Well. Starting a line with the `#` character tells Python that the line is a comment. It is only meant to be read by humans, so the computer will ignore that line. It's a way to make notes throughout your code.

Next notice line `3`. The word `print` is in purple. This tells the coder that `print` is a keyword in Python. A key word is like a command. Try removing the `n` from print so the line now reads `prit("Hello World")`. Try running the code now and see what happens.

You should get the following error message in your **Shell**:

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
NameError: name 'prnt' is not defined
```

Let's unpack that error message. The first line `Traceback (most recent call last):` is Python saying "this is where I got up to".

The second line `File "<string>", line 3, in <module>` tells you the file and the line of the error. In our case it is `line 3`.

Finally the last line `NameError: name 'prnt' is not defined` explains the type of error. In this case it is a `NameError` which means it's found a word that it doesn't understand. It then tell us which word `prnt`.

Now go back to line `3` and fix it up so it reads `print("Hello World")` again. Notice that `print` turns back to purple.

Let's keep investigating by removing the `"` so line`3` reads `print(Hello World)`, and then run the program again.

Once again your **Shell** contains another error:

```
Traceback (most recent call last):
  File "<string>", line 3
    print(Hello World)
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

This time the error actually shows you the line with the error `print(Hello World)` and then the line underneath has a row of `^` symbols pointing to where the error is. It also tells us it is a `SyntaxError: invalid syntax.` which means it's not following Python rules. Finally it suggests what you might have done wrong `Perhaps you forgot a comma?`. The suggestion is wrong in this case, but luckily we know what we did wrong.

Change line `3` back so that is reads `print("Hello World")` again. Notice how `"Hello World"` turns green? This syntax highlighting lets you know that the `Hello World` is a thing called a string. For the time being just think of a string as a whole bunch of characters. We will learn more about strings later on.

Continuing with the *Investigation* of line `3`, lets remove the `(` and `)` characters. So it now reads `print Hello World`. Running this will present the following error in your *Shell*

```
Traceback (most recent call last):
  File "<string>", line 3
    print "Hello World"
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

The error message should look familiar now. It's another `SyntaxError` but a different one called `Missing parentheses in call to 'print'`. Parentheses are the curved bracket we just removed. This time Python's hint was correct `Did you mean print(...)?`.

Now lets just replace the opening parenthesis `(` so line `3` now reads `print("Hello World"`. Run it and your will notice the error message change changed to a different syntax error.

```
Traceback (most recent call last):
  File "<string>", line 3
    print ("Hello World"
          ^
SyntaxError: '(' was never closed
```

It is now letting you know that you failed to close your parenthesis. In Python every opening parenthesis `(` needs to be matched with a closing parenthesis `)`. But before you fix line`3`, look at Thonny. Notice from `(` onwards is highlighted grey. This is Thonny's way of letting you know that a opening parenthesis was not closed. That way you can catch the error before running your code.

Ok you can fix line `3` up now so it reads `print("Hello World")`.

Ok our investigation is over, and you have met some of the error messages. In your time coding, you will meet many, many more of these error messages. Don't be discouraged by them. Even the most experienced programmers regularly get error messages. In fact there is a saying amongst programmers: error messages are your friend. They help you work out what when wrong.

#### Modify

Now time to modify the code. There's not much code there. But spend some time making the code print different things to the **Shell**.

## Part 2: Introducing turtle

### First turtle program

```python
# Our first turtle program
```

Save as L1_tut2

### Import turtle

```python
import turtle
```

### Create turtle

```python
import turtle

my_ttl = turtle.Turtle()
```

### Draw line

```python
import turtle

my_ttl = turtle.Turtle()

my_ttl.forward(100)
```

### Resize canvas

```python
import turtle

window = turtle.Screen()
window.setup(500,500)

my_ttl = turtle.Turtle()

my_ttl.forward(100)
```

### Change icon

```python
import turtle

window = turtle.Screen()
window.setup(500,500)

my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

my_ttl.forward(100)
```

### Draw with turn

```python
import turtle

window = turtle.Screen()
window.setup(500,500)

my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

my_ttl.forward(100)
my_ttl.left(90)
```

### Draw second line

```python
mport turtle

window = turtle.Screen()
window.setup(500,500)

my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

my_ttl.forward(100)
my_ttl.left(90)
my_ttl.forward(100)
```
### Exercises

#### L1_Ex1

```python
## Draw a square with the Turtle ##

import turtle

window = turtle.Screen()
window.setup(500, 500)

myttl = turtle.Turtle()

## Write your code below this line ##
```

#### L1_Ex2

```python
## Draw a Triangle with the Turtle ##

import turtle

window = turtle.Screen()
window.setup(500, 500)

myttl = turtle.Turtle()

## Write your code below this line ##
```

#### L1_Ex3

```python
## Draw a hexagon with the Turtle ##

import turtle

window = turtle.Screen()
window.setup(500, 500)

myttl = turtle.Turtle()

## Write your code below this line ##
```

