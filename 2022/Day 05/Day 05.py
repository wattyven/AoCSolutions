filepath = 'Day 05 input.txt'

import time

# 6 dec 2022 -- updated the code so that the towers are no longer hardcoded

# part one

def openFile(filepath):
    '''reads the raw file'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)

def getInstructions(data):
    '''gets move instructions from our data'''
    instructions = []
    for lst in data:
        if lst != '':
            if lst[0] == 'm':
                newlst = lst.split()
                instructions.append(newlst)
    return(instructions)

def towerCount(data):
    '''finds out where the towers end, and how many towers there are'''
    for i in range(len(data)):
        if data[i] == '':
            cutoff = i - 1
            break
    return(cutoff)

def buildTowers(cutoff, data):
    '''builds the number of towers from towerCount'''
    towers = data[cutoff].split()
    i = cutoff - 1
    while i >= 0:
        for n in range(len(towers)):
            if data[i][1 + 4 * n].isalpha():
                towers[n] += data[i][1 + 4 * n]
        i -= 1
    for x in range(len(towers)):
        towers[x] = towers[x][1:]
    return(towers)

def makeMoves(instructions, towers):
    '''makes moves based on our instructions'''
    newtowers = towers.copy()
    for instruction in instructions:
        start = int(instruction[3]) - 1
        end = int(instruction[5]) - 1
        count = int(instruction[1])
        movecount = 0
        while movecount < count:
            newtowers[end] = newtowers[end] + newtowers[start][-1]
            newtowers[start] = newtowers[start][:-1]
            movecount += 1
    return(newtowers)
 
# part two

def bulkMoves(instructions, towers):
    newtowers = towers.copy()
    for instruction in instructions:
        start = int(instruction[3]) - 1
        end = int(instruction[5]) - 1
        count = int(instruction[1])
        newtowers[end] = newtowers[end] + newtowers[start][-count:]
        newtowers[start] = newtowers[start][:-count]
    return(newtowers)

def getLast(lstlsts):
    '''gets the last element of each sublist in our list of lists'''
    last = ''
    for lst in lstlsts:
        last +=(lst[-1])
    return(last)

if __name__ == '__main__':
    start = time.time()
    data = openFile(filepath)
    numTowers = towerCount(data)
    towers = buildTowers(numTowers, data)
    towerInstructions = getInstructions(data)
    print('Part one: ', getLast(makeMoves((towerInstructions), towers)))
    print('Part two: ', getLast(bulkMoves((towerInstructions), towers)))
    print(f'Time elapsed was {time.time() - start} seconds')
