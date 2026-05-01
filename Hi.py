import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#Drew "HI"
pen.penup()         
pen.goto(-100, 0)
pen.pendown()   
pen.color(colors[0])
pen.write("HI", font=("Arial", 48, "bold"))

# Draw pattern
for i in range(120):
    pen.color(colors[i % 6])   # Cycle through colors
    pen.forward(i * 3)         # Increase step size
    pen.left(91)               # Slightly off 90° for spiral effect


Delay = 2000  # Delay in milliseconds
turtle.done()  

