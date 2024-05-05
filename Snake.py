import turtle as t
import time
import random as r

screen = t.Screen()
screen.title('Игра Змейка')
screen.setup(width = 700, height = 700)
screen.tracer(0)
t.bgcolor('turquoise')

t.speed(5)
t.pensize(4)
t.penup()
t.goto(-310, 250)
t.pendown()
t.color('black')
t.forward(600)
t.right(90)
t.forward(500)
t.right(90)
t.forward(600)
t.right(90)
t.forward(500)
t.penup()
t.hideturtle()

snake = t.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

tail = []

fruit = t.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

score = 0
delay = 0.1

scoring = t.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Очки: ", align = "center", font = ("Courier", 24, "bold"))

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

while True:
    screen.update()
    if snake.distance(fruit) < 20:
        x = r.randint(-290, 270)
        y = r.randint(-240, 240)
        fruit.goto(x,y)
        scoring.clear()
        score += 1
        scoring.write("Счёт:{}".format(score), align = "center", font = ("Courier", 24, "bold"))
        delay -= 0.001

        new_fruit = t.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('red')
        new_fruit.penup()
        tail.append(new_fruit)

    for index in range(len(tail) -1, 0, -1):
        a = tail[index - 1].xcor()     
        b = tail[index - 1].ycor()

        tail[index].goto(a, b)

    if len(tail) > 0:
        a = snake.xcor()  
        b = snake.ycor()    
        tail[0].goto(a, b)
    snake_move()

    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0, 0)
        scoring.write("   Game Over \n Ваш Счёт {}".format(score), align = "center", font = ("Courier", 30, "bold"))

    for food in tail:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write("   Game Over \n Ваш Счёт {}".format(score), align = "center", font = ("Courier", 30, "bold"))
    time.sleep(delay)

t.mainloop()
