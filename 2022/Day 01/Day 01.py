filepath = 'Day 01 input.txt'

# not my very first implementation, but revisited after solving and slimmed it down a little
# my first solution was AWFUL

def openFile(filepath):
    '''reads the raw file'''
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data

def findBiggest(data):
    '''splits the data into groups by looking for \n\n, comparing elf size along the way'''
    biggest = 0
    current = 0
    for line in data:
        if line == '\n':
            if current > biggest:
                biggest = current
            current = 0
        else:
            current += int(line)
    return biggest

def listelves(data):
    '''splits the data into groups by looking for \n\n, comparing elf size along the way'''
    elves = []
    current = 0
    for line in data:
        if line == '\n':
            elves.append(current)
            current = 0
        else:
            current += int(line)
    return elves

if __name__ == '__main__':
    data = openFile(filepath)
    print(findBiggest(data))
    lst = listelves(data)
    print(findBiggest(data) + sorted(lst)[-2] + sorted(lst)[-3])
