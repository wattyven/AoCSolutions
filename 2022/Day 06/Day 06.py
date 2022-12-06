filepath = 'Day 06 input.txt'

import time

def openFile(filepath):
    '''reads the raw file'''
    with open(filepath, 'r') as f:
        data = f.read()
    return(data)

def getStart(data, length):
    '''gets the starting position'''
    for i in range(len(data)):
        if len(set(data[i:i+length])) == length:
            startstring = data[i:i+length]
            position = i+length
            return (startstring, position)

if __name__ == "__main__":
    startTime = time.time()
    data = openFile(filepath)
    print(getStart(data, 4)) # part one
    print(getStart(data, 14)) # part two
    print(f'Time elapsed: {time.time() - startTime} seconds')
