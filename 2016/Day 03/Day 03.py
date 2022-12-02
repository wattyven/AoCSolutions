filepath = 'Day 03 input.txt'

def openFile(filepath):
    '''reads the raw file, splits it into a list of lines'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)

def getTriangles(data):
    '''checks each line of the input file for valid triangles'''
    count = 0
    for line in data:
        line = line.split()
        line = [int(i) for i in line]
        line.sort()
        if line[0] + line[1] > line[2]:
            count += 1
    return(count)

def alternateRead(filepath):
    '''reads the raw file in vertical column groups of three'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    # split our list of lines into a list of lists
        nums = []
        for line in data:
            nums.append(line.split())
    # transpose our list of lists
        nums = list(map(list, zip(*nums)))
    # flatten our list of lists
        nums = [item for sublist in nums for item in sublist]
    # convert our list of strings to a list of ints
        nums = [int(i) for i in nums]
    return(nums)
    # i liked that function, that was fun

def validateAltTriangles(data):
    '''using our alternateRead function, checks each group of three numbers in our data for valid triangles'''
    count = 0
    for i in range(0, len(data), 3):
        line = data[i:i+3]
        line.sort()
        if line[0] + line[1] > line[2]:
            count += 1
    return(count)

print(getTriangles(openFile(filepath))) # part one
print(validateAltTriangles(alternateRead(filepath))) # part two
