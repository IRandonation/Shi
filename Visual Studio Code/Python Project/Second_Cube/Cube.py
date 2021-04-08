#coding=utf-8
import numpy as np 

isGo = True

def Init_Cube():#分别是前0、后1、左2、右3、上4、下5
    Cube = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6]])
    return Cube

def Left_Turn(Cube):
    Cube = np.array([[Cube[0][0],Cube[5][1],Cube[0][2],Cube[5][3]],
                        [Cube[1][0],Cube[4][1],Cube[1][2],Cube[4][3]],
                        [Cube[2][0],Cube[2][1],Cube[2][2],Cube[2][3]],
                        [Cube[3][1],Cube[3][3],Cube[3][0],Cube[3][2]],
                        [Cube[4][0],Cube[0][1],Cube[4][2],Cube[0][3]],
                        [Cube[5][0],Cube[1][1],Cube[5][2],Cube[1][3]]])
    return Cube

def Front_Turn(Cube):
    Cube = np.array([[Cube[0][1],Cube[0][3],Cube[0][0],Cube[0][2]],
                        [Cube[1][0],Cube[1][1],Cube[1][3],Cube[1][3]],
                        [Cube[5][0],Cube[2][1],Cube[5][2],Cube[2][3]],
                        [Cube[4][0],Cube[3][1],Cube[4][2],Cube[3][3]],
                        [Cube[2][0],Cube[4][1],Cube[2][2],Cube[4][3]],
                        [Cube[3][0],Cube[5][1],Cube[3][2],Cube[5][3]]])
    return Cube

def Up_Turn(Cube):
    Cube = np.array([[Cube[0][0],Cube[0][1],Cube[3][2],Cube[3][3]],
                        [Cube[1][0],Cube[1][1],Cube[2][2],Cube[2][3]],
                        [Cube[2][0],Cube[2][1],Cube[0][2],Cube[0][3]],
                        [Cube[3][0],Cube[3][1],Cube[1][2],Cube[1][3]],
                        [Cube[4][1],Cube[4][3],Cube[4][0],Cube[4][2]],
                        [Cube[5][0],Cube[5][1],Cube[5][2],Cube[5][3]]])
    return Cube

# -*- coding:utf-8 -*-

#魔方结构体
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.mid = None
        self.right = None
        self.oper = None
        
def Search(root,AimCube,mystack):
    global isGo
    mystack.append(root.oper)
    if isGo == False:
        return
    if not root:
        mystack.pop()
        return
    if (AimCube == root.val).all():
        print(root.val)
        mystack.pop()
        Mystack = mystack.reverse
        print(Mystack)
        print('Find!')
        isGo = False
        return
        
    else:
        Search(root.left,AimCube,mystack)
        Search(root.mid,AimCube,mystack)
        Search(root.right,AimCube,mystack)


'列表创建二叉树'
def listcreattree(root,i,Cube):###用列表递归创建魔方三叉树，
    if i<265720:
        root=TreeNode(i)
        #往左递推
        root.left=listcreattree(root.left,3*i+1,Cube = Left_Turn(Cube))
        root.val = Cube
        root.oper = 'L'
        root.mid=listcreattree(root.mid,3*i+2,Cube = Front_Turn(Cube))
        root.val = Cube
        root.oper = 'F'
        #往右回溯
        root.right=listcreattree(root.right,3*i+3, Cube = Up_Turn(Cube))
        root.val = Cube
        root.oper = 'U'
        #再返回根'
        return root  
    return root

def Aim():#设定目标魔方状态
    i = 0
    j = 0
    Line = [[0]*4]*6
    print(Line)
    for j in range(6):
        Line[j] = input("Please input").split(" ")
        Line[i] = [int(j) for j in Line [i]]
        i = i+1
    #print(Line)
    return Line


Cube = Init_Cube()#初始化魔方
Tree = listcreattree(None,0,Cube)
cube = Aim()
print('*********')
mystack = []
Search(Tree,cube,mystack)









