import cv2
import numpy as np


def fileToArray(fileName):
    arrFold = np.array(([[],[]]), dtype=np.int32)
    yMax = xMax = 0
    with open(fileName, "r") as file:
        for line in file:
            if line != '\n':
                if line.find('=') < 0:
                    x, y = line.split(",")
                    if int(x) > xMax:
                        xMax = int(x)
                    if int(y) > yMax:
                        yMax = int(y)

    arr = np.full((yMax + 1, xMax + 1),'',  dtype=np.unicode_)
    with open(fileName, "r") as file:
        for line in file:
            if line != '\n':
                if line.find('=') > 0:
                    tempIs = line.find('=')+1
                    if line.find('x') > 0:
                        arrFold = np.append(arrFold,(0,int(line[tempIs:-1])))
                    if line.find('y') > 0:
                        arrFold = np.append(arrFold,(1,int(line[tempIs:-1])))
                else:
                    x, y = line.split(",")
                    arr[int(y)][int(x)]='#'
    return arr, arrFold


def foldy(arr, foldLine):
    yShape, xShape = np.shape(arr)
    tempArr = np.full((yShape-foldLine-1, xShape),'',  dtype=np.unicode_)

    for x in range(0, xShape):
        for y in range(1, yShape-foldLine):
            if foldLine - y > -1:
                tempArr[(yShape-foldLine-1)-y][x] = arr[foldLine-y][x] or arr[foldLine+y][x]
            else:
                tempArr[(yShape-foldLine-1)-y][x] = arr[foldLine+y][x]
    return tempArr


def foldx(arr, foldLine):
    yShape, xShape = np.shape(arr)
    tempArr = np.full((yShape, xShape-foldLine-1),'',  dtype=np.unicode_)

    for y in range(0, yShape):
        for x in range(1, xShape-foldLine):
            if foldLine - x > -1:
                tempArr[y][(xShape-foldLine-1)-x] = arr[y][foldLine-x] or arr[y][foldLine+x]
            else:
                tempArr[y][(xShape-foldLine-1)-x] = arr[y][foldLine+x]

    hashtagCount = 0
    for item in tempArr:
        for i in item:
            if i == '#':
                hashtagCount+=1
    print("Answer 1: ", hashtagCount)
    return tempArr



filename = "input.txt"
arr, arrFold = fileToArray(filename)
shape = np.shape(arrFold)
arrFold = np.reshape(arrFold, (int(shape[0]/2), 2))


for fold, foldLine in arrFold:
    if fold:
        arr = foldy(arr, foldLine)
    else:
        arr = foldx(arr, foldLine)
    # print('\n',arr)

arr = np.where(arr == '#', '255', arr)
arr = np.where(arr == '', '0', arr)
arr = arr.astype('uint8')
# print(np.shape(arr))
arr = cv2.resize(arr, (40*10, 6*10),
                     interpolation=cv2.INTER_AREA)
cv2.imshow('image', arr)
cv2.waitKey(0)
# print("Answer 2: \n", arr)
