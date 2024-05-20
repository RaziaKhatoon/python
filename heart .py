import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("red")

# Create a turtle object
my_turtle = turtle.Turtle()
my_turtle.speed(50)

# Draw a spiral
for i in range(100):
    my_turtle.stright(i)
    my_turtle.back(98)

# Close the window on click
win.exitonclick()