filepath = 'Day 01 input.txt'

# this is chunky, i just did it as fast as i could without a care for efficiency

def openFile(filepath):
    '''reads the raw file'''
    with open(filepath, 'r') as f:
        data = f.read()
    return data

def splitGroups(data):
    '''splits the data into groups, separated by empty lines'''
    groups = data.split('\n\n')
    return groups

def removeNewLine(group):
    '''removes the newline character from a group'''
    group = group.replace('\n', ',')
    return group

def removeNewLines(data):
    '''removes the newline characters from a list of groups'''
    newdata = []
    for group in data:
        newdata.append(removeNewLine(group))
    return newdata

def stringstolist(list):
    '''converts a list of strings to a list of lists of strings'''
    newlist = []
    for string in list:
        newlist.append(string.split(','))
    return newlist

def listToInt(list):
    '''converts a list of strings to a list of ints'''
    newlist = []
    for string in list:
        newlist.append(int(string))
    return newlist

def sumElements(list):
    '''sums the elements of a list'''
    return sum(list)

def sumGroups(groups):
    '''sums the groups'''
    sums = []
    for group in groups:
        sums.append(sumElements(listToInt(group)))
    return sums

if __name__ == '__main__':
    data = sumGroups(stringstolist(removeNewLines(splitGroups(openFile(filepath))))) # i'm so sorry
    # get the three highest values from newlist
    highest = max(data)
    secondHighest = sorted(data)[-2]
    thirdHighest = sorted(data)[-3]
    print(highest) # part one
    print(highest + secondHighest + thirdHighest) # part two
 
