filepath = "Day 3 input.txt"

# it's a spherical cow!

def readmoves(filepath):
    '''reads the moves from the input file'''
    file = open(filepath, "r") # opens the file
    inputstring = file.read() # reads the file
    return inputstring

def splitmoves(inputstring):
    '''unpacks the input string into a list of individual moves'''
    lst = [*inputstring] 
    return lst

'''for part one, the first solution to come to mind would have santa start at the 
origin (0,0), then for each move, get his updated position, and add it to a set, 
as sets can't have repeat elements; afterwards, just get the number of elements in 
the set to determine how many houses received at least one present! Not sure if
it's the most efficient solution, but it should work.'''

def updatePosition(move):
    '''gets the position of the house after the move'''
    if move == "^":
        return (0,1)
    elif move == "v":
        return (0,-1)
    elif move == ">":
        return (1,0)
    elif move == "<":
        return (-1,0)

def santasRoute(lst):
    '''gets the route of santa'''
    houses = set() # set of positions
    position = (0,0) # santa starts at the origin
    houses.add(position) # add the origin to the set
    for i in range(len(lst)): # for the number of moves santa makes
        position = tuple(map(sum, zip(position, updatePosition(lst[i])))) # get the updated position
        houses.add(position) # add the updated position to the set
    return houses # return the set of positions he visited

# oh god i just read part two and there's an elf drunk on eggnog
# if robo santa's anything like tesla autopilot there's gonna be a lot of collateral damage
'''first solution to come to mind: im going to write these down so i can keep track of how
my thought processes change as i slowly do more and more of these problems. so, for part two,
we have santa and robo santa, and they both start at the origin. we can use the same updatePosition, 
but to split their moves, we can have santa take all the odd positioned moves, and robo santa take
all the even positioned moves. we can give each of them a set of their own, and then take the union
to get the set of all the houses they visited. we can then get the number of elements in the set to
see how many houses were visited in total.'''

def splitSantas(lst):
    '''splits the moves between santa and robo santa'''
    santa = [] # list of santa's moves
    robo = [] # list of robo santa's moves
    for i in range(len(lst)):
        if i % 2 == 0: # if i is even, santa takes the move
            santa.append(lst[i])
        else: # if i is odd, robo santa takes the move
            robo.append(lst[i])
    return (santa, robo)

def twoSantaRoute(lst):
    '''gets the route of santa and robo santa'''
    (santa, robo) = splitSantas(lst) # splits the moves between santa and robo santa
    santaHouses = santasRoute(santa) # gets the route of santa
    roboHouses = santasRoute(robo) # gets the route of robo santa
    houses = santaHouses.union(roboHouses) # takes the union of the two sets to get the set of all houses visited
    return houses

def main():
    '''main, puts everything together'''
    inputstring = readmoves(filepath) # reads the moves from the input file
    lst = splitmoves(inputstring) # splits the moves into a list
    houses = santasRoute(lst) # gets the route of santa
    print("Santa visited", len(houses), "houses.") # part one
    print("After the birth of Robo-Santa, Santa and Robo-Santa visited", len(twoSantaRoute(lst)), "houses.") # part two

if __name__ == "__main__":
    main()
