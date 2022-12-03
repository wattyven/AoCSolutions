filepath = 'Day 03 input.txt'

# DEFINITELY not the most efficient, but did it the first way that came to mind
# will refine later

# part one
def openFile(filepath):
    '''reads the raw file'''
    with open(filepath, 'r') as f:
        data = f.read().split('\n')
    return(data)

def halfString(string):
    '''splits a string in half'''
    half = len(string) // 2
    return([string[:half], string[half:]])

def halfStringsinList(lst):
    '''splits each string in a list in half'''
    for i in range(len(lst)):
        lst[i] = halfString(lst[i])
    return(lst)

def getIntersection(lst):
    '''returns common elements in strings in a list'''
    inter = []
    for i in range(len(lst[0])):
        if lst[0][i] in lst[1]:
            inter.append(lst[0][i])
    return(removeRepeats(inter))

def compareLists(data):
    inter = []
    for i in range(len(data)):
        data[i] = halfString(data[i])
        inter.append(getIntersection(data[i]))
    return inter

def listofliststolistofstrings(lst):
    '''converts a list of lists of strings into a list of strings'''
    for i in range(len(lst)):
        lst[i] = ''.join(lst[i])
    return(lst)

def removeRepeats(lst):
    '''removes duplicate characters from a list'''
    lst = list(set(lst))
    return(lst)

def assignPoints(list):
    '''for each character in a list, assign a point value corresponding to letter number - lowercase get 1-26, uppercase 27-52'''
    points = []
    for i in range(len(list)):
        if list[i].islower():
            points.append(ord(list[i]) - 96)
        else:
            points.append(ord(list[i]) - 38)
    return(points)

common = compareLists(openFile(filepath))
# part one output
print(sum(assignPoints(listofliststolistofstrings(common))))

# part two

def splitFileThreeLines(filepath):
    '''splits the file into three lines'''
    with open(filepath, 'r') as f:
        data = f.read().split('\n')
    data = [data[i:i+3] for i in range(0, len(data), 3)]
    return(data)

def findCommonElements(lst):
    '''finds common characters in a list of 3 strings'''
    common = []
    for i in range(len(lst[0])):
        if lst[0][i] in lst[1] and lst[0][i] in lst[2]:
            common.append(lst[0][i])
    return(removeRepeats(common))

def compareLists(data):
    inter = []
    for i in range(len(data)):
        inter.append(findCommonElements(data[i]))
    return inter

common = compareLists(splitFileThreeLines(filepath))
# part two output
print(sum(assignPoints(listofliststolistofstrings(common))))
    
