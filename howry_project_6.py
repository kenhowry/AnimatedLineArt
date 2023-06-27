"""
Creating Animated Line Art

File Name: howry_project_6.py
Author: Ken Howry
Date: 22.10.21
Course: COMP 1351
Assignment: Project VI
Collaborators: N/A
Internet Source: N/A
"""
from random import random, randint
import dudraw
dudraw.set_canvas_size(500, 500)
dudraw.clear(dudraw.WHITE)

#lists
x_coor = []
y_coor = []
x_speed=[]
y_speed=[]

#appending random points
for k in range(10):
    x_coor.append(random())
    y_coor.append(random())
    x_speed.append(random()*.03)
    y_speed.append(random()*.03)

#animation
for l in range(100):
    dudraw.clear_rgb(235, 190, 232)
    dudraw.set_pen_width(.005)
    dudraw.set_pen_color_rgb(randint(0,255), randint(0,255), randint(0,255))
    #creating the 10 lines
    for i in range(9):
        if i < 8:
            dudraw.line(x_coor[i], y_coor[i], x_coor[i+1], y_coor[i+1])
        else:
            dudraw.line(x_coor[i], y_coor[i], x_coor[0], y_coor[0])

    #movement of the lines
    for j in range(len(x_coor)):
        x_coor[j]+=x_speed[j]
        y_coor[j]+=y_speed[j]

    #check collision with boundary
    for j in range(len(x_coor)):
        if x_coor[j] >= 1 or x_coor[j] <= 0:
        #reverse direction by changing the velocity sign
            x_speed[j] *= -1
        if y_coor[j] >= 1 or y_coor[j] <= 0:
        #reverse direction by changing the velocity sign
            y_speed[j] *= -1

    dudraw.show(100)