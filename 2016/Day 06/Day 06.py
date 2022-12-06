filepath = 'Day 06 input.txt'

def readColumns(filepath):
    '''reads the file and returns a list of columns instead of lines by transposing the data'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    columns = []
    for i in range(len(data[0])):
        column = ''
        for line in data:
            column += line[i]
        columns.append(column)
    return(columns)
    
def mostCommonChar(string):
    '''finds the most common character in a string'''
    chars = []
    for char in string:
        if char not in chars:
            chars.append(char)
    charcounts = []
    for char in chars:
        charcounts.append(string.count(char))
    return(chars[charcounts.index(max(charcounts))])

def errorCorrectedMsg(filepath):
    '''finds the most common character in each column and returns the message'''
    columns = readColumns(filepath)
    msg = ''
    for column in columns:
        msg += mostCommonChar(column)
    return(msg)

print(errorCorrectedMsg(filepath)) # part one

def leastCommonChar(string):
    '''finds the least common character in a string'''
    chars = []
    for char in string:
        if char not in chars:
            chars.append(char)
    charcounts = []
    for char in chars:
        charcounts.append(string.count(char))
    return(chars[charcounts.index(min(charcounts))])

def errorCorrectedMsg2(filepath):
    '''finds the least common character in each column and returns the message'''
    columns = readColumns(filepath)
    msg = ''
    for column in columns:
        msg += leastCommonChar(column)
    return(msg)

print(errorCorrectedMsg2(filepath)) # part two
