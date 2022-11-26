filepath = "Day 1 input.txt"

def splitInput(inputstring):
    '''unpacks our input string into a list'''
    lst = [*inputstring] # unpack our string into a list lst
    return lst

def checkvalid(lst):
    '''checks if our list is valid'''
    for i in range(len(lst)):
        if (lst[i] != "(" and lst[i] != ")"):
            print("Invalid input: character", i, "is not a valid character.")
            return False
    return True

def getFloor(lst):
    '''gets the floor number for part one'''
    floor = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            floor = floor + 1
        elif lst[i] == ")":
            floor = floor - 1
    return floor

def firstBasement(lst):
    '''gets the position of the first basement entry'''
    floor = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            floor = floor + 1
        elif lst[i] == ")":
            floor = floor - 1
        if floor == -1: # if we're on the basement floor, return the position
            return i + 1 # +1 because we want the position, not the index
    return "You never entered the basement." # we only get to this point if floor never goes below 0

def main():
    '''main, puts everything together'''
    file = open(filepath, "r") # opens the file
    inputstring = file.read() # reads the file
    lst = splitInput(inputstring) # splits the input into a list
    if checkvalid(lst):
        print("You are on floor", getFloor(lst)) # prints the floor number for part one
        print("You first entered the basement at position", firstBasement(lst)) # prints the position of the first basement entry for part two
    else:
        print("Invalid input") 

if __name__ == "__main__":
    main()
