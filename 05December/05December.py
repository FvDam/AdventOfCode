import cv2
import numpy as np


def fileToArray(fileName):
    arr= np.array(([[],[]]), dtype=np.int32)
    yMax = xMax = 0
    with open(fileName, "r") as file:
        for line in file:
            x, y = line.split("->")
            x = x.split(',')
            y = y.split(',')
            y[1]=y[1][:-1]
            if int(x[0]) > xMax:
                xMax = int(x[0])
            if int(y[1]) > yMax:
                yMax = int(y[1])
            arr = np.append(arr,[x,y])
    arr = np.reshape(arr, (int(len(arr)/4), 2, 2))
    arr = arr.astype('int32')
    return arr, (xMax+1, yMax+1)

def fSign(x):
    if x > 0:
        return 1.
    elif x < 0:
        return -1.
    elif x == 0:
        return 0.
    else:
        return x

def drawline(arr, instr, answer2 = False):
    if abs((instr[1][0]-instr[0][0])) > 0:
        slope = (instr[1][1]-instr[0][1])/(instr[1][0]-instr[0][0])
        len = instr[1][0]-instr[0][0]
        sign = fSign(len)
    else:
        slope = 2
        len = instr[1][1] - instr[0][1]
        sign = fSign(len)

    if slope == 0 or slope == -0:
        for i in range(0, abs(len)+1):
            y=int(instr[0][1])
            x=int(instr[0][0]+sign*i)
            arr[y][x] += 1
    elif (slope == 1 or slope == -1) and answer2:
        signx = fSign(instr[1][0]-instr[0][0])
        signy = fSign(instr[1][1]-instr[0][1])
        for i in range(0, abs(len)+1):
            y=int(instr[0][1]+signy*i)
            x=int(instr[0][0]+signx*i)
            arr[y][x] += 1
    elif slope == 2:
        for i in range(0, abs(len)+1):
            y=int(instr[0][1]+sign*i)
            x=int(instr[0][0])
            arr[y][x] += 1


filename = "input.txt"
arrInst, arrDim = fileToArray(filename)
arr = np.full(arrDim, 0,  dtype=np.int32)

for instruction in arrInst:
    drawline(arr, instruction)

answer1 = 0
for x in arr:
    for y in x:
        if y > 1:
            answer1+=1

print("Answer 1: ",answer1)

arr = np.full(arrDim, 0,  dtype=np.int32)
for instruction in arrInst:
    drawline(arr, instruction, True)
# print(arr)
answer2 = 0
for x in arr:
    for y in x:
        if y > 1:
            answer2+=1

print("Answer 2: ",answer2)
