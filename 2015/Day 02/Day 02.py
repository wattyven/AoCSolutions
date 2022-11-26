filepath = "Day 2 input.txt"

def splitLine(filepath):
    '''splits our input file into a list of strings'''
    file = open(filepath, "r") # opens the file
    inputstring = file.read() # reads the file
    lstlines = inputstring.splitlines() # splits the input into a list
    return lstlines

def getDimensions(string):
    '''gets the dimensions of a box from a string'''
    lst = string.split("x") # splits the string into a list
    dims = [int(i) for i in lst] # converts the list from strings to integers
    return dims

def smallestSide(lst):
    '''gets the smallest side of a box from a list of dimensions'''
    side1 = lst[0]*lst[1]
    side2 = lst[1]*lst[2]
    side3 = lst[2]*lst[0]
    if side1 <= side2 and side1 <= side3:
        return side1
    elif side2 <= side1 and side2 <= side3:
        return side2
    else:
        return side3

def getArea(lst):
    '''gets the area of a box from a list of dimensions'''
    area = 2*lst[0]*lst[1] + 2*lst[1]*lst[2] + 2*lst[2]*lst[0] + smallestSide(lst) # gets the area of the box plus the smallest side (for the elves' slack)
    return area

def bowLength(lst):
    '''gets the length of the bow for a box from a list of dimensions'''
    bow = lst[0]*lst[1]*lst[2] # gets the volume of the box
    return bow

def smallestPerimeter(lst):
    '''gets the smallest perimeter of a box from a list of dimensions'''
    side1 = 2*(lst[0]+lst[1])
    side2 = 2*(lst[1]+lst[2])
    side3 = 2*(lst[2]+lst[0])
    if side1 <= side2 and side1 <= side3:
        return side1
    elif side2 <= side1 and side2 <= side3:
        return side2
    else:
        return side3

def ribbonLength(lst):
    '''gets the total length of ribbon the elves need for a specific box'''
    ribbon = smallestPerimeter(lst) + bowLength(lst) # gets the smallest perimeter of the box plus the length of the bow
    return ribbon

def sumAllRibbons(filepath):
    '''gets the sum of all ribbon lengths'''
    lstlines = splitLine(filepath) # gets the list of strings
    lstdims = [getDimensions(i) for i in lstlines] # gets the list of dimensions
    lstribbons = [ribbonLength(i) for i in lstdims] # gets the list of ribbon lengths
    sum = 0
    for i in lstribbons:
        sum = sum + i
    return sum

def sumAllAreas(filepath):
    '''gets the sum of all areas'''
    lstlines = splitLine(filepath) # gets the list of strings
    lstdims = [getDimensions(i) for i in lstlines] # gets the list of dimensions
    lstareas = [getArea(i) for i in lstdims] # gets the list of areas
    sum = 0
    for i in lstareas:
        sum = sum + i
    return sum

def main():
    '''main, puts everything together'''
    print("The total square footage of wrapping paper needed is", sumAllAreas(filepath), "square feet.") # for part one
    print("The total length of ribbon needed is", sumAllRibbons(filepath), "feet.") # for part two

if __name__ == "__main__":
    main()
