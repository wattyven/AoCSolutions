# open input file and read it line by line
with open('Day 1 input.txt', 'r') as f:
    # convert the file into a list of lines, each line is an int
    lines = [int(line) for line in f.readlines()]
# find the two values in the list that sum to 2020
for i in range(len(lines)):
    for j in range(i+1, len(lines)): # not the most efficient method, but it'll do
        if lines[i] + lines[j] == 2020:
            print(lines[i] * lines[j])
