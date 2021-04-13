#coding=utf-8
import numpy as np
import random

class Point:
    def __init__(self):
        self.X_Axis = 0
        self.Y_Axis = 0
        self.Fit = 0

def Init_Point(point):
    i = 0
    for i in range(6):
        num1 = random.random()
        point[i].X_Axis = num1
        num2 = random.random()
        point[i].Y_Axis = num2 
    for j in range(6):
        point[j].Fit = Fitness(point,j)
        # print(point[j].Fit)
    return point

def Fitness(point,n):
    i = 0
    x_fit = 0
    y_fit = 0
    for i in range(6):
        x_fit = x_fit + pow((point[i].X_Axis-point[n].X_Axis),2)
        y_fit = y_fit + pow((point[i].Y_Axis-point[n].Y_Axis),2)
    Fit = (pow(point[n].X_Axis,2)+pow((1-point[n].X_Axis),2)+pow(point[n].Y_Axis,2)+pow((1-point[n].Y_Axis),2)+x_fit+y_fit)/8
    return Fit
    #print(point[n].Fit)

def Eliminate(Point):
    Point = sorted(Point, key = lambda Point: Point.Fit)
    # for i in range(6):
    #     print(Point[i].Fit)
    Point[4].X_Axis = 0
    Point[4].Y_Axis = 0
    Point[4].Fit = 0
    Point[5].X_Axis = 0
    Point[5].Y_Axis = 0
    Point[5].Fit = 0
    # for i in range(6):
    #     print(Point[i].Fit)
    return Point


def Breed(Point):
    Point[4].X_Axis = (Point[2].X_Axis+Point[3].X_Axis)/2
    Point[4].Y_Axis = (Point[2].Y_Axis+Point[3].Y_Axis)/2
    Point[5].X_Axis = (Point[0].X_Axis+Point[1].X_Axis)/2
    Point[5].Y_Axis = (Point[0].Y_Axis+Point[1].Y_Axis)/2
    Point[4].Fit = Fitness(Point,5)
    Point[5].Fit = Fitness(Point,4)   
    return Point




po = []
for i in range(6):
    po.append(Point())
po = Init_Point(po)
#print(po)
#print(po[2].X_Axis)
for k in range(3000):
    po = Eliminate(po)
    po = Breed(po)
    print(po[0].Fit)
    print('*******')
    print(po[1].Fit)





