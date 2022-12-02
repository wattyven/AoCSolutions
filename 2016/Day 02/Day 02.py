filepath = 'Day 02 input.txt'

def openFile(filepath):
    '''reads the raw file, splits it into a list of lines'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)

def getPad(data):
    '''create our keypad to start, then navigate our keypad'''
    pad = [[1,2,3],[4,5,6],[7,8,9]]
    location = [1,1] # because we start at 5, in the middle of the keypad
    code = []
    for line in data:
        for i in line:
            if i == 'U':
                if location[0] > 0:
                    location[0] -= 1
            elif i == 'D':
                if location[0] < 2:
                    location[0] += 1
            elif i == 'L':
                if location[1] > 0:
                    location[1] -= 1
            elif i == 'R':
                if location[1] < 2:
                    location[1] += 1
        code.append(pad[location[0]][location[1]]) # append the number at the current location
    return(code)

def getPad2(data):
    '''create the new keypad, then navigate it as well'''
    pad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
    location = [2,0] # because we start at 5, in the middle row of the keypad, far left
    code = []
    for line in data:
        for i in line:
            if i == 'U':
                if location[0] > 0 and pad[location[0]-1][location[1]] != 0:
                    location[0] -= 1
            elif i == 'D':
                if location[0] < 4 and pad[location[0]+1][location[1]] != 0:
                    location[0] += 1
            elif i == 'L':
                if location[1] > 0 and pad[location[0]][location[1]-1] != 0:
                    location[1] -= 1
            elif i == 'R':
                if location[1] < 4 and pad[location[0]][location[1]+1] != 0:
                    location[1] += 1
        code.append(pad[location[0]][location[1]]) # append the number at the current location
    return(code)

print(''.join(str(i) for i in getPad(openFile(filepath)))) # part one
print(''.join(str(i) for i in getPad2(openFile(filepath)))) # part two
