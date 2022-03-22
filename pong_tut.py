import turtle
import time
import random

def left_pad_up():
    left_pad.dir = "up"

def left_pad_down():
    left_pad.dir = "down"
    
def left_pad_stop():
    left_pad.dir = "stop"
    
def right_pad_up():
    right_pad.dir = "up"

def right_pad_down():
    right_pad.dir = "down"
    
def right_pad_stop():
    right_pad.dir = "stop"


def movement():
    # left pad
    if left_pad.dir == "up":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y + paddle_speed
        left_pad.goto(current_x,new_y)
    elif left_pad.dir == "down":
        current_x = left_pad.xcor()
        current_y = left_pad.ycor()
        new_y = current_y - paddle_speed
        left_pad.goto(current_x,new_y)
    
    # right pad
    if right_pad.dir == "up":
        current_x = right_pad.xcor()
        current_y = right_pad.ycor()
        new_y = current_y + paddle_speed
        right_pad.goto(current_x,new_y)
    elif right_pad.dir == "down":
        current_x = right_pad.xcor()
        current_y = right_pad.ycor()
        new_y = current_y - paddle_speed
        right_pad.goto(current_x,new_y)
    
    # ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


def reset_ball():
    ball.goto(0,0)
    ball.dx = random.choice([-10,10])
    ball.dy = random.randint(-10,10)
    

def check_collision():
    if ball.distance(right_pad) < 25 or ball.distance(left_pad) < 25:
        ball.dx *= -1
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.dy *= -1
    elif ball.xcor() < -500:
        reset_ball()
    elif ball.xcor() > 500:
        reset_ball()
        
def draw_score():
    left_score.clear()
    left_score.write(left_score.val,
                     align="center",
                     font=("Courier", 24, "normal"))
    
    right_score.clear()
    right_score.write(right_score.val,
                     align="center",
                     font=("Courier", 24, "normal"))
    

# vairable
screen_width = 1000
screen_height = 600
paddle_speed = 10
game_speed = .05

# setup screen
window = turtle.Screen()
window.setup(screen_width,screen_height)
window.title("Pong")
window.bgcolor("black")
window.tracer(0)                 # turn off automatic screen updates

# draw screen elements
ui = turtle.Turtle()
ui.color("white")
ui.pensize(5)
ui.penup()
ui.goto(0,screen_height / 2)
ui.pendown()
ui.goto(0,screen_height / 2 * -1)

# create left paddle
left_pad = turtle.Turtle()
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(3,1)
left_pad.penup()
left_pad.goto((screen_width/2-30)*-1,0)
left_pad.dir = "stop"

# create right paddle
right_pad = turtle.Turtle()
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(3,1)
right_pad.penup()
right_pad.goto((screen_width/2-30),0)
right_pad.dir = "stop"

# create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 0
ball.dy = 0
reset_ball()

# scores
left_score = turtle.Turtle()
left_score.speed(0)
left_score.shape("square")
left_score.color("white")
left_score.penup()
left_score.hideturtle()
left_score.goto(-250,260)
left_score.val = 0

right_score = turtle.Turtle()
right_score.speed(0)
right_score.shape("square")
right_score.color("white")
right_score.penup()
right_score.hideturtle()
right_score.goto(250,260)
right_score.val = 0

# key bindings
window.listen()
window.onkeypress(left_pad_up, "w")
window.onkeyrelease(left_pad_stop,"w")
window.onkeypress(left_pad_down, "s")
window.onkeyrelease(left_pad_stop,"s")
window.onkeypress(right_pad_up, "p")
window.onkeyrelease(right_pad_stop,"p")
window.onkeypress(right_pad_down, ";")
window.onkeyrelease(right_pad_stop,";")


# ---- MAIN LOOP ---- #
while True:
    window.update()
    time.sleep(game_speed)
    movement()
    check_collision()
    draw_score()