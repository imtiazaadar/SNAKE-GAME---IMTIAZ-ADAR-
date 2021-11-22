# Imtiaz Adar
# Email : imtiaz-adar@hotmail.com
# Phone : +8801778767775
# Project : Snake Game
# Language Used : Python
# Date : 21 / 11 / 2021

from turtle import *
from time import sleep
from random import randint

# variables
score, highscore = 0, 0
parts = []
delay = 0.1
outside_x = 1500
outside_y = 1500

# window setup
window = Screen()
window.title('SNAKE GAME BY IMTIAZ ADAR')
window.setup(width=709, height=718, startx=400, starty=40)
window.bgcolor('black')
window.cv._rootwindow.resizable(False, False)
window.tracer(0)

# snake head
snake_head = Turtle()
snake_head.speed(0)
snake_head.color('#083C0F')
snake_head.shape('square')
snake_head.penup()
snake_head.goto(-5, -21)
snake_head.direction = "stop"

# food
food = Turtle()
food.speed(0)
food.color('red')
food.shape('circle')
food.penup()
food.goto(-5, 100)

# scoreboard
scoreboard = Turtle()
scoreboard.speed(0)
scoreboard.color('cyan')
scoreboard.shape('square')
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 262)
scoreboard.write('Score : 0     High Score : 0', align="center", font=("ds-digital", 30, "normal"))

# line after scoreboard
after_scoreboard = Turtle()
after_scoreboard.color('white')
after_scoreboard.shape('square')
after_scoreboard.penup()
after_scoreboard.goto(0, 249)
after_scoreboard.shapesize(0.1, 100)

# imtiaz adar's intro
imtiaz_adar = Turtle()
imtiaz_adar.color('cyan')
imtiaz_adar.shape('square')
imtiaz_adar.penup()
imtiaz_adar.hideturtle()
imtiaz_adar.goto(0, 316)
imtiaz_adar.write('Snake Game By Imtiaz Adar', align="center", font=("ds-digital", 15, "normal"))

# directions
def up_direction():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'
def down_direction():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'
def left_direction():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'
def right_direction():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

# move
def move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y + 20)
        
    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y - 20)
        
    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 20)
        
    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 20)
        
# is collision with border
def isCollisionWithBorder():
    if snake_head.xcor() > 328 or snake_head.xcor() < - 334 or snake_head.ycor() > 221 or snake_head.ycor() < -339:
        resetGame()
  
# is food eaten      
def isFoodEaten():
    global score
    global highscore
    global delay
    if snake_head.distance(food) < 20:
        x = randint(-334, 328)
        y = randint(-339, 221)
        food.goto(x, y)
        newParts()
        score += 10
        if score < 50:
            delay -= 0.001
        else:
            delay -= 0.005
        if score > highscore:
            highscore = score
        updateScore()
        
# is collision with body
def isCollisionWithBody():
    for body_part in parts:
        if body_part.distance(snake_head) < 20:
            resetGame()

# update score
def updateScore():
    scoreboard.clear()
    scoreboard.write(f'Score : {score}      High Score : {highscore}', align="center", font=("ds-digital", 30, "normal"))

# new parts
def newParts():
    new_part = Turtle()
    new_part.color('green')
    new_part.shape('square')
    new_part.penup()
    parts.append(new_part)

# add parts in reverse order
def addPartsReverseOrder():
    for i in range(len(parts) - 1, 0, -1):
        x = parts[i - 1].xcor()
        y = parts[i - 1].ycor()
        parts[i].goto(x, y)
    
    if len(parts) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        parts[0].goto(x, y)

# listen key
def listenKey():
    window.listen()
    window.onkeypress(up_direction, 'Up')
    window.onkeypress(down_direction, 'Down')
    window.onkeypress(left_direction, 'Left')
    window.onkeypress(right_direction, 'Right')

# reset game
def resetGame():
    sleep(1)
    snake_head.goto(-5, -21)
    snake_head.direction = 'stop'
    for part in parts:
        part.goto(outside_x, outside_y)
    parts.clear()
    global score
    score = 0
    global delay
    delay = 0.1
    scoreboard.clear()
    scoreboard.write(f'Score : {score}      High Score : {highscore}', align="center", font=("ds-digital", 30, "normal"))

# calling listen key function
listenKey()

# game loop
while True:
    # updating window
    window.update()
    # checking collision with border
    isCollisionWithBorder()
    # checking food is eaten or not
    isFoodEaten()
    # adding parts in reverse order
    addPartsReverseOrder()
    # move
    move()
    # checking collision with body
    isCollisionWithBody()
    # sleep
    sleep(delay)
    
window.mainloop()