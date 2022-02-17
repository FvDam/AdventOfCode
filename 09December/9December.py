import cv2
import numpy as np


area = 0
black = (0, 0, 0)
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
yellow = (0, 255, 255)
white = (255, 255, 255)


def updateDisplay(arr, wait=1, size=(1000, 1000)):
    arrTemp = cv2.resize(arr, size,
                         interpolation=cv2.INTER_AREA)
    cv2.imshow('image', arrTemp)
    cv2.waitKey(wait)


# A recursive function to replace
# previous color 'prevC' at '(x, y)'
# and all surrounding pixels of (x, y)
# with new color 'newC' and
def floodFillUtil(screen, x, y, prevC, newC, draw):
    global area
    # Base cases
    if (x < 0 or x >= 100 or y < 0 or y >= 100
       or (not (screen[x][y] == prevC).all())
            or (screen[x][y] == newC).all()):
        return
    area += 1

    # Replace the color at (x, y)
    screen[x][y] = newC
    if draw:
        updateDisplay(screen, 1)
    # Recur for north, east, south and west
    floodFillUtil(screen, x + 1, y, prevC, newC, draw)
    floodFillUtil(screen, x - 1, y, prevC, newC, draw)
    floodFillUtil(screen, x, y + 1, prevC, newC, draw)
    floodFillUtil(screen, x, y - 1, prevC, newC, draw)


# It mainly finds the previous color on (x, y) and
# calls floodFillUtil()
def floodFill(screen, x, y, newC, draw=1):
    newC = np.asarray(newC, dtype=np.uint8)
    prevC = white

    if (prevC == newC).all():
        return

    floodFillUtil(screen, x, y, prevC, newC, draw)


def fileToArray(fileName, filter=10):
    arr = np.full(
        (100, 100, 3), 255,  dtype=np.uint8)
    i = 0
    with open(fileName, "r") as file:
        for line in file:
            # li=list(line.split(","))
            input_line_list = list(line[:-1])
            arr2 = np.array(
                [(9-int(i))*28 for i in input_line_list],  dtype=np.uint8)

            if filter != 10:
                for j in range(0, 100):
                    if arr2[j] == (9-filter)*28:
                        arr2[j] = 0
                    else:
                        arr2[j] = 255
            arr2 = np.reshape(arr2, (100, 1))
            arr[i] = arr2
            i += 1
            updateDisplay(arr)
        updateDisplay(arr, 0)
        return arr


filename = "input.txt"

pixel_array = fileToArray(filename)

arrTemp = pixel_array
arrOriginal = np.copy(pixel_array)
arrLowCoordinates = np.array([],  dtype=np.uint8)
Answer = 0

for i in range(0, 100):
    for j in range(0, 100):
        arrTemp = pixel_array

        lowestBool = 1
        if i > 0:
            lowestBool = lowestBool & (
                arrOriginal[i][j][0] > arrOriginal[i-1][j][0])
        if i < 99:
            lowestBool = lowestBool & (
                arrOriginal[i][j][0] > arrOriginal[i+1][j][0])
        if j > 0:
            lowestBool = lowestBool & (
                arrOriginal[i][j][0] > arrOriginal[i][j-1][0])
        if j < 99:
            lowestBool = lowestBool & (
                arrOriginal[i][j][0] > arrOriginal[i][j+1][0])

        if lowestBool and arrOriginal[i][j][0] != 0:
            pixel_array[i][j] = green
            arrLowCoordinates = np.append(arrLowCoordinates, (i, j))
            Answer += 9-((arrOriginal[i][j][0])/28)+1
            updateDisplay(pixel_array, 1)

arrLowCoordinates = np.reshape(arrLowCoordinates, (242, 2))
np.random.shuffle(arrLowCoordinates)
updateDisplay(pixel_array, 0)
print("Answer 1: ", Answer)

for i in range(0, 100):
    for j in range(0, 100):
        if pixel_array[i][j][0] != 0:
            pixel_array[i][j] = white

updateDisplay(pixel_array, 0)

pixel_array = fileToArray(filename, 9)
arrTemp = np.copy(pixel_array)
arrOriginal = np.copy(pixel_array)
max1, max2, max3 = 0, 0, 0
result = np.array([[0, 0], [0, 0], [0, 0]], dtype=np.uint8)

for cor in arrLowCoordinates:
    area = 0
    pixel_array = np.copy(arrTemp)
    floodFill(pixel_array, cor[0], cor[1], black)
    if area >= max1 and area < max2:
        max1 = area
        result[0] = cor
        arrTemp = np.copy(arrOriginal)
        floodFill(arrTemp, result[0][0], result[0][1], green, 0)
        floodFill(arrTemp, result[1][0], result[1][1], blue, 0)
        floodFill(arrTemp, result[2][0], result[2][1], red, 0)
        updateDisplay(arrTemp)
    elif area >= max2 and area < max3:
        max1 = max2
        max2 = area
        result[0] = result[1]
        result[1] = cor
        arrTemp = np.copy(arrOriginal)
        floodFill(arrTemp, result[0][0], result[0][1], green, 0)
        floodFill(arrTemp, result[1][0], result[1][1], blue, 0)
        floodFill(arrTemp, result[2][0], result[2][1], red, 0)
        updateDisplay(arrTemp)
    elif area >= max3:
        max1 = max2
        max2 = max3
        max3 = area
        result[0] = result[1]
        result[1] = result[2]
        result[2] = cor
        arrTemp = np.copy(arrOriginal)
        floodFill(arrTemp, result[0][0], result[0][1], green, 0)
        floodFill(arrTemp, result[1][0], result[1][1], blue, 0)
        floodFill(arrTemp, result[2][0], result[2][1], red, 0)
        updateDisplay(arrTemp)

print("Answer 2: ", max1, "*", max2, "*",
      max3, " = ", max1 * max2 * max3)
pixel_array = np.copy(arrOriginal)
for cor in result:
    floodFill(pixel_array, cor[0], cor[1], black)

arrTemp = cv2.resize(pixel_array, (1000, 1000),
                     interpolation=cv2.INTER_AREA)
cv2.imshow('image', arrTemp)
cv2.waitKey(0)

cv2.destroyAllWindows()
