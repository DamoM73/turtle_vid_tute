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
def draw_dot(x, y) :
    print(x,y)
    if y > 0:
        dotColor = 'orange'
    else:
        dotColor = 'green'
    driver.goto(x, y)
    dotSize = 10
    driver.dot(dotSize, dotColor)

driver = turtle.Turtle()
set_scene()
driver.hideturtle()