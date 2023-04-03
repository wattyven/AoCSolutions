# open input file and read it line by line
with open('Day 2 input.txt', 'r') as f:
    # convert the file into a list of lines, each line is an int
    lines = [line for line in f.readlines()]
    # parse each line into a list of the format [min, max, letter, password]
    lines = [line.split() for line in lines]
    for i in range(len(lines)):
        lines[i][0] = lines[i][0].split('-')
        lines[i][1] = lines[i][1][0]
        lines[i][2] = lines[i][2].strip()
    # check each password
    valid = 0
    # part one
    for line in lines:
        if line[2].count(line[1]) >= int(line[0][0]) and line[2].count(line[1]) <= int(line[0][1]):
            valid += 1
    print(valid)

    # part two
    valid = 0
    for line in lines:
        # Toboggan corp has no concept of 0 indexing so we index from i - 1
        if (line[2][int(line[0][0]) - 1] == line[1]) ^ (line[2][int(line[0][1]) - 1] == line[1]):
            valid += 1
    print(valid)
