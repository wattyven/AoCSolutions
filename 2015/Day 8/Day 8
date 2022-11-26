filepath = 'Day 8 input.txt'

def partOne(filepath):
    '''part one'''
    return sum(len(s[:-1]) - len(eval(s)) for s in open(filepath))
    # literally just the length of the string minus the length of the evaluated string

def partTwo(filepath):
    '''part two'''
    return sum(2+s.count('\\')+s.count('"') for s in open(filepath))
    # 2 for the two extra quotes, then count the number of backslashes and quotes

print(partOne(filepath))
print(partTwo(filepath))
