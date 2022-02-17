import numpy as np

def fileToArray(fileName):
    arrTemp= np.array(([]))
    arr= np.full(9, 0,  dtype=np.uint64)
    with open(fileName, "r") as file:
        for line in file:
            line = line[:-1]
    arrTemp = np.append(arrTemp, line.split(","))
    unique, counts = np.unique(arrTemp, return_counts=True)
    for i in range(0, len(unique)):
        arr[int(unique[i])]=counts[i]
    return arr

def updateFish(arr):
    temp = arr[0]
    for fish in range(1, 9):
        arr[fish-1] = arr[fish]
    arr[6] += temp
    arr[8] = temp
    return arr

filename = "input.txt"
arr = fileToArray(filename)

for i in range(0, 256):
    arr = updateFish(arr)
    if i == 79:
        print('Day',i+1,'days: ', np.sum(arr[0:9]))
print('Day',i+1,'days: ', np.sum(arr[0:9]))
