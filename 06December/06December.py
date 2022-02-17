import numpy as np

def fileToArray(fileName):
    arr= np.array(([[],[]]), dtype=np.int32)
    with open(fileName, "r") as file:
        for line in file:
            arr = np.append(arr, line.split(","))

    arr = arr.astype('int32')
    return arr, len(arr)

def updateFish(arr, inLenArr):
    addFish = 0
    for fish in range(0, inLenArr):
        arr[fish] = (arr[fish] - 1) % 7
        if arr[fish] == 0:
            addFish += 1
    for fish in range(inLenArr, len(arr)):
        arr[fish] = (arr[fish] - 1) % 9
        if arr[fish] == 0:
            addFish += 1
    return arr, addFish

def addFish(arr, addFish):
    for fish in range(0, addFish):
        arr = np.append(arr, 9)
    return arr

filename = "input.txt"
arr, inLenArr = fileToArray(filename)
print(arr)
prevAdd = [0,0,0]
for i in range(0, 80):
    arr, adFish = updateFish(arr, inLenArr)
    # print('Day',i+1,'days: ', arr)
    print('Day',i+1,len(arr))
    arr = addFish(arr, adFish)

    temp = prevAdd[1]
    prevAdd[1] = prevAdd[2]
    prevAdd[0] = temp
    prevAdd[2] = adFish
    inLenArr += prevAdd[0]
