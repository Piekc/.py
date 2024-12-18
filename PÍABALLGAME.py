#setup del modulo de la ventana
from turtle import*

#setup de los vectores
from freegames import vector

#Definir func (necesita indentacion)
def moveball(ball_1, ballspeed_1, barleft, barright, count, countgay) :
    ball_1 += ballspeed_1
    
    if ball_1.x >= 210 or ball_1.x <= -210:
        ballspeed_1.x *= -1
    if ball_1.y >= 210 or ball_1.y <= -210:
        ballspeed_1.y *= -1
    
    if (ball_1.x <= barleft.x + 10) and (barleft.y -50 <= ball_1.y <= barleft.y):
        ballspeed_1.x *= -1
        count += 1
        
    if (barright.x <= ball_1.x <= barright.x + 10) and (barright.y -50 <= ball_1.y <= barright.y):
        ballspeed_1.x *= -1
        countgay += 1
    
    return ball_1, ballspeed_1, count, countgay

def movebar(barposition, amount):
    barposition.y += amount
    
def movebargay(bargayposition, amount):
    bargayposition.y += amount

def draw(ball):
    goto(ball.x,ball.y)
    dot(20, 'purple')

def drawrectangle(position, width, height):
    up()
    goto(position.x, position.y)
    down()
    
    begin_fill()
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    end_fill()
    up()
    
def drawrectangay(position, width, height):
    up()
    goto(position.x, position.y)
    down()
    
    begin_fill()
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    end_fill()
    up()

def move(ball_1, ballspeed_1, barleft, barright, count, countgay):
    clear()
    ball_1, ballspeed_1, count, countgay = moveball(ball_1, ballspeed_1, barleft, barright, count, countgay)
    draw(ball_1)
    drawrectangle(barleft, 10, 50)
    drawrectangay(barright, 10, 50)
    
    up()
    color("black")
    goto(-70, 150)
    text = "Score:" + str(count)
    write(text, font=("Arial", 24, "normal"))
    
    up()
    color("black")
    goto(-20, -150)
    text = "Score:" + str(countgay)
    write(text, font=("Arial", 24, "normal"))
    
    ontimer(lambda: move(ball_1, ballspeed_1, barleft, barright, count, countgay), 30)
    
def main():
    #Posicion de la pelota
    ball_1 = vector(0,0)
    #Velocidad de la pelota
    ballspeed_1 = vector(5,2)
    #Posicion de la barra
    barleft = vector(-200, 25)
    barright = vector(180, 25)
    #Configura la ventana, (dimension, posicion)
    count = 0
    countgay = 0
    setup(420,420,500,200)
    hideturtle()
    up()
    tracer(0)
    listen()
    onkeypress(lambda: movebar(barleft, 10), 'w')
    onkeypress(lambda: movebar(barleft, -10), 's')
    onkeypress(lambda: movebargay(barright, 10), 'o')
    onkeypress(lambda: movebargay(barright, -10), 'l')
    move(ball_1, ballspeed_1, barleft, barright, count, countgay)
    done()
main()