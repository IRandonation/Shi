#coding=utf-8
import numpy as np
def Init_Cube():#分别是前0、后1、左2、右3、上4、下5
    Cube = np.array([(1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4),(5,5,5,5),(6,6,6,6)])
    return Cube

def Left_Turn(Cube):
    Cube = np.array([(Cube[0][0],Cube[5][1],Cube[0][2],Cube[5][3]),
                        (Cube[1][0],Cube[4][1],Cube[1][2],Cube[4][3]),
                        (Cube[2][0],Cube[2][1],Cube[2][2],Cube[2][3]),
                        (Cube[3][1],Cube[3][3],Cube[3][0],Cube[3][2]),
                        (Cube[4][0],Cube[0][1],Cube[4][2],Cube[0][3]),
                        (Cube[5][0],Cube[1][1],Cube[5][2],Cube[1][3])])
    return Cube

def Front_Turn(Cube):
    Cube = np.array([(Cube[0][1],Cube[0][3],Cube[0][0],Cube[0][2]),
                        (Cube[1][0],Cube[1][1],Cube[1][3],Cube[1][3]),
                        (Cube[5][0],Cube[2][1],Cube[5][2],Cube[2][3]),
                        (Cube[4][0],Cube[3][1],Cube[4][2],Cube[3][3]),
                        (Cube[2][0],Cube[4][1],Cube[2][2],Cube[4][3]),
                        (Cube[3][0],Cube[5][1],Cube[3][2],Cube[5][3])])
    return Cube

def Up_Turn(Cube):
    Cube = np.array([(Cube[0][0],Cube[0][1],Cube[3][2],Cube[3][3]),
                        (Cube[1][0],Cube[1][1],Cube[2][2],Cube[2][3]),
                        (Cube[2][0],Cube[2][1],Cube[0][2],Cube[0][3]),
                        (Cube[3][0],Cube[3][1],Cube[1][2],Cube[1][3]),
                        (Cube[4][1],Cube[4][3],Cube[4][0],Cube[4][2]),
                        (Cube[5][0],Cube[5][1],Cube[5][2],Cube[5][3])])
    return Cube

Cube = Init_Cube()
print(Cube)