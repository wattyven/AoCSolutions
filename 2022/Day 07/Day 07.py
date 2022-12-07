filepath = 'Day 07 input.txt'

# this one took me over an hour and three rewrites to get it to work

from collections import defaultdict
from time import time

def openFile(filepath):
    '''splits file into lines'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)

def maplines(data):
    '''self-explanatory'''
    lines = map(str.split, data) 
    return(lines)

def fileToList(filepath):
    '''combines the functions above, then calls on 
    defaultdict to assign our provided sizes as values'''
    data = openFile(filepath)
    lines = maplines(data) 
    path = [] # path is a list of directories and sub-directories
    directories = defaultdict(int) # defaultdict is a dictionary that assigns a value to a key if it doesn't exist
    for line in lines:
        if line[0] == '$': # this means we gave a command in this line, and we didn't get a filesize
            if line[1] == 'cd': # change directory, so we're changing our list path
                if line[2] == '..':
                    path.pop() # removes the last item in the list to go up a folder
                else:
                    path.append(line[2]) # adds the next folder to the list
        elif line[0].isnumeric(): # if the first item in the line is a number, that's a filesize we've been given
            for i in range(len(path)): # for each directory in the path, we add the filesize to the total
                directories[tuple(path[:i+1])] += int(line[0]) # add the file size to the total for each directory in the path
    return(directories) # return the dictionary of directories and their corresponding sizes

if __name__ == '__main__':
    startTime = time()
    dirs = fileToList(filepath)
    #print(dirs)
    print(f'Directory build time: {(time() - startTime) * 1000} ms')
    print(f'Part one: {sum(size for size in dirs.values() if size <= 100000)}') # sum of all directories with a size of at most 100000
    required = 30000000 - (70000000 - dirs[("/",)])
    print(f'Part two: {min(size for size in dirs.values() if size >= required)}') # smallest directory we can delete to get the required free space
