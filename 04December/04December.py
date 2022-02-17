import numpy as np


def fileToArray(fileName):
    # (BingoCard, Row, Number/Checked, Collumn)
    tDimensions = (100, 5, 2, 5)
    arr = np.full(tDimensions, 0,  dtype=np.uint8)
    firstLine = 0
    i = -1
    j=0
    with open(fileName, "r") as file:
        for line in file:
            line = line[:-1]
            if firstLine == 0:
                firstLine=1
                instrList = list(map(int, line.split(",")))
            elif line == '':
                i+=1
                j=0
            else:
                arr[i][j][0] = list(map(int, (line.split())))
                j+=1
    return arr, instrList

def bingoCross(number, bingoArr):
    for bingoCard in range(0,len(bingoArr)):
        for row in range(0,5):
            for collumn in range(0,5):
                if bingoArr[bingoCard][row][0][collumn] == number:
                    bingoArr[bingoCard][row][1][collumn] = 1
    return bingoArr

def bingoCheck(bingoArr, first):
    bingo = False
    firstBingo = False
    firstBingoArr = 0
    for bingoCard in range(len(bingoArr)-1,-1,-1):
        for i in range(0,5):
            bingo = bingo or np.sum(bingoArr[bingoCard][i:i+1,1,0:5]) == 5
            bingo = bingo or np.sum(bingoArr[bingoCard][0:5,1,i:i+1]) == 5
            if bingo and first:
                # print(bingoArr[bingoCard][i:i+1,0:2,0:5], np.sum(bingoArr[bingoCard][i:i+1,1,0:5]))
                first = False
                firstBingoArr = bingoArr[bingoCard]
                bingoArr = np.delete(bingoArr, bingoCard, 0)
                firstBingo = True
                bingo = 0
                bingoCard-=1
            elif bingo:
                bingo = 0
                bingoArr = np.delete(bingoArr, bingoCard, 0)
                bingoCard-=1

    # print(bingoArr[0][0:5,1,i:i+1],np.sum(bingoArr[0][0:5,1,i:i+1])==5)
    return firstBingo, firstBingoArr, bingoArr

filename  = "input.txt"

bingoArr, bingoNumberList = fileToArray(filename)
# print(len(bingoArr))
first = True
for number in range(0, len(bingoNumberList)):
    bingoArr = bingoCross(bingoNumberList[number], bingoArr)
    bingo, firstBingoArr, bingoArr =  bingoCheck(bingoArr, first)
    if bingo and first:
        first = False
        answer1 = 0
        for row in range(0,5):
            for column in range(0,5):
                if firstBingoArr[row][1][column] == 0:
                    answer1 += firstBingoArr[row][0][column]
        print("Answer 1: ", answer1, "*", number,"=", answer1*bingoNumberList[number])
    if len(bingoArr) == 1:
        break


for number in range(number, len(bingoNumberList)):
    bingoArr = bingoCross(bingoNumberList[number], bingoArr)
    answer2 = 0
    if bingo == False:
        for i in range(0,5):
            bingo = bingo or np.sum(bingoArr[0][i:i+1,1,0:5]) == 5
            bingo = bingo or np.sum(bingoArr[0][0:5,1,i:i+1]) == 5

    if bingo:
        for row in range(0,5):
            for column in range(0,5):
                if bingoArr[0][row][1][column] == 0:
                    answer2 += bingoArr[0][row][0][column]
        print("Answer 2: ", answer2, "*", bingoNumberList[number],"=", answer2 * bingoNumberList[number])
        break
