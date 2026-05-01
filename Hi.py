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


Delay = 2000  # Delay in milliseconds
turtle.done()   

