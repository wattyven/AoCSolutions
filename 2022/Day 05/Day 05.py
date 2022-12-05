filepath = 'Day 05 input.txt'

import time

# okay now i've tweaked it a bit so the towers are taken as strings now and i'm not 
# flip-flopping back and forth between handling lists and handling strings 
# yes the towers are still hardcoded atm

towers = ['GTRW', 'GCHPMSVW', 'CLTSGM', 'JHDMWRF', 'PQLHSWFJ', 'PJDNFMS', 'ZBDFGCSJ', 'RTB', 'HNWLC']

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

def getTowers(data):
    '''need to automate this instead of hardcoding it like i did'''

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
    print('Part one: ', getLast(makeMoves(getInstructions(openFile(filepath)), towers)))
    print('Part two: ', getLast(bulkMoves(getInstructions(openFile(filepath)), towers)))
    print(f'Time elapsed was {time.time() - start} seconds')
