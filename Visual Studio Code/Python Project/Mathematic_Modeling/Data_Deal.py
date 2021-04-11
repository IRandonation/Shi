import os
import numpy as np
import sys
import operator
from functools import reduce
i =0
result=[]
res = [0]*9
with open("Visual Studio Code/Python Project/Mathematic_Modeling/Data.txt","r") as f:
	for line in f:
		result.append(list(line.strip('\n').strip(',')))

for i in range(9):
    res[i] = result[i][0]
res = list(map(int, res))
print(res)
