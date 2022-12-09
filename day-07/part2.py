#!/usr/bin/env python3
file = open('input.txt', 'r')
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

current_closest_size = 9999999999999
for d in dir_sizes:
    difference = 70000000 - dir_sizes.get('/') + dir_sizes.get(d)
    if difference >= 30000000 and dir_sizes.get(d) < current_closest_size:
        current_closest_size = dir_sizes.get(d)

print(current_closest_size)
