import turtle

UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
SPACEBAR = 'Space'

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    return ("you pressed up")

def left():
    global direction
    direction = LEFT
    return("you pressed left")
def down():
    global direction
    direction = DOWN
    return ("you pressed down")

def right():
    global direction
    direction = RIGHT
    return("you pressed right")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()

turtle.mainloop()

