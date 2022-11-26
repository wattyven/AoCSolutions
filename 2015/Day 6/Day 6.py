filepath = 'Day 6 input.txt'

def splittolines(filepath):
    '''splits the lines of a file into a list'''
    with open(filepath) as fp:
        lines = fp.read().splitlines()
    return lines

def breakline(line):
    '''breaks a line into a list of words'''
    return line.split()
    
def getInstructions(filepath):
    '''gets the instructions from the file as a list of lists'''
    lines = splittolines(filepath)
    instructions = []
    for line in lines:
        instructions.append(breakline(line))
    return instructions

def turnon(grid, x1, y1, x2, y2):
    '''turns on the lights in the grid'''
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] = 1

def turnbrighter(grid, x1, y1, x2, y2):
    '''increases brightness of lights in the grid'''
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] += 1

def turnoff(grid, x1, y1, x2, y2):
    '''turns off the lights in the grid'''
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] = 0

def turndimmer(grid, x1, y1, x2, y2):
    '''decreases brightness of lights in the grid'''
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if grid[x][y] > 0:
                grid[x][y] -= 1

def toggle(grid, x1, y1, x2, y2):
    '''toggles the lights in the grid'''
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if grid[x][y] == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 0

def togglebrightness(grid, x1, y1, x2, y2):
    '''adds two to the brightness of lights in the grid'''
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            grid[x][y] += 2

def translateInstructions(instructions):
    '''reads turn on / turn off / toggle and calls the appropriate function
    after writing this i realized i should probably have made retrieving the 
    coordinates its own function to make these lines less painful to read'''
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for instruction in instructions:
        if instruction[0] == 'turn':
            if instruction[1] == 'on':
                turnon(grid, int(instruction[2].split(',')[0]), int(instruction[2].split(',')[1]), int(instruction[4].split(',')[0]), int(instruction[4].split(',')[1]))
            else:
                turnoff(grid, int(instruction[2].split(',')[0]), int(instruction[2].split(',')[1]), int(instruction[4].split(',')[0]), int(instruction[4].split(',')[1]))
        else:
            toggle(grid, int(instruction[1].split(',')[0]), int(instruction[1].split(',')[1]), int(instruction[3].split(',')[0]), int(instruction[3].split(',')[1]))
    return grid

def translateAncientNordicElvishInstructions(instructions):
    '''does the translation for part two'''
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for instruction in instructions:
        if instruction[0] == 'turn':
            if instruction[1] == 'on':
                turnbrighter(grid, int(instruction[2].split(',')[0]), int(instruction[2].split(',')[1]), int(instruction[4].split(',')[0]), int(instruction[4].split(',')[1]))
            else:
                turndimmer(grid, int(instruction[2].split(',')[0]), int(instruction[2].split(',')[1]), int(instruction[4].split(',')[0]), int(instruction[4].split(',')[1]))
        else:
            togglebrightness(grid, int(instruction[1].split(',')[0]), int(instruction[1].split(',')[1]), int(instruction[3].split(',')[0]), int(instruction[3].split(',')[1]))
    return grid

def countLights(grid):
    '''counts the number of lights that are on'''
    count = 0
    for x in range(1000):
        for y in range(1000):
            if grid[x][y] == 1:
                count += 1
    return count

def main():
    '''main function'''
    instructions = getInstructions(filepath)
    grid = translateInstructions(instructions)
    grid2 = translateAncientNordicElvishInstructions(instructions)
    print(countLights(grid)) # part one
    print(sum(sum(x) for x in grid2)) # part two

if __name__ == '__main__':
    main()
