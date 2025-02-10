import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

"""it extracts the colors of an image """
# rgb_colors = []
# colors = colorgram.extract("image.jpg",40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


color_list = [
 (236, 212, 109), (25, 108, 188), (229, 143, 78),(119, 91, 54), (219, 57, 85), (240, 119, 151),
 (144, 167, 184), (111, 100, 195), (73, 124, 109), (188, 49, 91),(212, 9, 28), (140, 179, 8), (35, 187, 106),
 (235, 46, 35), (108, 175, 136), (30, 54, 121), (193, 177, 231),(136, 221, 152), (8, 173, 186),
 (121, 210, 241), (86, 31, 35), (35, 41, 83), (237, 161, 179), (176, 28, 26),(80, 34, 32), (240, 168, 158),
 (87, 89, 29), (249, 9, 32)]


t.colormode(255)

casper = t.Turtle()
casper.penup()
casper.hideturtle()
casper.setheading(225)
casper.forward(300)
casper.setheading(0)
number_of_dots = 100
casper.speed("fastest")


for dot_counts in range(1, number_of_dots + 1):
    casper.dot(20, random.choice(color_list))
    casper.forward(50)

    if dot_counts % 10 == 0:
        casper.setheading(90)
        casper.forward(50)
        casper.setheading(180)
        casper.forward(500)
        casper.setheading(0)







screen = t.Screen()
screen.exitonclick()
