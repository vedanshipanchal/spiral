import turtle

pen = turtle.Screen()
pen.bgcolor("green")
pen.title("spiral pattern")

cursor = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        cursor.fd(size+1)
        cursor.left(90)
        size = size - 5
    size = size + 1