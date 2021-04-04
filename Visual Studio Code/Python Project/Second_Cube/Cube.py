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

# -*- coding:utf-8 -*-

'二叉树结点类'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.mid = None
        self.right = None
        
def Search(root,AimCube):
    if not root:
        return
    if (AimCube == root.val).all():
        print(root.val)
        print('true')
        return
    else:
        print(root.val)
        Search(root.left,AimCube)
        Search(root.mid,AimCube)
        Search(root.right,AimCube)
    print('false')

'列表创建二叉树'
def listcreattree(root,i,Cube):###用列表递归创建二叉树，
    #它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
    #再接着创建b的右子树，
    if i<13:
        root=TreeNode(i)
        print('列表序号：'+str(i)+str(Cube[0]))
        #往左递推
        root.left=listcreattree(root.left,3*i+1,Cube = Left_Turn(Cube))
        root.val = Cube
        root.mid=listcreattree(root.mid,3*i+2,Cube = Front_Turn(Cube))
        root.val = Cube
        #往右回溯
        root.right=listcreattree(root.right,3*i+3, Cube = Up_Turn(Cube))
        root.val = Cube
        #再返回根'
        print('************返回根')
        return root  ###这里的return很重要
    return root



Cube = Init_Cube()
Cube1 = Left_Turn(Cube)
Tree = listcreattree(None,0,Cube)

print(Cube1)
print('*********')

Search(Tree,Cube1)










