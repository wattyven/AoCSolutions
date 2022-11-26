from itertools import permutations as perm

filepath = 'Day 9 input.txt'

def minMaxPath(pairs, mode):
    '''returns min and max path length in a non-oriented graph'''
    distances = []
    for x in perm(pairs):
        for i in range(len(x) - 1):
            distances.append(sum(pairs[x[i]][x[i+1]]))
    if mode == 'min':
        return min(distances) 
    else:
        return max(distances)

def main():
    with open(filepath, 'r') as file:
        text = file.read().splitlines()
        distances = dict()
        places = set()
        for line in text:
            start, end, value = line.split()[0], line.split()[2], int(line.split()[-1])
            places.add(start)
            places.add(end)
            distances.setdefault(start, dict())[end] = int(value)
            distances.setdefault(end, dict())[start] = int(value)
        print("Shortest route length: ", minMaxPath(distances,'min')) # part one
        print("Longest route length: ", minMaxPath(distances,'max')) # part two


if __name__ == "__main__":
    main()
