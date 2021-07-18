import os
from os.path import getsize, isfile
path = input("enter your path:")
if path.startswith("~"):
    path = path.replace("~", os.environ['HOME']) #os.environ['HOME'] = path of home directory
dirlst = os.listdir(path)
sizeOfFiles = 0
for file in dirlst:
    if isfile(path+f'/{file}'):
        filextension = file[file.index('.'):]
        if len(filextension) > 5:
            sizeOfFiles += getsize(path+f'/{file}')
print(sizeOfFiles)
