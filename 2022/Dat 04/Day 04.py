filepath = 'Day 04 input.txt'

# part one
def openFile(filepath):
    '''reads the raw file'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
        lines = []
        for line in data:
            line = line.split(',')
            lines.append(line)
    return(lines)

def getRanges(data):
    '''gets the range of numbers from each line'''
    ranges = []
    for line in data:
        line = line.split()
        ranges.append(line[0].split('-'))
    return(ranges)

def getRange(string):
    '''converts the range strings in a list into integers'''
    numRange = set()
    nums = string.split('-')
    for i in range(int(nums[0]), int(nums[1])+1):
        numRange.add(i)
    return(numRange)

def getValidRanges(lst):
    '''generates the ranges from each string in each sublist'''
    range1 = getRange(lst[0])
    range2 = getRange(lst[1])
    return(range1, range2)

def checkIfContained(range1, range2):
    '''checks if range1 is in range2 or if range2 is in range1'''
    if range1.issubset(range2) or range2.issubset(range1):
        return True
    else:
        return False

def checkIfIntersect(range1, range2):
    '''checks if range1 and range2 intersect'''
    if range1.intersection(range2):
        return True
    else:
        return False

if __name__ == '__main__':
    data = openFile(filepath)
    count = 0
    count2 = 0
    for lst in data:
        range1, range2 = getValidRanges(lst)
        if checkIfContained(range1, range2):
            count += 1
        if checkIfIntersect(range1, range2):
            count2 += 1
    print('Part one: ', count) # part one
    print('Part two: ', count2) # part two
