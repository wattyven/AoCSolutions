filepath = 'Day 14 input.txt'

def getspeeds(filepath):
    '''gets the speeds from a file'''
    dict = {}
    with open(filepath, 'r') as f:
        for line in f:
            line = line.split()
            reindeer = line[0] # gets the name of the reindeer
            speed = line[3]
            speed_time = line[6]
            cooldown = line[-2]
            sublist = [speed, speed_time, cooldown]
            dict[reindeer] = sublist
    return dict

def cycles_per_deer(deer, dict, duration):
    '''checks how many complete cycles (with cooldown timer) run by each deer'''
    modulusval = int(dict[deer][1]) + int(dict[deer][2])
    complete_cycles = duration // modulusval
    incomplete_time = duration % modulusval
    return complete_cycles, incomplete_time 

def distance_deer(deer, dict, duration):
    '''gets the distance run by a specific deer after a specified duration'''
    complete, incomplete = cycles_per_deer(deer, dict, duration)
    lst = dict[deer]
    complete_dist = complete*(int(lst[0]))*(int(lst[1]))
    if incomplete > int(lst[1]):
        incomplete_dist = (int(lst[0]))*(int(lst[1]))
    else:
        incomplete_dist = incomplete*(int(lst[0]))
    return complete_dist + incomplete_dist

def compare_deer(dict, duration):
    '''creates a new dictionary with each reindeer and its distance travelled'''
    race_distance = {}
    for deer in dict:
        distance = distance_deer(deer, dict, duration)
        race_distance[deer] = distance
    return race_distance

def main():
    duration = int(input("Length of race in seconds: "))
    racedict = compare_deer(getspeeds(filepath), duration)
    # part one below:
    print("The winner is", max(racedict, key=lambda key: racedict[key]), "with a distance of", racedict[max(racedict, key=lambda key: racedict[key])])
    # part two below:
    '''gets scores per reindeer after race duration, given each reindeer gets one point for being in the lead each second'''
    scoredict = {}
    for deer in racedict:
        scoredict[deer] = 0
    for i in range(duration):
        tempdict = compare_deer(getspeeds(filepath), i+1)
        leader = max(tempdict, key=lambda key: tempdict[key])
        # If there are multiple reindeer tied for the lead, they each get one point.
        for deer in tempdict:
            if tempdict[deer] == tempdict[leader]:
                scoredict[deer] += 1
    scoreleader = max(scoredict, key=lambda key: scoredict[key])
    print("The highest scorer is", scoreleader, "with a score of", scoredict[scoreleader])


if __name__ == "__main__":
    main()
