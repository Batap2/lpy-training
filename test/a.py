import turtle

# Define the L-system rules
rules = {
    'F': 'FF+[+F-F-F]-[-F+F+F]',
    '+': '+',
    '-': '-'
}

# Starting axiom and number of iterations
axiom = 'F'
iterations = 5

# Generate the L-system string
lsystem = axiom
for _ in range(iterations):
    lsystem = ''.join([rules.get(c, c) for c in lsystem])

# Set up the Turtle Graphics screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("L-System Tree")
t = turtle.Turtle()
t.speed(0)
t.color("green")

# Set initial position and angle
t.penup()
t.goto(0, -200)
t.setheading(90)
t.pendown()

# Define the drawing commands
length = 5  # Length of each line segment
angle = 22.5  # Turning angle in degrees

for char in lsystem:
    if char == 'F':
        t.forward(length)
    elif char == '+':
        t.right(angle)
    elif char == '-':
        t.left(angle)
    elif char == '[':
        t.penup()
    elif char == ']':
        t.pendown()

# Close the Turtle Graphics window on click
screen.exitonclick()
