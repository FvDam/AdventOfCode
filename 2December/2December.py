fileName = "input.txt"
location = [0,0]

with open(fileName, "r") as file:
    for line in file:
        line, move = line.split(' ')
        if line == 'forward':
            location[0] += int(move[:-1])
        if line == 'down':
            location[1] += int(move[:-1])
        if line == 'up':
            location[1] -= int(move[:-1])
print('Answer 1:',location[0]*location[1])

location = [0,0,0]
with open(fileName, "r") as file:
    for line in file:
        line, move = line.split(' ')
        if line == 'forward':
            location[0] += int(move[:-1])
            location[1] += int(move[:-1]) * location[2]
        if line == 'down':
            location[2] += int(move[:-1])
        if line == 'up':
            location[2] -= int(move[:-1])
print('Answer 2:',location[0]*location[1])
