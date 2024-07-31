import turtle

windo = turtle.Screen()
windo.title("Hello, it's me")
windo.bgcolor("black")
windo.setup(width=800, height=600)
windo.tracer(0) #stops the window from updating, speeds up the game

#score
score_a = 0
score_b = 0


#paddle A

paddle_a = turtle.Turtle()  #small t is the module, big t is the class
paddle_a.speed(0)   #speed of the animation, maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.x_change = 0.1
bola.y_change = 0.1

#pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 20, "bold"))

#functions
def paddle_a_up():
    y = paddle_a.ycor() #returns the y coordinate
    y += 20    #increases when you go up, decreases when you go down
    paddle_a.sety(y)    #paddle a set y to the new y

def paddle_a_down():
    y = paddle_a.ycor() #returns the y coordinate
    y -= 20    #increases when you go up, decreases when you go down
    paddle_a.sety(y)    #paddle a set y to the new y

def paddle_b_up():
    y = paddle_b.ycor() #returns the y coordinate
    y += 20    #increases when you go up, decreases when you go down
    paddle_b.sety(y)    #paddle a set y to the new y

def paddle_b_down():
    y = paddle_b.ycor() #returns the y coordinate
    y -= 20    #increases when you go up, decreases when you go down
    paddle_b.sety(y)    #paddle a set y to the new y

#keyboard binding
windo.listen()  #listen to keyboard input
windo.onkeypress(paddle_a_up, "Up")
windo.onkeypress(paddle_a_down, "Down")
windo.onkeypress(paddle_b_up, "w")
windo.onkeypress(paddle_b_down, "s")


#main game loop
while True:     #while true the window of the game will update
    windo.update()

    #move the ball
    bola.setx(bola.xcor() + bola.x_change)
    bola.sety(bola.ycor() + bola.y_change)
    
    #border checking
    if bola.ycor() > 290:
        bola.sety(290)
        bola.y_change *= -1 #reverse the direction

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.y_change *= -1 #reverse the direction
    
    if bola.xcor() > 350:
        bola.goto(0, 0)
        bola.x_change *= -1
        score_a += 1
        pen.clear() #cleans the score so that it doesn't print on the same place as the old score
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
    
    if bola.xcor() < -350:
        bola.goto(0, 0)
        bola.x_change *= -1
        score_b += 1
        pen.clear() #cleans the score so that it doesn't print on the same place as the old score
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))

    
    #paddle and ball collision
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paddle_b.ycor() + 40 and bola.ycor() > paddle_b.ycor() - 40):   #if it touches on the edges and the top and bottom of the paddle
        bola.setx(340)  
        bola.x_change *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paddle_a.ycor() + 40 and bola.ycor() > paddle_a.ycor() - 40):   #if it touches on the edges and the top and bottom of the paddle
        bola.setx(-340)  
        bola.x_change *= -1