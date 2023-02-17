#Clear screen function
import os
def clear(): #clear screen
    os.system('cls' if os.name =='nt' else 'clear')


#Functions for final
def welcome():
    print(""" 
___________________________________
Welcome to the:

Python Mart Online Cashier System

\x1B[3m" It runs "\x1B[0m
___________________________________
""")

def gst(sub):
    total = sub * 1.05
    return total

import random
def discount(add):
    disc = random.choice([0.7, 0.8, 0.9])
    sub = add * disc
    return sub

import turtle
def logo():
    l = turtle.Screen()
    t = turtle.Turtle()
    #Settings
    t.speed(0)
    t.pensize(5)
    t.pencolor("black")
    t.fillcolor("dark red")
    t.hideturtle()
    #Drawing
    t.up()
    t.goto(155.72, 0)
    t.down()
    t.begin_fill()
    t.rt(105)
    t.fd(100)    
    t.circle(-30,75)
    t.fd(200)
    t.circle(-30,75)
    t.fd(100)
    t.end_fill()
    t.up()
    t.rt(105)
    t.fd(154)
    t.down()
    for x in range(2):
        t.fd(165)
        t.circle(10,90)
        t.fd(10)
        t.circle(5,90)
        t.fd(165)
    
    t.up()
    t.lt(90)
    t.fd(11)
    t.rt(45)
    t.fd(5)
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    for x in range(2):
        t.fd(200)
        t.circle(10,180)
    t.end_fill()
    t.up()
    t.goto(0,0)
    t.rt(135)
    t.fd(59)
    t.fd(5)
    t.down()
    c = "yellow"
    for x in range(2):
        t.fillcolor(c)
        t.begin_fill()
        t.lt(90)
        t.fd(20)
        t.circle(10, 90)
        t.fd(10)
        t.rt(90)
        t.fd(13)
        t.rt(45)
        t.circle(-25,90)
        t.rt(45)
        t.fd(30)
        t.lt(90)
        t.fd(8)
        t.lt(90)
        t.fd(10)
        t.rt(90)
        t.fd(7)
        t.rt(45)
        t.circle(-25,90)
        t.rt(45)
        t.fd(20)
        t.circle(-10, 90)
        t.fd(8)
        t.end_fill()
        t.up()
        t.lt(90)
        t.fd(10)
        t.down()
        c = "blue"
    t.up()
    t.goto(0, -200)
    t.down()
    t.write("Python Mart", align="center", font=("Comic Sans MS", 30, "normal"))
    l.exitonclick()
logo()