from turtle import Turtle
t = Turtle()
def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)
if __name__ == "__main__":
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    length = 300
    level = 2
    koch_snowflake(t, length, level)
