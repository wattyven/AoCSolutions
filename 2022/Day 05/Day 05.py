filepath = 'Day 05 input.txt'

import time

# yes i hardcoded the towers as lists, yes i switch them back and forth between 
# lists and strings a few times in here, yes it's DEFINITELY bad, 
# but i got the answers i guess

towers = [['G', 'T', 'R', 'W'], ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'], 
['C', 'L', 'T', 'S', 'G', 'M'], ['J', 'H', 'D', 'M', 'W', 'R', 'F'], 
['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'], ['P', 'J', 'D', 'N', 'F', 'M', 'S'], 
['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'], ['R', 'T', 'B'], ['H', 'N', 'W', 'L', 'C']]

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
    for instruction in instructions:
        start = int(instruction[3]) - 1
        end = int(instruction[5]) - 1
        count = int(instruction[1])
        movecount = 0
        while movecount < count:
            towers[end].append(towers[start].pop())
            movecount += 1
    return(towers)

def lst2str(lst):
    '''converts a list to a string'''
    string = ''
    for item in lst:
        string += item
    return(string)

def lstlsts2str(lst):
    newlst = []
    for item in lst:
        newlst.append(lst2str(item))
    return(newlst)

newdata = (lstlsts2str(towers))

def bulkMoves(instructions, towers):
    for instruction in instructions:
        start = int(instruction[3]) - 1
        end = int(instruction[5]) - 1
        count = int(instruction[1])
        towers[end] = towers[end] + towers[start][-count:]
        towers[start] = towers[start][:-count]
    return(towers)

def getLast(towers):
    '''gets the last element of each sublist in our list of lists'''
    last = ''
    for lst in towers:
        last +=(lst[-1])
    return(last)

if __name__ == '__main__':
    start = time.time()
    print(getLast(makeMoves(getInstructions(openFile(filepath)), towers))) # part one
    print(getLast(bulkMoves(getInstructions(openFile(filepath)), newdata))) # part two
    print('Time: ', time.time() - start, 's')
