filepath = 'Day 10 input.txt'

from time import time

def openFile(filepath):
    '''splits file into lines'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)

def lstlines2lstlsts(data):
    '''converts a list of strings to a list of lists of integers'''
    lstlsts = []
    for line in data:
        lst = line.split()
        lstlsts.append(lst)
    return lstlsts

def checkburst(cycle):
    '''checks if cycle is a burst'''
    if cycle == 20:
        return True
    elif (cycle - 20) % 40 == 0 and cycle <= 220:
        return True
    else:
        return False

def pixelDrawn(cycle):
    pixelrow = (cycle - 1) // 40
    pixelcol = (cycle - 1) % 40
    #pixCoord = [pixelrow, pixelcol]
    return pixelrow, pixelcol

def drawLogic(cycle, x, CRT):
    '''draws the logic'''
    pixelrow, pixelcol = pixelDrawn(cycle)
    if (cycle - 1) % 40 >= x-1 and (cycle - 1) % 40 <= x+1:
        CRT[pixelrow][pixelcol] = '#'
    else:
        CRT[pixelrow][pixelcol] = '.'
    return CRT

def execute(data):
    '''executes the instructions'''
    CRT = [['.' for i in range(40)] for j in range(6)]
    cycle = 0
    x = 1
    signals = []
    for line in data:
        if line[0] == 'noop':
            cycle += 1
            CRT = drawLogic(cycle, x, CRT)
            if checkburst(cycle):
                signals.append(x * cycle)
        elif line[0] == 'addx':
            cycle += 1
            if checkburst(cycle):
                signals.append(x * cycle)
            CRT = drawLogic(cycle, x, CRT)
            cycle += 1
            if checkburst(cycle):
                signals.append(x * cycle)
            CRT = drawLogic(cycle, x, CRT)
            x += int(line[1])
    for line in CRT:
        print(line) # print the CRT for part two
    return sum(signals) # return the sum of the signals for part one
            
if __name__ == '__main__':
    starttime = time()
    data = openFile(filepath)
    data = lstlines2lstlsts(data)
    signalsum = execute(data) # execute the instructions, also prints part two
    print(signalsum) # print the sum of the signals for part one
    print('Time taken: {:.2f} seconds'.format(time()-starttime)) # print the time taken
