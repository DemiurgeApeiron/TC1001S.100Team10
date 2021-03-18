"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

limitex = 420
limitey = 420
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -limitex / 2 + 10 < head.x < limitex / 2 - 10 and -limitey / 2 + 10 < head.y < limitey / 2 - 10


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    if food.x < limitex / 2 - 10 and food.x > -limitex / 2 + 10:
        print(food.x)
        food.x += round(randrange(-1, 2)) * 10
    else:
        food.x += food.x / food.x * -10
    if food.y < limitey / 2 - 10 and food.y > -limitey / 2 + 10:
        print(food.y)
        food.y += round(randrange(-1, 2)) * 10
    else:
        food.y += food.y / food.y * -10

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)

    if head == food:
        print("Snake:", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, "black")

    square(food.x, food.y, 9, "green")
    update()
    ontimer(move, 100)
    print(f"snake {head.x} :: {head.y}")


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")
move()
done()
