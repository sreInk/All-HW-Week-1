import turtle


pen = turtle.Turtle()

pen.speed(1)

# Draw a square
for _ in range(4):
    pen.forward(100) 
    pen.right(90)   

turtle.done()
