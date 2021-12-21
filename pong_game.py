import turtle
import winsound

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stops the window from updating

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation
paddle_a.shape("square")  # the shape of the paddle
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # paddle size
paddle_a.penup()
paddle_a.goto(-350, 0)  # this is the starting point, 0 represents the middle(left)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation
paddle_b.shape("square")  # the shape of the paddle
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # paddle size
paddle_b.penup()
paddle_b.goto(350, 0)  # this is the starting point, 0 represents the middle(right)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape("square")  # the shape of the paddle
ball.color("yellow")
ball.penup()
ball.goto(0, 0)  # it starts from the middle of the screen
ball.mx = 2  # every time the ball moves, it moves by 2 pixels
ball.my = -2

# Pen
pen = turtle.Turtle()  # capital T is the class name
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 16, "italic"))

# Functions that move the paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20  # this add 20 pixels to the y coordinates
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20  # this subtract 20 pixels to the y coordinates
    paddle_a.sety(y)

# Functions that move the paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20  # this add 20 pixels to the y coordinates
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20  # this subtract 20 pixels to the y coordinates
    paddle_b.sety(y)

# Keyboard biding for paddle A
window.listen()  # keyboard commands, it tells the program to execute the user commands
window.onkeypress(paddle_a_up, "u")  # when the user press u (only lowercase), it call the function paddle_a_up
window.onkeypress(paddle_a_down, "d")  # when the user press d, paddle will go down

# Keyboard biding for paddle B
window.listen()  # keyboard commands, it tells the program to execute the user commands
window.onkeypress(paddle_b_up, "Up")  # here we use the arrow up key to move the paddle B
window.onkeypress(paddle_b_down, "Down")  # here we use the arrow down key

# Main game
while True:
    window.update()  # every time the loop runs, the screen will be updated

    # Move the ball
    ball.setx(ball.xcor() + ball.mx)
    ball.sety(ball.ycor() + ball.my)

    # Border checking (right)
    if ball.ycor() > 290:  # when the ball reaches 290 pixels(max. 300) we have to change the ball direction to the opposite corner
        ball.sety(290)
        ball.my *= -1  # this function reverses the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.my *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Border checking (left)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.mx *= -1
        score_a += 1  # if the ball goes off the right side of the screen Player A gets the point
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Arial", 16, "italic"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.mx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Arial", 16, "italic"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.mx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

