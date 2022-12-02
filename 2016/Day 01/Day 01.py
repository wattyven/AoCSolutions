filepath = 'Day 01 input.txt'

def openFile(filepath):
    '''reads the raw file, splits it into a list of directions'''
    with open(filepath, 'r') as f:
        data = f.read().split(', ')
    return(data)

def read_direction(data):
    '''reads the list of directions and returns the final location'''
    location = [0, 0]
    direction = 0
    for i in data:
        # read the turn
        if i[0] == 'R':
            direction += 1
        elif i[0] == 'L':
            direction -= 1
        if direction == 4:
            direction = 0
        elif direction == -1:
            direction = 3
        # move the distance according to the direction
        if direction == 0:
            location[1] += int(i[1:])
        elif direction == 1:
            location[0] += int(i[1:])
        elif direction == 2:
            location[1] -= int(i[1:])
        elif direction == 3:
            location[0] -= int(i[1:])
    return(location)

def distance(location):
    '''calculates the distance from the origin to the location, using grid navigation (not as the bird flies)'''
    distance = abs(location[0]) + abs(location[1])
    return(distance)

def newLocation(data):
    '''reads the list of directions and returns the first location visited twice'''
    location = [0, 0]
    direction = 0
    visited = [] # list of visited locations, could also use a set but this was the first way i did it
    for i in data:
        if i[0] == 'R':
            direction += 1
        elif i[0] == 'L':
            direction -= 1
        if direction == 4:
            direction = 0
        elif direction == -1:
            direction = 3
        if direction == 0:
            for j in range(int(i[1:])):
                location[1] += 1
                if location in visited:
                    return(location)
                else:
                    visited.append(location[:])
        elif direction == 1:
            for j in range(int(i[1:])):
                location[0] += 1
                if location in visited:
                    return(location)
                else:
                    visited.append(location[:])
        elif direction == 2:
            for j in range(int(i[1:])):
                location[1] -= 1
                if location in visited:
                    return(location)
                else:
                    visited.append(location[:])
        elif direction == 3:
            for j in range(int(i[1:])):
                location[0] -= 1
                if location in visited:
                    return(location)
                else:
                    visited.append(location[:])

print(distance(read_direction(openFile(filepath)))) # part 1
print(distance(newLocation(openFile(filepath)))) # part 2
