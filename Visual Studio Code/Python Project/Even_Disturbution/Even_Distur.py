#coding=utf-8
import numpy as np
import random
import math
import matplotlib.pyplot as plt

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

def Fitness(Point,n):
    i = 0
    Dis = 0
    Dis_Min = 1
    Fit = 0
    for i in range(6):
        Dis = ((Point[i].X_Axis - Point[n].X_Axis)**2 + (Point[i].Y_Axis - Point[n].Y_Axis)**2)*0.5
        if ((Dis < Dis_Min) and (Dis != 0)):
            X_Min = Point[i].X_Axis
            Y_Min = Point[i].Y_Axis
            Dis_Min = Dis
            Flag = i

    # if (X_Min < Point[Flag].X_Axis and Y_Min > Point[Flag].Y_Axis):
    #     Y_Min = Point[Flag].Y_Axis
    # elif (X_Min > Point[Flag].X_Axis and Y_Min < Point[Flag].Y_Axis):
    #     X_Min = Point[Flag].X_Axis
    # elif (X_Min > Point[Flag].X_Axis and Y_Min > Point[Flag].Y_Axis):
    #     X_Min = Point[Flag].X_Axis
    #     Y_Min = Point[Flag].Y_Axis
    Area = 4*X_Min * Y_Min
    Fit = (((1/6 - Area)**2)**0.5)*10
    return Fit
    #print(point[n].Fit)

def Eliminate(Point):
    Point = sorted(Point, key = lambda Point: Point.Fit)
    for i in range(6):
        print(Point[i].Fit)
    Point[4].X_Axis = 0
    Point[4].Y_Axis = 0
    Point[4].Fit = 0
    Point[5].X_Axis = 0
    Point[5].Y_Axis = 0
    Point[5].Fit = 0
    for i in range(6):
        print(Point[i].Fit)
    return Point


def Breed(Point):
    Point[4].X_Axis = (Point[1].X_Axis + Point[2].X_Axis + Point[3].X_Axis)/3
    Point[4].Y_Axis = (Point[1].X_Axis + Point[2].Y_Axis + Point[3].Y_Axis)/3
    Point[5].X_Axis = (Point[0].X_Axis+Point[1].X_Axis)/2
    Point[5].Y_Axis = (Point[0].Y_Axis+Point[1].Y_Axis)/2
    Point[4].Fit = Fitness(Point,5)
    Point[5].Fit = Fitness(Point,4)   
    return Point




po = []
x = [0,0,0,0,0,0]
y = [0,0,0,0,0,0]
for i in range(6):
    po.append(Point())
po = Init_Point(po)
#print(po)
#print(po[2].X_Axis)
for k in range(20):
    po = Eliminate(po)
    po = Breed(po)
    print(po[0].Fit)
    print('*******')
#     # if (k%1000) == 0:
#     #     for f in range(6):
#     #         x[f] = po[f].X_Axis
#     #         y[f] = po[f].Y_Axis
#     #     plt.scatter(x, y, alpha=0.6)
#     #     plt.show()
#     # print(po[1].Fit)
#     # print('*******')
#     # print(po[2].Fit)
#     # print('*******')
#     # print('*******')
# for k in range(6):
#     x[k] = po[k].X_Axis
#     y[k] = po[k].Y_Axis
# plt.scatter(x, y, alpha=0.6)
# plt.axis([0,1,0,1])
# plt.show()




