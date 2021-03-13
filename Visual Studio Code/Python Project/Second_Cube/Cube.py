#coding=utf-8
import numpy as np
def Init_Cube():#分别是前、后、左、右、上、下
    Cube = np.array([(1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4),(5,5,5,5),(6,6,6,6)])
    return Cube

def Left_Turn(Cube):
    Empty = np.array([Cube[0][1],Cube[0][3]])
    Cube = np.array([(Cube[0][0],cube[6][1],Cube[0][2],Cube[6][3])，
                        ])

Cube = Init_Cube()
Em = Left_Turn(Cube)
print(Em)