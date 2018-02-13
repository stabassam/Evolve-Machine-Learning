#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:15:16 2018

@author: stabassam
"""

import turtle

        
def draw_s(turtle):
    turtle.pendown()
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    reset_turtle_state(turtle)

    
def draw_t(turtle):
    turtle.pendown()
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(100)
    reset_turtle_state(turtle)
    
    
def reset_turtle_state(turtle):
    turtle.penup()
    turtle.home()


def setup_turtle():
    
    window = turtle.Screen()
    window.bgcolor("black")
    
    my_turtle = turtle.Turtle()
    my_turtle.color("white")
    my_turtle.pensize(3)
    my_turtle.speed(10)
    my_turtle.penup()
    
    return my_turtle
    
    
def draw_initials(turtle):
    draw_s(turtle)
    turtle.forward(50)
    draw_t(turtle)


draw_initials(setup_turtle())