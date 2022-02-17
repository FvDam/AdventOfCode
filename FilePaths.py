import os

dir_path = os.path.dirname(os.path.realpath(__file__))
f = open('filePaths.txt', 'a')
dir_path = os.listdir(dir_path)

for map in dir_path:
    f.write(map+"\n")
f.close()
