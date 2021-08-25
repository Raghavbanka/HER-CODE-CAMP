# import random library (to randomize enemy location)
# import turtle library
# import platform to add sound effects to the game

import math
import random
import turtle
import winsound
import pygame
from pygame import mixer
import time

# turtle.fd(0)

turtle.tracer(0)
turtle.hideturtle()

pygame.mixer.init()
mixer.music.load("background.wav")
pygame.mixer.music.set_volume(0.3)
mixer.music.play(-1)

# setup the screen and add pictures
screen = turtle.Screen()
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.addshape('battleship_2.gif')
screen.addshape('enemy1.gif')
screen.addshape('bullet.gif')
screen.addshape('start.background.gif')
screen.addshape('yellow.gif')
# boolean to make the game start
start = False
# draw the start screen on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('start.background.gif')
# create the button
button = turtle.Turtle()
button.speed(0)
button.hideturtle()
button.color('#8B008B')  # the color of the line it draws
button.pencolor('white')  # the color of the object
button_x = 80
button_y = -185
button_length = 200
button_width = 100
button.penup()
button.begin_fill()
button.goto(button_x, button_y)
button.goto(button_x, button_y + button_width)
button.goto(button_x + button_length, button_y + button_width)
button.goto(button_x + button_length, button_y)
button.goto(button_x, button_y)
button.end_fill()
button.penup()
button.goto(180, -163)
button.pencolor("white")
button.write("PLAY", align="center", font=("Courier", 40, "bold"))


# function that the button executes
def start_game(x, y) -> None:  # -> None means function will not return anything
    """ Start game
    """
    if button_x <= x <= (button_x + button_length):
        if button_y <= y <= (button_y + button_width):
            global start
            start = True
            screen.clear()

            screen.bgcolor("black")
            screen.bgpic("neon.png")


# making the button 'clickable'
screen.onclick(start_game)
# this loop makes the start screen display until the button is clicked
while not start:
    screen.update()

# turtle.fd(0)
turtle.tracer(0)

screen.bgcolor("black")
screen.bgpic('neon.png')
# put the battleship on the screen
ship = turtle.Turtle()
ship.shape('battleship_2.gif')
ship.speed(0)
ship.penup()
ship.setpos(0, -263)
ship.fire_state = False
# the speed of the battle ship in a variable
shipspeed = 20


# functions to move the battle ship
def ship_left() -> None:
    """ Move ship to the left"""
    x_cor = ship.xcor()
    x_cor -= shipspeed
    if x_cor < -364:
        x_cor = -364
    ship.setx(x_cor)


def ship_right() -> None:
    """ Move ship to the right"""
    x_cor = ship.xcor()
    x_cor += shipspeed
    if x_cor > 360:
        x_cor = 360
    ship.setx(x_cor)


# the speed of the enemy in a variable
# put 8 enemies on the screen
num_enemies = 8
# 1,3
enemy_speed = 100
enemies = []  # create a list to store the enemies
# create a for loop for the number of enemies
# each time, add an enemy to the list enemies
for _ in range(num_enemies):
    enemy = turtle.Turtle()
    enemy.direction = random.choice([-1, 1])
    enemy.speed(0)
    enemy.shape('enemy1.gif')
    enemy.penup()
    enemy.is_yellow = False
    # randomize the enemy location
    enemy.setpos(random.randint(-300, 300), random.randint(170, 200))
    enemies.append(enemy)

# create the bullet
bullet = turtle.Turtle()
bullet.shape('bullet.gif')
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
# the speed of the bullet in a variable
bullet.bullet_speed = 20


# give the bullet a condition (ready - shooting)


def initialise_enemy() -> turtle.Turtle:
    """ Function to initilaise bullet"""
    alien = turtle.Turtle()
    alien.direction = random.choice([-1, 1])
    alien.speed(0)
    if random.randint(0, 10) == 0:
        enemy.shape('yellow.gif')
        enemy.is_yellow = True
    else:
        enemy.shape('enemy1.gif')
        enemy.is_yellow = False
    enemy.penup()
    # randomize the enemy location
    enemy.setpos(random.randint(-300, 300), random.randint(170, 200))
    return enemy


# function to fire the bullet
def fire_bullet() -> None:
    """ Function to fire bullet"""
    if not ship.fire_state:  # only fire a bullet when no bullet is fired
        x_cor = ship.xcor()
        y_cor = ship.ycor() + 15
        bullet.setpos(x_cor, y_cor)
        bullet.showturtle()
        ship.fire_state = not ship.fire_state


# create a score counter at top left
counter = turtle.Turtle()
counter.speed(0)
counter.hideturtle()
counter.color('white')
counter.penup()
counter.setpos(-380, 270)
counter.pendown()
counter.write("Points: ", font=("Arial", 15, "bold"))  # print Points: on screen
# the player's score in a variable
points = 0
# print the score on the screen
counter.penup()
counter.setpos(-310, 270)
counter.pendown()
counter.write(points, font=("Arial", 15, "bold"))
counter.penup()


# function that checks collision (bullet hit alien)
def collision(obj1: turtle.Turtle, obj2: turtle.Turtle) -> bool:  # objs being alien and bullet
    """ Function to determine collision or not"""

    # dist = math.sqrt((obj1.xcor() - obj2.xcor()) ** 2 +
    #                  (obj1.ycor() - obj2.ycor()) ** 2)
    # distanceX = obj1.xcor() - obj2.xcor()  # get the distance between the objects
    # distanceY = obj1.ycor() - obj2.ycor()  # get the distance between the objects
    dist = obj1.distance(obj2)
    if dist < 32:
        return True
    else:
        return False


# make the battleship move by listening to user input
screen.listen()
screen.onkeypress(ship_left, "Left")  # "Left" means left arrow
screen.onkeypress(ship_right, "Right")  # "Right" means right arrow
screen.onkeyrelease(fire_bullet, "space")  # "space" means space key

# main loop for the game
var = True
while var and start:
    turtle.hideturtle()
    # make all 8 enemies move
    for enemy in enemies:
        # move the enemy across
        x = enemy.xcor()
        x += enemy_speed * enemy.direction  # move the enemy 0.15 pixels
        enemy.setx(x)
        # move ALL the enemies down and back the other direction
        if enemy.xcor() > 360 or enemy.xcor() < -368:
            y = enemy.ycor()
            y -= 45  # change the position of the enemy down 45 pixels
            enemy.sety(y)  # move the enemy down
            enemy.direction *= -1  # so the enemy moves back the other way
        # check if the enemy is too low (player loses)
        if enemy.ycor() < -200:
            var = False

    for enemy in enemies:
        # check collision
        if collision(enemy, bullet) and ship.fire_state:
            if enemy.is_yellow:
                shipspeed += 8
            bullet.hideturtle()  # if collision is true, hide bullet and reset enemy
            enemies.remove(enemy)
            enemies.append(initialise_enemy())
            ship.fire_state = not ship.fire_state  # reset bullet condition so it can fire
            bullet.setpos(0, -300)  # move the bullet to bottom to avoid collision
            points += 1  # add one point
            counter.clear()  # clear (Points: *) from the screen
            counter.setpos(-380, 270)  # re-write the points on the screen
            counter.pendown()
            counter.write("Points: ", font=("Arial", 15, "bold"))
            counter.penup()
            counter.setpos(-310, 270)
            counter.pendown()
            counter.write(points, font=("Arial", 15, "bold"))
            counter.penup()
            if points % 8 == 0 and points != 0:
                enemy_speed += 0.8

    # move the bullet
    if ship.fire_state:
        y = bullet.ycor()
        y += bullet.bullet_speed
        bullet.sety(y)
    # change bullet condition to ready when bullet gets goes past the frame
    if bullet.ycor() > 300:
        ship.fire_state = False
        bullet.hideturtle()

    screen.update()


# setup the end screen with points
if not var:
    pygame.mixer.music.stop()
    turtle.clearscreen()
    screen.bgcolor("red")
    pen1 = turtle.Turtle()
    pen1.speed(0)
    pen1.color("white")
    pen1.penup()
    pen1.setpos(0, 100)
    pen1.pendown()
    pen1.write("GAME OVER", align="center", font=("Arial", 50, "bold"))
    pen1.penup()
    pen1.setpos(0, 0)
    pen1.pendown()
    pen1.write("Nice Try!", align="center", font=("Arial", 30, "bold"))
    pen1.penup()
    pen1.setpos(-20, -150)
    pen1.pendown()
    pen1.write("Points:", align="center", font=("Arial", 30, "bold"))
    pen1.penup()
    pen1.setpos(55, -150)
    pen1.pendown()
    pen1.write(points, font=("Arial", 30, "bold"))
    pen1.hideturtle()
    time.sleep(5)


# # create the button
# button = turtle.Turtle()
# button.speed(0)
# button.hideturtle()
# button.color('#8B008B')  # the color of the line it draws
# button.pencolor('white')  # the color of the object
# button_x = 120
# button_y = -185
# button_length = 200
# button_width = 100
# button.penup()
# button.begin_fill()
# button.goto(button_x, button_y)
# button.goto(button_x, button_y + button_width)
# button.goto(button_x + button_length, button_y + button_width)
# button.goto(button_x + button_length, button_y)
# button.goto(button_x, button_y)
# button.end_fill()
# button.penup()
# button.goto(220, -163)
# button.pencolor("white")
# button.write("END", align="center", font=("Courier", 40, "bold"))
#
# screen.listen()
#
#
# def end_screen(x, y) -> bool:
#     """ Start game
#     """
#     if button_x <= x <= (button_x + button_length):
#         if button_y <= y <= (button_y + button_width):
#             return True

count = 200000
# while not var:
#     screen.update()
#     count-=1
#     if count==0:
#         screen.bye()
    # if not end_screen:
    #     screen.bye()



