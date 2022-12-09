#!/usr/bin/env python3
cwd = ''
dir_sizes = {}

def addToAllDirs(size, path):
    # if (path == '/'):
    dir_sizes[path] = dir_sizes.get(path, 0) + int(size)

    while (len(path) > 1):
        path = path[:path.rfind('/')]
        if len(path) == 0: path = '/'
        dir_sizes[path] = dir_sizes.get(path, 0) + int(size)

file = open('input.txt', 'r')

for line in file:
    line = line.strip().split(' ')
    
    if line[0] == '$' and line[1] == 'cd' and line[2] == '..':
        cwd = cwd[:cwd.rfind('/')]

    elif line[0] == '$' and line[1] == 'cd':
        if line[2] == '/':
            cwd = '/'
        elif cwd.endswith('/'): 
            cwd = cwd + line[2]
        else:
            cwd = cwd + '/' + line[2]

    elif line[0].isnumeric():
        addToAllDirs(line[0], cwd)

total = 0
for key in dir_sizes:
    if dir_sizes.get(key) <= 100000:
        total = total + dir_sizes[key]

print(total)