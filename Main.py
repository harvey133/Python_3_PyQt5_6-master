#!/usr/bin/env python3
# coding=utf-8

import turtle

bob = turtle.Turtle()


def draw_bob(left_or_right, angle, length):
    if left_or_right == "right":
        bob.right(angle)
    else:
        bob.left(angle)

    bob.forward(length)


def draw_turtle(left_or_right, angle, length):
    if left_or_right == "right":
        turtle.right(angle)
    else:
        turtle.left(angle)

    turtle.forward(length)


# (1) --- Фронатальная сторона коробки ---
# Начинаем окрашивать фронатальную сторону коробки
bob.fillcolor("#BEBEBE")
bob.begin_fill()


draw_bob("left", 90, 70)
draw_bob("left", 90, 15)
draw_bob("left", 90, 70)
draw_bob("left", 45, 10)
draw_bob("left", 90, 10)
draw_bob("left", 180, 10)
draw_bob("left", -135, 15)
draw_bob("left", 90, 7)
draw_bob("left", 180, 14)
draw_bob("left", 90, 63)
draw_bob("left", -70, 10)
draw_bob("left", 90, 10)
draw_bob("left", 45, 15)
draw_bob("left",45, 12)
draw_bob("left", 45, 10)
draw_bob("left", 78, 15)
bob.end_fill()


turtle.done()
