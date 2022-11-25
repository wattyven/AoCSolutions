vowels = 'aeiou'
filepath = 'Day 5 input.txt'

def count_vowels(word):
    '''counts the number of vowels in a word'''
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def doubleLetter(word):
    '''checks if a word has a double letter'''
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

def valid(word):
    '''checks if a word is valid'''
    if count_vowels(word) < 3:
        return False
    if not doubleLetter(word):
        return False
    if 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word:
        return False
    return True

def twoletterpair(word):
    '''checks for non-overlapping two letter pairs'''
    for i in range(len(word)-1):
        if word[i:i+2] in word[i+2:]:
            return True

def spacedRepeat(word):
    '''checks if a word has a letter that repeats with a space in between'''
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            return True
    return False

def partTwoNice(word):
    '''checks if a word is nice for part 2'''
    if not twoletterpair(word):
        return False
    if not spacedRepeat(word):
        return False
    return True

def main():
    '''main function'''
    # part one
    with open(filepath) as fp:
        count = 0
        for line in fp:
            if valid(line):
                count += 1
    print(count) # returns number of valid words for part one
    # part two
    with open(filepath) as fp:
        count2 = 0
        for line in fp:
            if partTwoNice(line):
                count2 += 1
    print(count2) # returns number of valid words for part two


if __name__ == '__main__':
    main()
