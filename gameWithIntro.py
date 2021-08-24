# import random library (to randomize enemy location)
# import turtle library
# import platform to add sound effects to the game
import random
import turtle
import winsound
import pygame
from pygame import mixer

turtle.tracer(0)

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
screen.addshape('powerup.gif')
screen.addshape('start.background.gif')
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
button.color('#8B008B') # the color of the line it draws
button.pencolor('white') # the color of the object
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
button.write("PLAY", False, align="center", font=("Courier", 40, "bold"))


# function that the button executes
def start_game(x, y) -> None:  # -> None means function will not return anything
    if button_x <= x <= (button_x + button_length):
        if button_y <= y <= (button_y+button_width):
            global start
            start = True
            screen.clear()
            screen.bgpic("neon.png")


# making the button 'clickable'
screen.onclick(start_game)
# this loop makes the start screen display until the button is clicked
while not start:
    screen.update()


# put the battleship on the screen
ship = turtle.Turtle()
ship.shape('battleship_2.gif')
ship.speed(0)
ship.penup()
ship.setpos(0, -263)
# the speed of the battle ship in a variable
shipspeed = 60


# functions to move the battle ship
def ship_left():
    x = ship.xcor()
    x -= shipspeed
    if x < -364:
        x = -364
    ship.setx(x)


def ship_right():
    x = ship.xcor()
    x += shipspeed
    if x > 360:
        x = 360
    ship.setx(x)


# put one enemy on the screen
# enemy = turtle.Turtle()
# enemy.shape('enemy.gif')
# enemy.penup()
# enemy.speed(0)
# enemy.setpos(-300, 250)
# the speed of the enemy in a variable
enemyspeed = 8
# put 8 enemies on the screen
num_enemies = 8
enemies = [] # create a list to store the enemies
for v in range(num_enemies): # create a for loop for the number of enemies
    enemies.append(turtle.Turtle()) # each time, add an enemy to the list enemies
for enemy in enemies:
    enemy.shape('enemy1.gif')
    enemy.penup()
    enemy.speed(0)
    # randomize the enemy location
    enemy.setpos(random.randint(-300, 300), random.randint(170, 200))


# create the bullet
bullet = turtle.Turtle()
bullet.shape('bullet.gif')
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
# the speed of the bullet in a variable
bulletspeed = 70
# give the bullet a condition (ready - shooting)
bulletcondition = "ready"


# function to fire the bullet
def fire_bullet():
    global bulletcondition  # global means variable is changable even within func.
    if bulletcondition == "ready": # only fire a bullet when no bullet is fired
        play_sounds("firing_sound.wav") # play a firing sound when a bullet is fired
        x = ship.xcor()
        y = ship.ycor() + 15
        bullet.setpos(x, y)
        bullet.showturtle()
        bulletcondition = "shooting"


# create a score counter at top left
counter = turtle.Turtle()
counter.speed(0)
counter.hideturtle()
counter.color('white')
counter.penup()
counter.setpos(-380, 270)
counter.pendown()
counter.write("Points: ", False, align="left", font=("Arial", 15, "bold")) # print Points: on screen
# the player's score in a variable
points = 0
# print the score on the screen
counter.penup()
counter.setpos(-310, 270)
counter.pendown()
counter.write(points, False, align="left", font=("Arial", 15, "bold"))
counter.penup()


# function that checks collision (bullet hit alien)
def collision(obj1, obj2):  # objs being alien and bullet
    distanceX = obj1.xcor() - obj2.xcor()  # get the distance between the objects
    distanceY = obj1.ycor() - obj2.ycor()  # get the distance between the objects
    if abs(distanceX) < 32 and abs(distanceY) < 32:
        return True
    else:
        return False



# function to play sound effects in the game
def play_sounds(sound_file, time=0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)


# make the battleship move by listening to user input
screen.listen()
screen.onkeypress(ship_left, "Left")    # "Left" means left arrow
screen.onkeypress(ship_right, "Right")  # "Right" means right arrow
screen.onkeypress(fire_bullet, "space") # "space" means space key


collide = False

# main loop for the game
var = True
while var and start:
    # if enemyspeed != 0:
    #     ori = enemyspeed
    #
    # ori = enemyspeed



    # make all 8 enemies move
    for enemy in enemies:
        # move the enemy across
        x = enemy.xcor()
        x += enemyspeed # move the enemy 0.15 pixels
        enemy.setx(x)
        # move ALL the enemies down and back the other direction
        if enemy.xcor() > 360 :
            for v in enemies:
                y = v.ycor()
                y -= 45 # change the position of the enemy down 45 pixels
                v.sety(y) # move the enemy down
            enemyspeed *= -1  # so the enemy moves back the other way
        if enemy.xcor() < -368 :
            for v in enemies:
                y = v.ycor()
                y -= 45
                v.sety(y)
            enemyspeed *= -1  # - and - make a positive

        # check collision
        if collision(enemy, bullet):
            collide = True
            play_sounds("collision_sound.wav") # play sound when enemy is shot
            bullet.hideturtle()  # if collision is true, hide bullet and reset enemy
            enemy.setpos(random.randint(-300, 300), random.randint(170, 200))
            bulletcondition = "ready"  # reset bullet condition so it can fire
            bullet.setpos(0, -300)  # move the bullet to bottom to avoid collision
            points += 1  # add one point
            change = True
            counter.clear()  # clear (Points: *) from the screen
            counter.setpos(-380, 270)  # re-write the points on the screen
            counter.pendown()
            counter.write("Points: ", False, align="left", font=("Arial", 15, "bold"))
            counter.penup()
            counter.setpos(-310, 270)
            counter.pendown()
            counter.write(points, False, align="left", font=("Arial", 15, "bold"))
            counter.penup()
            if points % 8 == 0 and points != 0:
                enemyspeed += 2

        # check if the enemy is too low (player loses)
        if enemy.ycor() < -200:
            play_sounds("lose.wav") # play sound if the enemies win
            var = False

    # move the bullet
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
    # change bullet condition to ready when bullet gets goes past the frame
    if bullet.ycor() > 300 or collide:
        bulletcondition = "ready"
        collide = False


    screen.update()

# setup the end screen with points
if not var:
    pygame.mixer.music.stop()
    turtle.clearscreen()
    screen.bgpic('end.background.png')
    pen1 = turtle.Turtle()
    pen1.speed(0)
    pen1.color("white")
    pen1.penup()
    pen1.setpos(0, 100)
    pen1.pendown()
    pen1.write("GAME OVER", False, align="center", font=("Arial", 50, "bold"))
    pen1.penup()
    pen1.setpos(0, 0)
    pen1.pendown()
    pen1.write("Nice Try!", False, align="center", font=("Arial", 30, "bold"))
    pen1.penup()
    pen1.setpos(-20, -150)
    pen1.pendown()
    pen1.write("Points:", False, align="center", font=("Arial", 30, "bold"))
    pen1.penup()
    pen1.setpos(55, -150)
    pen1.pendown()
    pen1.write(points, False, align="left", font=("Arial", 30, "bold"))
    pen1.hideturtle()

while not var:
    screen.update()