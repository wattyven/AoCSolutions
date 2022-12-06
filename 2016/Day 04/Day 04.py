filepath = 'Day 04 input.txt'

def openFile(filepath):
    '''reads the raw file, splits it into a list of lines'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)

def getChecksum(data):
    '''gets the checksum from the data'''
    checksums = []
    for line in data:
        checksums.append(line.split('[')[1][:-1])
    return(checksums)

def validateRooms(data, checksums):
    '''validates the rooms based on the checksums'''
    validRooms = []
    for i in range(len(data)):
        line = data[i][:-7]
        checksum = checksums[i]
        letters = []
        for char in line:
            if char.isalpha():
                letters.append(char)
        lettercount = {}
        for letter in letters:
            if letter not in lettercount:
                lettercount[letter] = 1
            else:
                lettercount[letter] += 1
        lettercount = sorted(lettercount.items(), key=lambda x: (-x[1], x[0]))
        lettercount = [x[0] for x in lettercount]
        if lettercount[:5] == list(checksum):
            validRooms.append(i)
    return(validRooms)

def getSectorIds(validRooms, data):
    '''uses the validRooms list to get the sector IDs from the data list'''
    sectorIds = []
    for room in validRooms:
        sectorIds.append(int(data[room].split('-')[-1].split('[')[0]))
    return(sectorIds)

def decryptRoomNames(data):
    '''decrypts the room names by shifting the letters by the sector ID'''
    # alphabet is mod 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = []
    for line in data:
        sectorId = int(line.split('-')[-1].split('[')[0])
        name = line[:-7]
        decryptedName = ''
        for char in name:
            if char.isalpha():
                decryptedName += alphabet[(alphabet.index(char) + sectorId) % 26]
            else:
                decryptedName += ' '
        decrypted.append(decryptedName)
    return(decrypted)

if __name__ == '__main__':
    data = openFile(filepath)
    checksums = getChecksum(data)
    validRooms = validateRooms(data, checksums)
    sectorIds = getSectorIds(validRooms, data)
    print(sum(sectorIds)) # part one
    decrypted = decryptRoomNames(data)
    for i in range(len(decrypted)):
        if 'northpole' in decrypted[i]:
            print(f'String "northpole" found in room {i}, with sector ID', int(data[i].split('-')[-1].split('[')[0])) # part two
