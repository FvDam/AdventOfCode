import numpy as np

fileName = "input.txt"
arr = np.array([], dtype=bool)
with open(fileName, "r") as file:
    for line in file:
        for letter in line:
            if letter != '\n':
                arr = np.append(arr,int(letter))

shape = np.shape(arr)
arr = np.reshape(arr, (int(shape[0]/12), 12))
arrCO2 = np.copy(arr)
new = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = ['0','0','0','0','0','0','0','0','0','0','0','0']
epsilon = ['0','0','0','0','0','0','0','0','0','0','0','0']
lines = 0
for line in arr:
    lines+=1
    i=0
    for element in line:
        new[i] += element
        i+=1

i=0
for element in new:
    if element > int(lines/2):
        gamma[i]='1'
        epsilon[i]='0'
    else:
        gamma[i]='0'
        epsilon[i]='1'
    i+=1
gamma = ''.join([str(elem) for elem in gamma])
epsilon = ''.join([str(elem) for elem in epsilon])

print("Answer 1: ", int(gamma,2) * int(epsilon,2))
# print(len(arr))

for i in range(0, 12):
    lines = 0
    counter = 0
    for element in arr:
        lines+=1
        if element[i]:
            counter+=1

    for j in range(len(arr)-1, -1, -1):
        if len(arr) == 1:
            break
        if counter*2<lines and arr[j][i] == 1:
            arr = np.delete(arr, j, 0)
        elif counter*2>lines and arr[j][i] == 0 or counter*2==lines and arr[j][i] == 0:
            arr = np.delete(arr, j, 0)
    # print(arr,'\n\n')

# print("arrCO2")
for i in range(0, 12):
    lines = 0
    counter = 0
    for element in arrCO2:
        lines+=1
        if element[i]:
            counter+=1

    for j in range(len(arrCO2)-1, -1, -1):
        if len(arrCO2) == 1:
            break
        if counter*2>lines and arrCO2[j][i] == 1 or counter*2==lines and arrCO2[j][i] == 1:
            arrCO2 = np.delete(arrCO2, j, 0)
        elif counter*2<lines and arrCO2[j][i] == 0:
            arrCO2 = np.delete(arrCO2, j, 0)
# print('arr: ',arr,"\narrCO2: ",arrCO2,'\n')
gamma = ''.join([str(elem) for elem in arr[0]])
epsilon = ''.join([str(elem) for elem in arrCO2[0]])
print("Answer 2: ", int(gamma,2) * int(epsilon,2))
