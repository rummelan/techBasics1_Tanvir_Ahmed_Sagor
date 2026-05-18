# generative_art.py
# Assignment 3 - Generative Art

import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)

artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()
artist.pensize(2)

# List of colors
colors = [
    "red", "orange", "yellow",
    "green", "cyan", "blue",
    "purple", "magenta", "white"
]

# Nested loops
for x in range(-300, 301, 100):
    for y in range(-300, 301, 100):

        artist.penup()
        artist.goto(x, y)
        artist.pendown()

        # Random values
        sides = random.choice([3, 4, 5, 6])
        size = random.randint(20, 60)
        color = random.choice(colors)

        artist.color(color)

        # Conditional statement
        if sides % 2 == 0:
            artist.fillcolor(random.choice(colors))
            artist.begin_fill()

        # Draw shape
        for i in range(sides):
            artist.forward(size)
            artist.left(360 / sides)

        if sides % 2 == 0:
            artist.end_fill()

        # Random circle decoration
        artist.penup()
        artist.goto(x, y)
        artist.pendown()

        artist.color(random.choice(colors))
        artist.circle(random.randint(10, 40))

turtle.done()
