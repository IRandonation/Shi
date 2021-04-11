#coding=utf-8
import numpy as np
import random

class Point:
    def __init__(self):
        self.X_Axis = 0
        self.Y_Axis = 0
        self.Fit = 0

def Init_Point(point):
    for i in range(6):
        point[i].X_Axis = random.random()
        point[i].Y_Axis = random.random()
        point[i].Fit = Fitness(point,i)

def Fitness(point,n):
    i = 0
    x_fit = 0
    y_fit = 0
    for i in range(6):
        x_fit = x_fit + pow((point[i].X_Axis-point[n].X_Axis),2)
        y_fit = y_fit + pow((point[i].Y_Axis-point[n].Y_Axis),2)
    Fit = (pow(point[n].X_Axis,2)+pow((1-point[n].X_Axis),2)+pow(point[n].Y_Axis,2)+pow((1-point[n].Y_Axis),2)+x_fit+y_fit)/8
    point[n].Fit = Fit
    print(point[n].Fit)


#def Eliminate(Point):


#def Breed(Point):




po = [Point()]*9
Init_Point(po)
#print(po[2].X_Axis)
#print(po[2].Fit)




