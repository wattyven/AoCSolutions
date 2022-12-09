filepath = 'Day 08 input.txt'

from time import time

def openFile(filepath):
    '''splits file into lines'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)

def getVisibleTrees(data):
    '''returns the number of trees that can be seen from outside the forest'''
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    rows = len(data)
    columns = len(data[0])
    count = 0
    for row in range(rows):
        for column in range(columns):
            # we're taking a look at tree X at position (row, column)
            visible = False
            for (x,y) in directions:
                xrow = row
                xcol = column
                valid = True
                while True:
                    xrow += x
                    xcol += y
                    if not (0 <= xrow<rows and 0 <= xcol < columns):
                        break
                    if data[xrow][xcol] >= data[row][column]:
                        valid = False
                if valid:
                    visible = True
            if visible:
                #print(f'The tree at {xrow, xcol} is visible!')
                count += 1
    return(count)

def getScenicScore(data):
    '''returns the highest scenic score of any tree in the forest'''
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    rows = len(data)
    columns = len(data[0])
    scores = 0
    for row in range(rows):
        for column in range(columns):
            # same as above! 
            treeScore = 1
            for (x,y) in directions:
                dist = 1
                xrow = row+x
                xcol = column+y
                while True:
                    if not (0 <= xrow < rows and 0 <= xcol < columns):
                        dist -= 1
                        break
                    if data[xrow][xcol]>=data[row][column]:
                        break
                    dist += 1
                    xrow += x
                    xcol += y
                treeScore *= dist
            scores = max(scores, treeScore)
    return(scores)

if __name__ == '__main__':
    startTime = time()
    data = openFile(filepath)
    print('Part 1:', getVisibleTrees(data)) 
    print('Part 2:', getScenicScore(data)) 
    print(f'Time elapsed: {time()-startTime} seconds')
