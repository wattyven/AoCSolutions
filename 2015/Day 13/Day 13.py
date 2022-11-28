# thank god, it's something i'm actually a little better at

filepath = 'Day 13 input.txt'

def open_file(filepath):
    with open(filepath, 'r') as f:
        return f.read().splitlines()

def parse_input(text):
    '''returns a list of lists of the form [person, happiness change, neighbor]'''
    parsed = []
    for line in text:
        line = line.split()
        parsed.append([line[0], int(line[3]) * (-1 if line[2] == 'lose' else 1), line[10][:-1]])
    return parsed

def make_dict(parsed):
    '''returns a dictionary of the form {person: {neighbor: happiness change}}'''
    d = {}
    for line in parsed:
        if line[0] not in d:
            d[line[0]] = {}
        d[line[0]][line[2]] = line[1]
    return d

def make_permutations(d):
    '''returns a list of all possible permutations of the keys in d'''
    from itertools import permutations
    return list(permutations(d.keys()))

def find_happiness(d, perm):
    '''returns the total happiness of a seating arrangement'''
    happiness = 0
    for i in range(len(perm)):
        happiness += d[perm[i]][perm[i-1]]
        happiness += d[perm[i]][perm[(i+1) % len(perm)]]
    return happiness

def find_best_happiness(d, perms):
    '''returns the best possible happiness of a seating arrangement'''
    return max(find_happiness(d, perm) for perm in perms)

def add_myself(d):
    '''adds myself to the dictionary'''
    d['Me'] = {}
    for person in d:
        d[person]['Me'] = 0
        d['Me'][person] = 0
    return d

if __name__ == "__main__":
    text = open_file(filepath)
    parsed = parse_input(text)
    d = make_dict(parsed)
    perms = make_permutations(d)
    print('Total change in happiness: ', find_best_happiness(d, perms)) # part one
    d = add_myself(d)
    perms = make_permutations(d)
    print('Total change in happiness: ', find_best_happiness(d, perms)) # part two
