# import turtle library
import random
import turtle
turtle.tracer(0)

# setup the screen and add pictures
screen = turtle.Screen()
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.bgpic("background.png")
screen.addshape('battleship.gif')
screen.addshape('enemy.gif')
screen.addshape('bullet.gif')

# put the battleship on the screen
ship = turtle.Turtle()
ship.shape('battleship.gif')
ship.speed(0)
ship.penup()
ship.setpos(0, -263)
# functions to move the battle ship
def ship_left():
    x = ship.xcor()
    x -= 25 # move the ship 25 pixels
    if x < -364:
        x = -364
    ship.setx(x)

def ship_right():
    x = ship.xcor()
    x += 25 # move the ship 25 pixels
    if x > 360:
        x = 360
    ship.setx(x)


# put one enemy on the screen
enemy = turtle.Turtle()
enemy.shape('enemy.gif')
enemy.penup()
enemy.speed(0)
enemy.setpos(-300, 250)
# the speed of the enemy in a variable
enemyspeed = 0.15

# put five enemies on the screen
# num_enemies = 5
# enemies = []
# for i in range(num_enemies):
#     enemies.append(turtle.Turtle())

# make the battleship move by listening to user input
screen.listen()
screen.onkeypress(ship_left, "Left") # "Left" means left arrow
screen.onkeypress(ship_right, "Right") # "Right" means right arrow


# main loop for the game
var = True
while var:
    # move the enemy
    x = enemy.xcor()
    x += enemyspeed # move the enemy 0.15 pixels
    enemy.setx(x)
    # move the enemy back and down
    if enemy.xcor() > 360 :
        y = enemy.ycor()
        y -= 45 # change the position of the enemy down 45 pixels
        enemyspeed *= -1 # so the enemy moves back the other way
        enemy.sety(y) # move the enemy down

    if enemy.xcor() < -368 :
        y = enemy.ycor()
        y -= 45
        enemyspeed *= -1 # - and - make a positive
        enemy.sety(y)

    screen.update()
