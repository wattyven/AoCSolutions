filepath = 'Day 09 input.txt'

from time import time

def openFile(filepath):
    '''splits file into lines'''
    with open(filepath, 'r') as f:
        data = f.read().splitlines()
    return(data)
                
def follow(H,T):
    '''returns the new tail position, based on the head position'''
    deltaX = (H[0] - T[0])
    deltaY = (H[1] - T[1])
    if abs(deltaX) <= 1 and abs(deltaY) <=1 : # if the tail is within one space of the head
        pass # do nothing
    elif abs(deltaX) >= 2 and abs(deltaY) >= 2: # if the tail is two spaces away from the head in both directions
        if T[0] < H[0]: # if the tail is to the left of the head
            if T[1] < H[1]: # if the tail is below the head
                T = (H[0] - 1, T[1] - 1)
            else: # if the tail is above the head
                T = (T[0] - 1, H[1] + 1)
        else: # if the tail is to the right of the head
            if T[1] < H[1]: # if the tail is below the head
                T = (H[0] + 1, T[1] - 1)
            else: # if the tail is above the head
                T = (T[0] + 1, H[1] + 1)
    elif abs(deltaX) >= 2: # if the tail is two spaces away from the head in the x direction
        if T[0] < H[0]: # if the tail is to the left of the head
            T = (H[0] - 1, T[1])
        else: # if the tail is to the right of the head
            T = (H[0] + 1, T[1])
    elif abs(deltaY) >= 2: # if the tail is two spaces away from the head in the y direction
        if T[1] < H[1]: # if the tail is below the head
            T = (T[0], H[1] - 1)
        else: # if the tail is above the head
            T = (T[0], H[1] + 1)
    return T # return the new tail position

if __name__ == '__main__':
    starttime = time()
    lines = openFile(filepath)
    H = (0,0) # initialize our head
    T = [(0,0) for num in range(9)] # initialize our tail
    X = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
    Y = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    T1 = set([T[0]]) # set of positions traveled by the snake
    T2 = set([T[8]])
    for line in lines: # for each movement instruction
        dir, mag = line.split() # split into direction and magnitude
        mag = int(mag) # convert to integer
        for move in range(mag): # move as many times as the magnitude
            H = (H[0] + X[dir], H[1] + Y[dir]) # update the head position
            T[0] = follow(H, T[0]) # update the first tail segment based on the head position
            for i in range(1, 9): # update the rest of the tail
                T[i] = follow(T[i - 1], T[i]) # tail N+1 follows tail N as our first tail followed the head
            T1.add(T[0]) # add the new tail position to the set
            T2.add(T[8]) # add the new tail position to the set
    print(len(T1)) # print the length of the set (number of unique positions)
    print(len(T2))
    print('Time taken: {:.2f} seconds'.format(time()-starttime)) # print the time taken
